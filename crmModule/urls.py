from django.urls import path, include
from .views import views, sponsor, getInformation
urlpatterns = [
    
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin,name='signin'),
    path('logout/', views.signout,name='signout'),
    path('menu/', views.menu,name='menu'),
    path('sponsor/', sponsor.sponsor, name='sponsor'),
    path('sponsor/register/', sponsor.register_sponsor,name='register_sponsor'),
    path('sponsor/<int:sponsor_id>/', sponsor.sponsor_detail,name='sponsor_detail'),
    path('sponsor/<int:sponsor_id>/delete', sponsor.delete_sponsor,name='delete_sponsor'),
    path('agreement/', getInformation.getInfo, name='agreement'),
    path('agreement/<int:sponsor_id>/', getInformation.agreement, name='agreement')
    
]
