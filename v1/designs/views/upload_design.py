import tablib
import pathlib

from tablib.core import UnsupportedFormat

from rest_framework import parsers
from rest_framework import status
from rest_framework import views

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from v1.designs.serializers.upload_design import FileSerializer
from v1.designs.serializers.upload_design import DesignLoadSerializer

from v1.designs.models.category_design import CategoryDesign
from v1.designs.models.design import Design


# v1/admin/upload-designs/
class AdminUploadDesignView(views.APIView):

    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser]
    authentication_classes = [JSONWebTokenAuthentication]
    field_names = ["category", "name", "image"]

    serializer_class = FileSerializer
    per_row_serializer_class = DesignLoadSerializer

    def post(self, request, *args, **kwargs):
        # check file serializer
        file_serializer = FileSerializer(data=request.data)
        file_serializer.is_valid(raise_exception=True)

        dataset = self.get_dataset_or_400(
            file=file_serializer.validated_data.get("file")
        )
        dataset.headers = self.field_names

        # check data
        serializer = DesignLoadSerializer(data=dataset.dict, many=True)
        serializer.is_valid(raise_exception=True)

        data = [dict(value) for value in serializer.validated_data]
        for value in data:

            try:
                category_design = CategoryDesign.objects.get(slug=value.get("category"))
            except CategoryDesgin.DoesNotExist as e:
                raise ValidationError({"detail": e.args[0]})

            Design.objects.get_or_create(
                category_design=category_design,
                name=value.get("name"),
                img=value.get("image"),
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
