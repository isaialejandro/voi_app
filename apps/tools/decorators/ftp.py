from ftplib import FTP
import sys
import ftplib
import os
import fnmatch

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required, permission_required

from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_exempt

from django.views import View

#Review this.
class FTPSourceMixin(object):

    def dispatch(self, *args, **kwargs):

        os.chdir(r'______________') # Directory where the files need to be downloaded
        ftp=ftplib.FTP('xxxxxxxx', 'xxxxx', 'xxxxxx') # ftp host info
        ftp.cwd('______')
        filematch='*csv'
        import time

        downloaded = []

        while True:  # runs forever
            skipped = 0

            for filename in ftp.nlst(filematch):
                if filename not in downloaded:
                    fhandle=open(filename, 'wb')
                    print 'Getting ' + filename
                    ftp.retrbinary('RETR '+ filename, fhandle.write)
                    fhandle.close()
                    downloaded.append(filename)
                else:
                    skipped += 1

            print 'Downloaded %s, skipped %d files' % (downloaded[-1], skipped)
            time.sleep(24*60*60)  # sleep 24 hours after finishing last download

        ftp.quit()

        return super(FTPSourceMixin, self).dispatch(*args, **kwargs)
