from django.urls import path
from .import views


urlpatterns = [
    path('', views.main),
    path('create', views.create),
    path('login', views.login),
    path('success', views.success),
    # path('wipeDB', views.wipeDB)
]