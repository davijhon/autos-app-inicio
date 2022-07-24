from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin




class ClientsListSectionView(LoginRequiredMixin, TemplateView):
    template_name = 'clients/list.html'


    def get_context_data(self, **kwargs):
        ctx =  super().get_context_data(**kwargs)

        ctx['section_name'] = 'clientes'
        return ctx


