"""
URL configuration for Matching_Offer_With_Cv project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from Matching_Offer_CV_App.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home ,name='home'),
    path('resultat/', resultat ,name='resultat'),


    #Views concerning offers
    path('offer/list', offer_list, name='offer_list'),
    path('offer/add/', offer_add, name='offer_add'),
    path('offer/view/<int:pk>/', offer_view, name='offer_view'),
    path('offer/edit/<int:pk>/', offer_edit, name='offer_edit'),
    path('offer/delete/<int:pk>/', offer_delete, name='offer_delete'),


    #Views concerning CVs
    path('cvs/', cv_list, name='cv_list'),
    path('cv/add/', cv_add, name='cv_add'),
    path('cv/edit/<int:pk>/', cv_edit, name='cv_edit'),
    path('cv/delete/<int:pk>/', cv_delete, name='cv_delete'),
    path('cv/view/<int:pk>/', cv_view, name='cv_view'),


    # Views related with my models
    path('cv/add_and_predict/', cv_add_and_predict, name='cv_add_and_predict'),
    path('offer/add_and_predict/', offer_add_and_predict, name='offer_add_and_predict'),


    # Views for listing seperately Offers for a Specifique class(category)
    path('offer/list_gestion/', offer_list_gestion, name='offer_list_gestion'),
    path('offer/list_informatique/', offer_list_informatique, name='offer_list_informatique'),
    path('offer/list_immobilier/', offer_list_immobilier, name='offer_list_immobilier'),
    path('offer/list_finance/', offer_list_finance, name='offer_list_finance'),
    path('offer/list_commerce/', offer_list_commerce, name='offer_list_commerce'),


    # Views for listing seperately Cvs for a Specifique category(class)
    path('cv/list_gestion/', cv_list_gestion, name='cv_list_gestion'),
    path('cv/list_informatique/', cv_list_informatique, name='cv_list_informatique'),
    path('cv/list_immobilier/', cv_list_immobilier, name='cv_list_immobilier'),
    path('cv/list_finance/', cv_list_finance, name='cv_list_finance'),
    path('cv/list_commerce/', cv_list_commerce, name='cv_list_commerce'),



]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
