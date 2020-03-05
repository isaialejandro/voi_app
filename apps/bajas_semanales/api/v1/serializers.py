from rest_framework import serializers

from apps.bajas_semanales.models import BajaSemanal

from apps.application.api.v1.serializers import ApplicationSerializer


class BajaSemanalSerializer(serializers.ModelSerializer):

    """
    type = serializers.StringRelatedField(many=True)
    subject = serializers.CharField(max_length=200)
    user_code = serializers.CharField(max_length=20)
    user_name = serializers.CharField(max_length=20)
    request_date = serializers.DateTimeField()
    application = ApplicationSerializer(read_only=True, many=True)
    already_checked = serializers.BooleanField()
    #user = serializers.CharField(max_length=100)
    """

    class Meta:

        model = BajaSemanal
        fields = (
            'type',
            'subject',
            'user_code',
            'user_name',
            'request_date',
            'application',
            #'already_checked',
            #'user',
        )
