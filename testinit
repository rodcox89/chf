for data in [
  ['rodcox89', 'password', 'Rodney', 'Cox', True],
  ['stunna81', 'password', 'scott', 'romney', False],
  ['cody123', 'password', 'cody', 'anderson', False],
  ['csmith12', 'password', 'carter', 'Smith', False],
]:

    #set attributes
    u = hmod.SiteUser()
    u.username = data[0]
    u.set_password = data[1]
    u.first_name = data[2]
    u.last_name = data[3]
    u.is_superuser = data[4]

    #save
    u.save()

    
