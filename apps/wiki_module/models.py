from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User


"""
Wiki Module--

*Blog:
Destinado para artículos pequeños o grandes acerca de funciones, instrucciones cortas,
 acciones extra  relacionados con aplicaciones,
interfaces, etc.

*Artículos:
Módulo para almacenamiento de artículos completos acerca de reseteo de contraseñas,
administración de interfaces, aplicaciones,

    Método de subida y versionamiento de artículos:

    -El artículo se subirá en formato PFD para ser visualizado dentro del aplicativo con un visor de PDF integrado.
    -Si se desea actualizar dicho artículo, se descargará la versión actual para modificarla en la máquina local.
    -Después de actualizarla, se procederá a subir la nueva versión. Se creará el nombre del archivo
     con una versión nueva arriba de la anterior.
    -Si existen más de 2 versiones del mismo archivo, se mostrará un listado con todas las versiones existentes del mismo.
"""


ACTIVE = 'Active'
INACTIVE = 'Inactive'
STATUS = [
    (ACTIVE, 'active'),
    (INACTIVE, 'inactive'),
]


class AppDocument(models.Model):

    title = models.CharField(max_length=200,  blank=False, null=False)
    reg_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField()
    update_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='app_update_user')
    status = models.CharField(max_length=8, choices=STATUS, default=ACTIVE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    class Meta:

        permissions = (
            ('view_app_document_list', 'Visualize AppDocs List'),
            ('create_app_document', 'Create new AppDoc'),
            ('update_app_document', 'Update current AppDoc'),
        )


class Article(models.Model):

    name = models.CharField(max_length=200,  blank=False, null=False)
    article_version = models.CharField(max_length=200,  blank=False)
    desc = models.CharField(max_length=100,  blank=False, null=False)
    file = models.FileField(upload_to='uploads/wiki_module/articles/', blank=True, null=True)
    views =  models.CharField(max_length=10, blank=True, null=False)
    reg_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    update_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='art_update_user')
    update_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=8, choices=STATUS, default=ACTIVE)

    def __str__(self):
        return self.name + ' | ' + '{}'.format(self.reg_date) + ' | ' + '{}'.format(self.author)

    class Meta:

        permissions = (
            ('view_app_article_list', 'Visualize App Article List'),
            ('create_app_article', 'Create App Article'),
            ('versioning_app_article', 'Versioning App Article'),
            ('deactivate_app_article', 'Deactivate App Article'),
        )

#class AccountReset(models.Model):
