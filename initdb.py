#!/usr/bin/env python 3

# initialize django

import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'chf.settings'
import django
django.setup()

#regular imports
import homepage.models as hmod
from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess, sys

print(hmod)

#empty (or drop) db
cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")

#create db
cursor.execute("CREATE SCHEMA PUBLIC")

#Migrage db
subprocess.call([sys.executable, "manage.py", "migrate"])

#initialize tables










#initialize tables

##########################################################################################
#########Group

#Delete old groups

##########################################################################################
#########User

##### CREATE PERMISSIONS/GROUPS #####################
Permission.objects.all().delete()
Group.objects.all().delete()

permission = Permission()
permission.codename = 'manager_rights'
permission.content_type = ContentType.objects.get(id=7)
permission.name = 'Has Manager Rights'
permission.save()

group = Group()
group.name = "Managers"
group.save()
group.permissions.add(permission)


print('permissions initialized')
#Delete old users
hmod.SiteUser.objects.all().delete()

#create som users
###############################ADD FIRST USER ###############################
u = hmod.SiteUser()
u.name = "users"
u.first_name = "rodney"
u.last_name = "cox"
u.set_password("showtime")
u.username = "rod"
u.is_superuser= True
u.is_staff= True
u.save()


###############################ARRAY OF users###############################
#Create new users: username, password, first_name, last_name, is_superuser
for data in [
  ['rodcox89', 'password', 'Rodney', 'Cox', True, True],
  ['stunna81', 'password', 'scott', 'romney', False, True],
  ['cody123', 'password', 'cody', 'anderson', False, True],
  ['csmith12', 'password', 'carter', 'Smith', False, True],
]:

    #set attributes
    u = hmod.SiteUser()
    u.username = data[0]
    u.set_password(data[1])
    u.first_name = data[2]
    u.last_name = data[3]
    u.is_superuser = data[4]
    u.is_staff = data[5]

    #save
    u.save()
    print(u.username)
    print(u.set_password)

###############################events##############################

#Delete old events
hmod.Event.objects.all().delete()

#Create new events: name, description, start, end, venue
for data in [
  ['Questival','The best day of your life','2015-04-06','2015-04-07','#igutah'],
  ['Baptism','For Dan','2015-03-12','2015-03-12','Provo Temple'],
  ['Bonfire','For the besties','2015-02-28','2015-02-28','Provo Canyon'],
  ['Dinner Nite','Going away dinner for Jeff','2015-05-05','2015-05-05','SLAB Pizza'],
]:

    #set attributes
    e = hmod.Event()
    e.name = data[0]
    e.description = data[1]
    e.start = data[2]
    e.end = data[3]
    e.location = data[4]
    #save
    e.save()
    print(e)

###############################ITEMS###############################
#Delete old items
hmod.Item.objects.all().delete()

#Create new items: name, description, value
for data in [
  ['Knife' , 'Stabbed Julius Caesar', '999','chf'],
  ['Rope' , 'Hung your mom', '1'],
  ['Backpack' , 'From Cotopaxi', '29','chf'],
  ['Canteen' , '12 oz.', '5','chf'],
]:

    i = hmod.Item()
    i.name = data[0]
    i.description = data[1]
    i.value = data[2]
    i.organization = [3]

    i.save()
    print(i)

###############################Products###############################
#
# #Delete old Products
hmod.Product.objects.all().delete()

#Create new Products: name, description, category, current_price
for data in [
  ['Poem Journal', 'Jot down anything that comes to your mind', 'Crafts', '14'],
  ['Ice', 'Cool off with this stuff', 'Household', '2'],
  ['Quil', 'Birds of a feather', 'Collectors', '8'],
  ['Abicus', 'Count better than anyone', 'Business', '13'],

]:

    p = hmod.Product()
    p.name = data[0]
    p.description = data[1]
    p.category = data[2]
    p.current_price = data[3]

    p.save()
    print(p)




###############################LOCATIONS###############################

hmod.Location.objects.all().delete()

#create new Locations: name, description, city, state

for data in [
    ['Kiwanis Park','decent tree coverage, close to the creamery','Provo','Utah'],
    ['Veterans Memorial Park','Two pavillions with basketball courts','Provo','Utah'],
    ['Larsen Park','Attached to larsen Elementary school','SF','Utah'],
    ['Brookhollow Park','a bit colder, but tons of open space','Evanston','Wyoming'],

]:

    l = hmod.Location()
    l.name = data[0]
    l.description = data[1]
    l.city = data[2]
    l.state = data[3]

    l.save()
    print(l)


###############################Venues###############################
#delete previous venues

hmod.Venue.objects.all().delete()

#create new Venue: name, Description, address, city, state, zip

for data in [

    ['usana ampitheatre','nice outdoor venue, great for concerts','332 pleasant way','West Valley','Utah','84669'],
    ['The great saltair','Old open warehouse at the edge of the great salt Lake','55 e I-80','Magna','Utah','84667'],
    ['Scera Parl','Awesome ampitheatre seats close to 4000 people, great for movies','800 north state street','Orem','Utah','84664'],
    ['Jordan towns','Has a splashpad for kids, with a nice barbeque pit','455 e main','Springville','Utah','84661'],

]:

    v = hmod.Venue()
    v.name = data[0]
    v.description = data[1]
    v.address = data[2]
    v.city = data[3]
    v.state = data[4]
    v.zip_code = data[5]

    v.save()
    print(v)


#runs server
###############################RUN SERVER###############################
subprocess.call([sys.executable, "manage.py", "runserver"])
