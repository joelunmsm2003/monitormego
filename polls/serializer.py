from django.contrib.auth.models import User, Group
from rest_framework import serializers
from polls.models import *


class LocalSerializer(serializers.ModelSerializer):
    localplataforma = serializers.RelatedField(many=True,read_only=True)

    class Meta:
        model = Locales
        fields = '__all__'

