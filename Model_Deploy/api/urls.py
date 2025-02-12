from django.urls import path
from . import views
urlpatterns = [
    path('predict/',views.predict_price,name='Predicated_Price'),
    path('scam/',views.predict_scam,name='Predicated_Scam')

]
