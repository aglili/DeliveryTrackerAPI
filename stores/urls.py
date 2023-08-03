from django.urls import path
from . import views


urlpatterns = [
    path("<str:store_id>/",views.getStore,name="get a particular store"),
    path("delete/<str:store_id>/",views.deleteStore,name="delete store"),
    path("create",views.createStore,name="create store"),
    
]