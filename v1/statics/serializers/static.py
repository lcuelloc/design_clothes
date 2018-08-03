from rest_framework import serializers

from v1.statics.models.static import Static


class AdminStaticSerializer(serializers.ModelSerializer):

    class Meta:
        model = Static
        fields = ["id", "stamped_light", "print_dimension", "paper_dimension"]
