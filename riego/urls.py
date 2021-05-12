"""riego URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from riego import views as local_view
from usuario import views as usuario_view
from riegoapp import views as riegoapp_view


urlpatterns = [
    #local views riego
    path("", local_view.index),
    path("setting",local_view.setting_count, name="setting"),

    #usuarios views usuarios
    path("user/", usuario_view.usuarios, name="usuario"),
    path("login", usuario_view.login_view, name="login"),
    path("registro", usuario_view.registro, name="registro"),
    path("logout", usuario_view.logout_view, name='logout'),
    path("perfil", usuario_view.perfil, name="perfil"),

    #riego views riegoapp
    path("estadisticas", riegoapp_view.estadisticas, name="estadisticas"),
    path("calendario",riegoapp_view.calendario, name="calendario"),
    path("sectores", riegoapp_view.sectores, name="sectores"),
]
