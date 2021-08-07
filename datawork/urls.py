from django.urls.conf import include
from .import views
from django.urls import path

urlpatterns = [

    path('dashboard', views.dashboard, name="dashboard"),
    path("email", views.email, name='email'),
    path('error', views.error, name="error"),
    path('calendar', views.calendar, name="calendar"),
    path('charts', views.charts, name="charts"),
    path('contact', views.contact, name="contact"),
    path('dashboard_2', views.dashboard_2, name="dashboard_2"),
    path('general_elements', views.general_elements, name="general_elements"),
    path('icons', views.icons, name="icons"),
    path('index', views.index, name="index"),
    path('invoice', views.invoice, name="invoice"),
    path('contact', views.invoice, name="contact"),
    path('login', views.login, name="login"),
    path('map', views.map, name="map"),
    path('media_gallery', views.media_gallery, name="media_gallery"),
    path('price', views.price, name="price"),
    path('profile', views.profile, name="profile"),
    path('project', views.project, name="project"),
    path('settings', views.settings, name="settings"),
    path('tables', views.tables, name="tables"),
    path('widgets', views.widgets, name="widgets"),
    path('subscribers', views.subscribers, name="subscribers"),
    path('managebanner', views.managebanner, name="managebanner"),
    path('banneredit/<int:id>', views.banneredit, name="banneredit"),
    path('delete_banner/<int:id>', views.delete_banner, name="delete_banner"),
    path('update/<int:id>', views.update, name="update"),
    path('addbanner/', views.addbanner, name="addbanner"),






]
