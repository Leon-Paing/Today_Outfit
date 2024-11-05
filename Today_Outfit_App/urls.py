from django.conf import settings
from django.urls import path
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('', views.logIn, name='logIn'),
    path('signup', views.signup, name='signup'),
    path('home', views.home, name='home'),
    path('explore', views.explore, name='explore'),
    path('store_session', views.store_session, name='store_session'),
    path('like_item/<int:item_id>/',views.like_item, name='like_item'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)