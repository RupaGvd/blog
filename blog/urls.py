from django.urls import path
from .views import home,user_login,user_signup,dashboard,user_logout,user_profile,newpost
from django.conf.urls.static import static
from django.conf import settings

app_name = 'blog'
urlpatterns = [
    path('',home,name='home'),
    path('login',user_login,name='login'),
    path('signup',user_signup,name='signup'),
    path('logout',user_logout,name='logout'),
    path('dashboard',dashboard,name='dashboard'),
    path('profile',user_profile,name='profile'),
    path('newpost',newpost,name='newpost')
]


urlpatterns += static(settings.STATIC_URL,document_rooot=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)