from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse



from .forms import ClientFilterForm


class RentaAutosClientsListSectionView(LoginRequiredMixin, TemplateView):
    template_name = 'renta_autos/list.html'


    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)

        ctx['section_name'] = 'renta_autos'
        ctx['filter_form'] = ClientFilterForm()
        return ctx



class RentaAutosModulesSectionView(LoginRequiredMixin, TemplateView):
    template_name = 'base/module.html'


    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)
        ctx['module_name'] = 'Renta de Autos'
        ctx['client_list_url'] = reverse('renta_autos:renta_autos_clients_list')
        ctx['section_name'] = 'renta_autos'

        return ctx

