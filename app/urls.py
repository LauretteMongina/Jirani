from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.registration, name='registration'),
    path('account/', include('django.contrib.auth.urls')),
    path('profile/', views.profile, name='profile'),
    path('hood/', views.hoods, name='hood'),
    path('new-hood/', views.new_hood, name='new-hood'),
    path('join_hood/<id>', views.join_hood, name='join-hood'),
    path('single_hood/<hood_id>', views.single_hood, name='single-hood'),
    path('<hood_id>/news', views.news, name='news'),                    
    path('<hood_id>/business',views.business,name='business'),
    path('leave_hood/<id>', views.leave_hood, name='leave-hood'),
    path('businesses/<hood_id>', views.businesses, name='businesses'),
    path('post/<hood_id>', views.post, name='post'),
]