from django.urls import path
from .views import MaghaleView , Addmaghale , MaghaleDetails ,About ,search , PostLike , PostunLike


urlpatterns = [
    path('',MaghaleView.as_view(), name = 'home'),
    path('maghale/<pk>',MaghaleDetails.as_view(), name = 'details'),
    path('additem',Addmaghale , name = 'addMaghale'),
    path('aboutus/',About.as_view(), name = 'aboutus'),
    path('search/',search, name = 'search'),
    path('like/<id>',PostLike, name = 'postlike'),
    path('unlike/<id>',PostunLike, name = 'postunlike'),
]