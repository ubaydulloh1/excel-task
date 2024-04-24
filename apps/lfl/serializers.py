from rest_framework import serializers

from . import models, utils


class LFLCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LFL
        fields = (
            "id",
            "excel",
            "year",
            "month",
        )

    def create(self, validated_data):
        excel = self.context["request"].FILES["excel"]

        if models.LFL.objects.filter(
                year=validated_data["year"],
                month=validated_data["month"],
        ).exists():
            raise serializers.ValidationError(
                detail={"month": "Already uploaded for this month."}
            )

        try:
            lfl = utils.import_lfl(
                excel=excel, year=validated_data["year"], month=validated_data["month"],
            )
        except Exception as e:
            raise serializers.ValidationError(
                {"excel": "Invalid excel data."}
            )
        return lfl


class LFLListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LFL
        fields = "__all__"


class LFLDailyListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.LFLDaily
        fields = "__all__"


class LFLDetailSerializer(serializers.ModelSerializer):
    days = LFLDailyListSerializer(many=True)

    class Meta:
        model = models.LFL
        fields = "__all__"
