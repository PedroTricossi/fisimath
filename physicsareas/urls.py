from django.urls import path

from .views import AreaListView

urlpatterns = [
    path('<uuid:pk>/', AreaListView.as_view(), name='area_detail'),
]