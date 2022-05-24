from rest_framework import serializers
from .models import Resume


class ResumeSerializer(serializers.ModelSerializer):
    user_resume = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Resume
        fields = ('__all__' )