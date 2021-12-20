from django.urls import path
from django.conf.urls import url
from athletes import views

urlpatterns = [
    path('api/weightclasses', views.weightclasses_Api),
    path('api/weightclasses/<int:pk>/', views.weight_class_detail)
]

# urlpatterns = [
#     url('api/weightclasses/', views.weightclasses_Api),
#     url('api/weightclasses/<int:pk>', views.weight_class_detail)
# ]

