from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.models import AbstractUser     
from django.http import HttpResponse, HttpResponseRedirect, Http404

class SiteUser(AbstractUser): 	
	address = models.CharField(max_length=60, blank=True, null=True)
	city = models.CharField(max_length=30, blank=True, null=True)
	state = models.CharField(max_length=12, blank=True, null=True)
	zip_code = models.IntegerField(max_length=5, blank=True, null=True)	
	phone = models.CharField(max_length=30, blank=True, null=True)

	class Meta:

		abstract = False
	
class Organization(models.Model):
	organization_type = models.CharField(max_length=30)
	phone = models.CharField(max_length=30, blank=True, null=True)
	creation_date = models.DateField()
	address1 = models.CharField(max_length=60)
	address2 = models.CharField(max_length=60)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=12)
	zip_code = models.IntegerField(max_length=5)
	email = models.EmailField()

class Artisan(SiteUser):
	trade = models.CharField(max_length=30)
	bio = models.TextField()
	start_year = models.DateField()

class Agent(SiteUser):
	date_appointed = models.DateField()

class Product(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=144)
	category = models.CharField(max_length=144)
	current_price = models.DecimalField(max_digits=6,decimal_places=2)

class IndividualProduct(Product):
	date_made = models.DateField()
	artisan = models.ForeignKey(Artisan)

class Participant(SiteUser):
	biographical_sketch = models.CharField(max_length=144)
	contact_relationship = models.CharField(max_length=30)
	emergency_contact = models.ForeignKey('self')  

class Area(models.Model):
	name = models.CharField(max_length=255)
	description = models.CharField(max_length=255)
	supervisor = models.ForeignKey(Agent,null=True,related_name='supervises')	
	coordinator = models.ForeignKey(Agent,null=True,related_name='coordinates')	

class Role(models.Model):
	participant = models.ForeignKey(Participant)
	area = models.ForeignKey(Area)
	name = models.CharField(max_length=30)
	role_type = models.CharField(max_length=30)

class SaleItem(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=140)
	low_price = models.DecimalField(max_digits=6,decimal_places=2)
	high_price = models.DecimalField(max_digits=6,decimal_places=2)
	area = models.ForeignKey(Area)

class Item(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=144)
    value = models.DecimalField(max_digits=6, decimal_places=2)
    organization = models.ForeignKey('Organization')
    is_rentable = models.BooleanField(default=True)

class WardrobeItem(models.Model):
    size = models.CharField(max_length=2)
    size_modifier = models.CharField(max_length=30)
    gender = models.BooleanField(default=True)
    color = models.CharField(max_length=30)
    pattern = models.CharField(max_length=30)
    start_year = models.DateField()
    end_year = models.DateField()
    note = models.CharField(max_length=255)
    is_rentable = models.BooleanField(default=False)
 
class PublicEvent(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=255)
	start_date = models.DateField()
	end_date = models.DateField()

class Event(models.Model):
	date = models.DateField()
	start_time = models.DateTimeField()
	map_url = models.URLField()
	public_event = models.ForeignKey(PublicEvent)
	area = models.ForeignKey(Area)
	venue = models.ForeignKey('Venue',null=True)

class Venue(models.Model):
	name = models.CharField(max_length=30)
	address = models.CharField(max_length=30)
	city = models.CharField(max_length=30)
	state = models.CharField(max_length=30)
	zip_code = models.IntegerField(max_length=5)

class Order(models.Model):
	customer = models.ForeignKey(SiteUser)
	order_date = models.DateTimeField()
	phone = models.CharField(max_length=30, blank=True, null=True)
	packaged_date = models.DateTimeField()
	date_shipped = models.DateTimeField()
	tracking_number = models.CharField(max_length=255)
	shipper = models.ForeignKey(Agent,null=True,related_name='ships')
	processor = models.ForeignKey(Agent,null=True,related_name='processes')
	packer = models.ForeignKey(Agent,null=True,related_name='packs')

class BulkProduct(Product):
	quantity_on_hand = models.IntegerField()
	bulk_detail = models.ManyToManyField(Order, through='BulkDetail',null=True)
	producer = models.ForeignKey(Organization)

class PersonalProduct(Product):
	order_form_name = models.CharField(max_length=30)
	production_time = models.DateTimeField()
	details = models.ManyToManyField(Order, through='PersonalDetail')
	artisan = models.ForeignKey(Artisan)

class ProductPicture(models.Model):
	picture = models.URLField()
	caption = models.CharField(max_length=255)
	product = models.ForeignKey(Product)

class BulkDetail(models.Model):
	bulk_product = models.ForeignKey(BulkProduct)
	order = models.ForeignKey(Order)
	quantity = models.IntegerField()
	price = models.IntegerField()

class RentedItem(models.Model):
	condition = models.CharField(max_length=255)
	new_damage = models.CharField(max_length=255)
	late_fee = models.DecimalField(max_digits=6,decimal_places=2)
	damage_fee = models.DecimalField(max_digits=6,decimal_places=2)
	rented_item = models.ForeignKey('Rental')

class Rental(models.Model):
	rental_time = models.DateTimeField()
	due_date = models.DateTimeField()
	discount_percent = models.DecimalField(max_digits=6,decimal_places=2)
	renting_organization = models.ForeignKey(Organization,null=True)
	rental_agent = models.ForeignKey(Agent,null=True,related_name='extends_rental')
	renting_person = models.ForeignKey(SiteUser,null=True,related_name='rents')		

class Return(models.Model):
	return_time = models.DateTimeField()
	fees_paid = models.DecimalField(max_digits=6,decimal_places=2)
	item = models.ForeignKey(RentedItem)
	return_agent = models.ForeignKey(Agent)

class PersonalDetail(models.Model):
	personal_product = models.ForeignKey(PersonalProduct)
	order = models.ForeignKey(Order)