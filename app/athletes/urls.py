from django.urls import path
from django.conf.urls import url
from athletes import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/weightclasses', views.weightclasses_Api),
    path('api/weightclasses/<int:pk>', views.weight_class_detail),
    path('api/athletes', views.athlete_Api),
    path('api/athletes/<int:pk>', views.athlete_datail),
    # path('api/athletes/SaveFile', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# urlpatterns = [
#     url('api/weightclasses/', views.weightclasses_Api),
#     url('api/weightclasses/<int:pk>', views.weight_class_detail)
# ]

