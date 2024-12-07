from django.contrib import admin

# Register your models here.

from django.contrib import admin

from Matching_Offer_CV_App.models import Offer
from Matching_Offer_CV_App.models import Cv

# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    list_display = ('id_offer', 'title_offer', 'description_offer','category')

class CvAdmin(admin.ModelAdmin):
    list_display = ('id_cv', 'description_cv','category')

admin.site.register(Offer, OfferAdmin)
admin.site.register(Cv, CvAdmin)