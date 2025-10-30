from django.urls import path
from .views import ProcessImagesView

urlpatterns = [
    path('process/', ProcessImagesView.as_view(), name='download_images')
]
