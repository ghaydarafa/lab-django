from django.urls import path
from wishlist.views import show_wishlist
from wishlist.views import show_xml

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
]