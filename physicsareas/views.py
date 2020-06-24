from django.views.generic import ListView

from .models import AreasEspecificas

class AreaListView(ListView):
    model = AreasEspecificas

    context_object_name = 'areas_esp'

    template_name = 'area_detail.html'
    