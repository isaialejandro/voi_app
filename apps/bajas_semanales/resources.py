from import_export import resources
from apps.bajas_semanales.models import BajaSemanal


class BajaSemanalResource(resources.ModelResource):
    class Meta:
        model = BajaSemanal
