import os

from django.conf import settings
from django.http import HttpResponse

from django.http.response import Http404

from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response


class FileAPI(APIView):

    authentication_classes = [ SessionAuthentication, BasicAuthentication ]
    permission_classes = [ IsAuthenticated ]

    def get(self, request):
        
        filename = self.request.GET.get('filename')
        user_path = 'user_files/' + filename
        #user_path = os.path.dirname(os.path.abspath('voi/')) + '/voi/media/user_files/' + filename
        file_path = os.path.join(settings.MEDIA_ROOT, user_path)

        print('FILEPATH: ', file_path)
        if os.path.exists(file_path):
            print('exists!!!!')
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/csv')
                print('FileCSV: ', response)
                response['Content-Disposition'] = 'attachment; filename="' + os.path.basename(file_path) + '"'
                # response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
                return response
        else:
            print('else!!')
            raise Http404