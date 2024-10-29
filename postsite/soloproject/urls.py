from django.urls import path
from .views import soloproject, index, farmer,semipage,solo, login


urlpatterns = [
    path('', soloproject, name='soloproject'),
    path('index/', index, name = 'index'),
    path('farmer/', farmer, name = 'farmer'),
    path('semipage/', semipage, name = 'semipage'),
    path('solo/', solo, name = 'solo'),
    path('login/', login, name = 'login' )
    
]
