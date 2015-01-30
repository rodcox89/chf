from django.db import models
from django.contrib import admin
from .models import *


admin.site.register(SiteUser)
admin.site.register(Organization)
admin.site.register(Artisan)
admin.site.register(Agent)
admin.site.register(Product)
admin.site.register(IndividualProduct)
admin.site.register(Participant)
admin.site.register(Area)
admin.site.register(SaleItem)
admin.site.register(Item)
admin.site.register(WardrobeItem)
admin.site.register(PublicEvent)
admin.site.register(Event)
admin.site.register(Venue)
admin.site.register(Order)
admin.site.register(BulkProduct)
admin.site.register(PersonalProduct)
admin.site.register(ProductPicture)
admin.site.register(BulkDetail)
admin.site.register(RentedItem)
admin.site.register(Rental)
admin.site.register(Return)
admin.site.register(PersonalDetail)
