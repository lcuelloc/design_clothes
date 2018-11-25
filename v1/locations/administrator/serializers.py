from rest_framework import serializers

from expander import ExpanderSerializerMixin

from v1.locations.models.location import Location


class AdminLocationSerializer(ExpanderSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = [
            "id",
            "user",
            "country",
            "region",
            "commune",
            "address",
            "number",
            "alias",
            "secondary_address",
            "commentary",
        ]
