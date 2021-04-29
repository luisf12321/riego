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

urlpatterns = [
    path('hello/', local_view.hello_world),
    path('hi/', local_view.hi),
    path('hi2/', local_view.hi2),
    path('hi3/<str:nombre>/<int:edad>/', local_view.hi3),
    path("usuario/", usuario_view.list_usuario),
    path("user/", usuario_view.usuarios),
]
