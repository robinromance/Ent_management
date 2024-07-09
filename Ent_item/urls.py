from django.urls import path
from Ent_item.views import sample, create_view, delete_view, update_view, update_recd, sign_up, login_view, logout_view

urlpatterns = [
    path('sign_up/', sign_up, name="sign_up" ),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('', sample, name = 'home'),
    path('create_view/', create_view, name='create_view'),
    path('delete_view/<int:id>', delete_view, name='delete_view'),
    path('update_view/<int:id>', update_view, name='update_view'), 
    path('update_recd/<int:id>', update_recd, name='update_recd')
]
