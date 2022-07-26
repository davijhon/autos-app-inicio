from django.views.generic import TemplateView



class PageHomeView(TemplateView):
    template_name = 'pages/home.html'
