import tablib
import pathlib

from tablib.core import UnsupportedFormat

from rest_framework import parsers
from rest_framework import serializers
from rest_framework import status
from rest_framework import views

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.products.models.product import Product
from v1.products.serializers.upload_product import FileSerializer
from v1.products.serializers.upload_product import ProductLoadSerializer
from v1.categories.models.category import Category
from v1.prints.models.print_type import PrintType
from v1.prints.models.print_product import PrintProduct
from v1.colors.models.color import Color
from v1.colors.models.product_color import ProductColor
from v1.images.models.image import Image
from v1.sizes.models.product_size import ProductSize
from v1.sizes.models.size import Size


# v1/admin/upload-products/
class AdminUploadProductView(views.APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser]
    authentication_classes = [JSONWebTokenAuthentication]
    field_names = [
        "category",
        "product_name",
        "product_price",
        "size",
        "print_type",
        "color",
        "front",
        "back",
        "left",
        "right",
    ]

    serializer_class = FileSerializer
    per_row_serializer_class = ProductLoadSerializer

    def post(self, request, *args, **kwargs):
        # check file serializer
        file_serializer = FileSerializer(data=request.data)
        file_serializer.is_valid(raise_exception=True)

        dataset = self.get_dataset_or_400(
            file=file_serializer.validated_data.get("file")
        )
        dataset.headers = self.field_names

        # check data
        serializer = ProductLoadSerializer(data=dataset.dict, many=True)
        serializer.is_valid(raise_exception=True)

        data = [dict(value) for value in serializer.validated_data]
        for value in data:

            try:
                category = Category.objects.get(slug=value.get("category"))
            except category.DoesNotExist as e:
                raise ValidationError({"detail": e.args[0]})

            product, _ = Product.objects.get_or_create(
                category=category,
                name=value.get("product_name"),
                defaults={"price": value.get("product_price")},
            )

            # Print types association
            split_prints = value.get("print_type").split(";")
            for prints in split_prints:
                try:
                    print_type = PrintType.objects.get(slug=prints)
                except PrintType.DoesNotExist as e:
                    raise ValidationError({"detail": e.args[0]})

                PrintProduct.objects.get_or_create(
                    product=product, print_type=print_type
                )

            # color association
            try:
                color = Color.objects.get(slug=value.get("color"))
            except Color.DoesNotExist as e:
                raise ValidationError({"detail": e.args[0]})

            # get or create product_color association
            product_color, _ = ProductColor.objects.get_or_create(
                product=product, color=color
            )

            # add images
            images = {
                "front": value.get("front"),
                "back": value.get("back"),
                "left": value.get("left"),
                "right": value.get("right"),
            }

            for key, content in images.items():
                if content:
                    Image.objects.get_or_create(
                        product_color=product_color, name=key, path=content
                    )

            # add sizes
            split_sizes = value.get("size").split(";")
            for sp_size in split_sizes:
                try:
                    size = Size.objects.get(name=sp_size.upper())
                except Size.DoesNotExist as e:
                    raise ValidationError({"detail": e.args[0]})

                # add final association
                ProductSize.objects.get_or_create(
                    product_color=product_color, size=size
                )

        return Response(status=status.HTTP_204_NO_CONTENT)

    @staticmethod
    def get_dataset_or_400(file=None):
        """
        Extract and process the information contained in the excel.

        :param file: file to process
        :type file: django.core.files.uploadedfile.InMemoryUploadedFile

        :return: dataset of processes file
        :rtype: tablib.core.Dataset
        :raises ValidationError: if `file` param is not valid, raises a 400 error
        """
        try:
            stream = file.read()
            suffix = pathlib.Path(file.name).suffix
            data = tablib.Dataset().load(stream, format=suffix.replace(".", ""))
            file.close()
            return data
        except (UnsupportedFormat, AttributeError) as e:
            raise ValidationError({"detail": e.args[0]})
