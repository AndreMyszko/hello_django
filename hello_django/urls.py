"""hello_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import include, path
from core import views
from django.views.generic import RedirectView
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'movies', views.MovieViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # endpoints rest_framework
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # admin
    path('admin/', admin.site.urls),

    # redirects
    # path('', RedirectView.as_view(url='/agenda/')),

    # paths
    # login
    path('login/', views.login_user),
    path('login/submit', views.login_submit),
    path('logout/', views.logout_user),

    # agenda eventos
    path('agenda/', views.lista_eventos),
    path('agenda/evento/', views.evento),
    path('agenda/evento/submit', views.submit_evento),
    path('agenda/evento/delete/<int:id_evento>/', views.delete_evento),

    # json
    path('agenda/json/evento', views.json_lista_evento),
    path('agenda/json/evento/<int:id_usuario>', views.json_lista_evento_id),

]
