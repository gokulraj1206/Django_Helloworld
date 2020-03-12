from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from helloworld import views
from users import views as user_views
#from .admin import MyApp_AdminSite

admin.site.site_header = "Gocool's Blog"
admin.site.site_title = "GoCool's Title"
admin.site.index_title = "GoCool's Blog Admin Page"

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('admin/', MyApp_AdminSite.urls),
    path('',include('blog.urls')),
    path('register/', user_views.register, name = "register"),
    path('profile/', user_views.profile, name = "profile"),
    path('login/', auth_views.LoginView.as_view(template_name ='users/login.html'), name = "login"),
    path('logout/', auth_views.LogoutView.as_view(template_name ='users/logout.html'), name = "logout"),

    # Hello, world!
    #path('', views.index, name='index')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
