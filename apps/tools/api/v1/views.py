import os

from django.core.files.storage import default_storage

from django.shortcuts import redirect, render

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
        """Receive the current filename from the template for being downloaded in the browser."""

        filename = self.request.GET.get('filename')
        user_path = 'user_files/' + filename
        file_path = os.path.join(settings.MEDIA_ROOT, user_path)
        f = default_storage.open(file_path).read()

        if os.path.exists(file_path):
            with open(file_path, 'rb') as f:
                response = HttpResponse(f.read(), content_type='application/csv')
                response['Content-Disposition'] = 'attachment; filename="' + os.path.basename(file_path) + '"' 
                return response
                #return redirect('templates/blank.html', { 'current_filename': filename })
                # return Response({'user_file': response})
        else:
            print('else!!')
            raise Http404
    