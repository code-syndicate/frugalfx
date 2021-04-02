
from django.contrib import admin
from django.urls import path, include
from config import admin_site1
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),

	
    path('frugalfx-admin/', admin_site1.urls),

	path( 'users/' , include('users.urls') ),
	
	path( '' , include( 'main.urls' ) ) ,

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
