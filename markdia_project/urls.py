"""markdia_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls.conf import include
from datawork import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.marketingindex, name="marketingindex"),
    path('marketing-blog/', views.marketingblog, name="marketingblog"),
    path('marketing-category/', views.marketingcategory,
         name="marketingcategory"),
    path('marketing-contact/', views.marketingcontact, name="marketingcontact"),
    path('marketing-single/', views.marketingsingle, name="marketingsingle"),
    path('success/', views.success, name="success"),
    path('datawork/', include('datawork.urls')),
    path('subs',views.subs,name='subs')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# path('admin_dashboard', views.admin_dashboard, name="admin_dashboard"),
# path("email", views.email, name='email'),
# path('error', views.error, name="error"),
# path('calendar', views.calendar, name="calendar"),
# path('charts', views.charts, name="charts"),
# path('contact', views.contact, name="contact"),
# path('dashboard_2', views.dashboard_2, name="dashboard_2"),
# path('general_elements', views.general_elements, name="general_elements"),
# path('icons', views.icons, name="icons"),
# path('index', views.index, name="index"),
# path('invoice', views.invoice, name="invoice"),
# path('contact', views.invoice, name="invoice"),
# path('login', views.login, name="login"),
# path('map', views.map, name="map"),
# path('media_gallery', views.media_gallery, name="media_gallery"),
# path('price', views.price, name="price"),
# path('profile', views.profile, name="profile"),
# path('project', views.project, name="project"),
# path('settings', views.settings, name="settings"),
# path('tables', views.tables, name="tables"),
# path('widgets', views.widgets, name="widgets"),
