



"""
class UpdateBaja(NeverCacheMixin, CSRFExemptMixin, LoginRequiredMixin, APIView):

    #Actualiza el campo de apps,
    #Guarda un detalle del usuario que actualizó, y que campos/apps ha actualizado.

    def get(self, request, **kwargs):

        context = {}
        context[''] = True
        context['form'] = BajaSemanalForm
        return render(request, 'bajas_semanales_form.html', context)
"""
