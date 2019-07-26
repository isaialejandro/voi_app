from django.db import models

from django.contrib.auth.models import User


class Applicant(models.Model):

    id_ambassador = models.CharField(max_length=20, null=True)
    no_ambassador = models.CharField(max_length=20, null=True)


    first_name = models.CharField(max_length=50, blank=False)
    #last_name = models.CharField(max_length=50, blank=False, default='')

    frst_lastname = models.CharField(max_length=50, blank=False, default='')
    scnd_lastname = models.CharField(max_length=50, blank=False, default='')

    id_puesto = models.CharField(max_length=4, null=True)
    id_area_chief = models.CharField(max_length=4, null=True)
    id_area_dir = models.CharField(max_length=4, null=True)
    id_area_ger = models.CharField(max_length=4, null=True)
    id_area_jef = models.CharField(max_length=4, null=True)
    no_ambassador_boss = models.CharField(max_length=20, null=True)
    id_ambassador_status = models.CharField(max_length=2, null=True)
    id_station = models.CharField(max_length=4, null=True)
    genere = models.CharField(max_length=20, null=True)
    id_cc_nomina = models.CharField(max_length=4, null=True)
    id_cc_pases = models.CharField(max_length=4, null=True)
    id_cc_cobus = models.CharField(max_length=4, null=True)
    ingress_date = models.CharField(max_length=20, null=True)
    birth_date = models.CharField(max_length=20, null=True)
    rfc = models.CharField(max_length=25, null=True)
    curp = models.CharField(max_length=25, null=True)
    plaza = models.CharField(max_length=20, null=True)
    process = models.CharField(max_length=2, null=True)
    id_enterprise = models.CharField(max_length=4, null=True)

    registry_date = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(default='')

    is_active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, default='')

    def __str__(self):
        return self.first_name.capitalize() + ' ' + self.last_name.title()

    class Meta:

        permissions = (
            ('view_applicant_list', 'Can visualize applicant list'),
            ('create_applicant', 'Can create applicant'),
            ('can_disable_applicant', 'Can disable Applicant'),
        )
