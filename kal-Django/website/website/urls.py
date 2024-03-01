
from django.contrib import admin
from django.urls import path
from stocks.views import home, items, contact_us, sign
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name = 'home'),
    path('stocks/', items, name = 'items'),
    path('contact/',contact_us, name = 'contact_us'),
    path('sign/', sign, name = 'sign')
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)