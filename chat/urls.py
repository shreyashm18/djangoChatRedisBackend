from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.showchathome,name='showchathome'),
    path('room/<str:room>/<str:user>/',views.chatpage,name='chatpage'),
    path('createGroup/',views.create_group,name='create_group'),
    path('changeMember/<str:room_name>/<str:person_name>/',views.changeMember,name = 'changeMember')
    
]
