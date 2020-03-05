from rest_framework import serializers

class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:

        fields = ('__all__')
