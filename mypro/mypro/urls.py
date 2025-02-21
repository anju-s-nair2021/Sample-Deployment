"""
URL configuration for mypro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import myapp.views 
from django.conf.urls.static import static
from mypro import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myapp.views.first_pgm,name='first_page'),
    path('state/',myapp.views.state,name='state'),
    path('district/',myapp.views.district,name='district'),
    path('reg/',myapp.views.reg,name='reg'),
    path('login/',myapp.views.login,name='login'),
    path('userhome/',myapp.views.userhome,name='userhome'),
    path('adminhome/',myapp.views.adminhome,name='adminhome'),
    path('viewuser/',myapp.views.viewuser,name='viewuser'),
    path('edituser/',myapp.views.edituser,name='edituser'),
    path('deleteuser/<id>',myapp.views.deleteuser,name='deleteuser'),
    path('viewuser_qry/',myapp.views.viewuser_qry,name='viewuser_qry'),
    path('search/',myapp.views.search,name='search'),
    path('index/',myapp.views.index,name='index'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
