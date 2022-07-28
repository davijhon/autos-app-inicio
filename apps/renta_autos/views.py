from django.views.generic import TemplateView, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string


from utils.utils import get_secure_nro_cta_mode


from .forms import ClientRentAutoFilterForm, ClienteRentAutoEditForm
from .models import Cliente




class RentaAutosClientsListSectionView(LoginRequiredMixin, TemplateView):
    template_name = 'renta_autos/list.html'


    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)

        ctx['section_name'] = 'renta_autos'
        ctx['filter_form'] = ClientRentAutoFilterForm()
        return ctx



class RentaAutosModulesSectionView(LoginRequiredMixin, TemplateView):
    template_name = 'base/module.html'


    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['module_name'] = 'Renta de Autos'
        ctx['client_list_url'] = reverse('renta_autos:renta_autos_clients_list')
        ctx['section_name'] = 'renta_autos'

        return ctx


class RentaAutoClienteEditView(View):
    form_class = ClienteRentAutoEditForm

    def get(self, *args, **kwargs):
        uuid = self.kwargs.get('uuid', None)

        if uuid:
            instance = get_object_or_404(Cliente, id_uuid=uuid)
            form = self.form_class(instance=instance)
            ctx = {
                "form": form,
                "cli": instance,
                "rentas": instance.rentas.select_related('auto', 'cliente'),
                "nro_cta": get_secure_nro_cta_mode(instance.cuenta_numero)
            }

            return JsonResponse({
                "status": 200,
                "message": "",
                "errors": "",
                "html_content": render_to_string('renta_autos/clientes/edit_form.html', ctx, request=self.request)
            })
        else:
            return JsonResponse({
                "status": 404,
                "errors": "No se ha encontrado el respectivo ID de este registro."
            })

