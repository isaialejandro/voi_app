from django.db import models

from django.contrib.auth.models import AbstractUser

"""
class UserProfile(models.Model):

	user = models.OneToOneField(User, on_delete=models.CASCADE)


class UserPermissions(AbstractUser):

	station = models.CharField(max_length=2, default='', blank=False,  null=False)
	profile = models.ForeignKey('Profile', on_delete=models.DO_NOTHING)


	class Meta:

		permissions = (
			#TICKET
			('can_create_ticket', 'Puede crear un ticket'),
			('can_update_ticket', 'Puede actualizara un ticket'),
			('can_disable_ticket', 'Puede deshabilitar ticket'),

			#APPLICATION
			('can_add_application', 'Puede aniadir aplicacion'),
			('can_update_application', 'Puede actualizar aplicacion'),
			('can_disable_application', 'Puede deshabilitar aplicacion'),
			
			#SOLICITANTE
			('can_add_applicant', 'Puede crear solicitante'),
			('can_update_applicant', 'Puede actualizar solicitante'),
			('can_disable_applicant', 'Puede deshabilitar solicitante'),

			#USERS
			('can_view_users', 'Puede visualizar usuarios'),
			('can_add_user', 'Puede aniadir usuarios'),
			('can_update_user', 'Puede actualizar usuario'),
			('can_disable_user', 'Puede deshabilitar usuario'),
			
			('can_add_sox', 'Puede crear ticket SOX'),
			('can_update_sox', 'Puede actualizar sox'),
			('can_disable_sox', 'Puede deshabilitar ticket SOX'),
			

		)
"""

"""
class UserRol(models.Model):

	roll = models.ForeignKey()
"""