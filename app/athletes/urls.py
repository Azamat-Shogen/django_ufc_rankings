from django.urls import path
from athletes import views

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.main_page, name='home'),
    path('api/weightclasses', views.weightclasses_Api),
    path('api/weightclasses/<int:pk>', views.weight_class_detail),
    path('api/rankings-athletes', views.rankings_athlete_Api),
    path('api/rankings-athletes/<int:pk>', views.rankings_athlete_detail),
    path('api/fighters/<int:page_number>', views.fighters_Api),
    path('api/fighters/men/<int:page_number>', views.fighters_men_Api),
    path('api/fighters/women/<int:page_number>', views.fighters_women_Api),
    path('api/fighters/info/<int:pk>', views.fighter_detail)
    # path('api/athletes/SaveFile', views.SaveFile)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

