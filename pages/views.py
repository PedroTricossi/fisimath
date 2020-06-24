from django.views.generic import ListView
from .models import Areas

class HomePageView(ListView):
    model = Areas

    context_object_name = 'areas'
    
    template_name = 'index.html'