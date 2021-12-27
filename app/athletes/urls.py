from django.urls import path
from athletes import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main_page, name='home'),
    path('api/weightclasses', views.weightclasses_Api),
    path('api/weightclasses/<int:pk>', views.weight_class_detail),
    path('api/athletes', views.athlete_Api),
    path('api/athletes/<int:pk>', views.athlete_datail),
    # path('api/athletes/SaveFile', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

