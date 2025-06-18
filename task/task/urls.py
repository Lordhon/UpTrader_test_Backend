
from django.contrib import admin
from django.urls import path

from menu.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('about/', index),
    path('about/team/', index),
    path('contact/', index , name='contact1'),
    path('contact/team/', index , name='contact2'),

]
