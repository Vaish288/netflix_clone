from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('in/', views.in_view, name='in'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('subscription/', views.subscription_view, name='subscription'),
    path('',views.home, name='home'),
    path('episodes/', views.episodes, name='episodes'),
   # path('data/', views.getData, name='data'),
   # path('post/', views.postData, name='post')
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)