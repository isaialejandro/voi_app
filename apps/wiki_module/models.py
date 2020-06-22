from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User


"""
Wiki Module--

*BlogDoc:
Destinado para artículos pequeños o grandes acerca de funciones, instrucciones cortas,
 acciones extra relacionados con aplicaciones,
interfaces, etc. Estos se encontrarán dentro de la misma aplicación con PageDown.

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


ACTIVE = 'active'
INACTIVE = 'inactive'
STATUS = [
    (ACTIVE, 'Active'),
    (INACTIVE, 'Inactive'),
]


class Tags(models.Model):

    key = models.CharField(max_length=10, null=False, blank=False, default='')
    name = models.CharField(max_length=30, blank=True, null=False)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)


class WikiModule(models.Model):

    #NOT IN USE
    #blog_visits = models.CharField(max_length=999999, blank=True, null=True)
    #article_visits = models.CharField(max_length=999999, blank=True, null=True)


    class Meta:

        permissions = (
            ('view_wiki_module', 'Visualize Wiki Module'),
        )


class BlogDoc(models.Model):

    key = models.CharField(max_length=500, null=False, blank=False, default='')
    title = models.CharField(max_length=200,  blank=False, null=False)
    description = models.CharField(max_length=350, blank=True, null=True)
    reg_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateField(blank=True, null=True)
    content = models.TextField(max_length=15000, blank=False, null=False)
    views = models.IntegerField(blank=True, null=True)
    blog_tags = models.TextField(max_length=250, blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)
    update_user = models.ForeignKey(User, blank=True, null=True, on_delete=models.DO_NOTHING, related_name='app_update_user')
    status = models.CharField(max_length=8, choices=STATUS, default=ACTIVE)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='created_by')

    def __str__(self):
        return self.title.capitalize() + ' | ' + '{}'.format(self.reg_date)

    class Meta:

        permissions = (
            ('view_app_document_list', 'Visualize AppDocs List'),
            ('create_app_document', 'Create new AppDoc'),
            ('update_app_document', 'Update current AppDoc'),
        )


class ArticleFile(models.Model):

    key = models.CharField(max_length=500, null=False, blank=False, default='')
    name = models.CharField(max_length=200,  blank=False, null=False)
    article_version = models.CharField(max_length=200,  blank=False)
    desc = models.CharField(max_length=100,  blank=False, null=False)
    file = models.FileField(upload_to='uploads/wiki_module/articles/', blank=True, null=True)
    views =  models.IntegerField()
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
