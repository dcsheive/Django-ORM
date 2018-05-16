from django.db import models

# Create your models here.
class Dojo(models.Model):
      name = models.CharField(max_length=255)
      city = models.CharField(max_length=255)
      desc = models.CharField(max_length=255)
      state = models.CharField(max_length=2)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
class Ninja(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
      dojo = models.ForeignKey(Dojo, related_name='ninjas')

# Dojo.objects.create(name = "CodingDojo Silicon Valley", city = "Mountain View", state = "CA")
# Dojo.objects.create(name = "CodingDojo Seattle", city = "Seattle", state = "WA")
# Dojo.objects.create(name = "CodingDojo New York", city = "New York", state = "NY")
# Dojo.objects.get(id=1).delete()
# Dojo.objects.get(id=2).delete()
# Dojo.objects.get(id=3).delete()
# Dojo.objects.create(name = "CodingDojo Silicon Valley", city = "Mountain View", state = "CA")
# Dojo.objects.create(name = "CodingDojo Seattle", city = "Seattle", state = "WA")
# Dojo.objects.create(name = "CodingDojo New York", city = "New York", state = "NY")
# Ninja.objects.create(first_name = "Roger", last_name = "Ver", dojo = Dojo.objects.get(state='CA'))
# Ninja.objects.create(first_name = "Satoshi", last_name = "Nakamoto", dojo = Dojo.objects.get(state='CA'))
# Ninja.objects.create(first_name = "Sergey", last_name = "Nazarov", dojo = Dojo.objects.get(state='CA'))
# Ninja.objects.create(first_name = "Doug", last_name = "Polk", dojo = Dojo.objects.get(state='CA'))
# Ninja.objects.create(first_name = "Ro", last_name = "Ve", dojo = Dojo.objects.get(id=2))
# Ninja.objects.create(first_name = "Sa", last_name = "Na", dojo = Dojo.objects.get(id=2))
# Ninja.objects.create(first_name = "Se", last_name = "Na", dojo = Dojo.objects.get(id=2))
# Ninja.objects.create(first_name = "Do", last_name = "Po", dojo = Dojo.objects.get(id=2))
# Ninja.objects.create(first_name = "Rok", last_name = "Vek", dojo = Dojo.objects.get(id=3))
# Ninja.objects.create(first_name = "Sak", last_name = "Nak", dojo = Dojo.objects.get(id=3))
# Ninja.objects.create(first_name = "Sek", last_name = "Nak", dojo = Dojo.objects.get(id=3))
# Ninja.objects.create(first_name = "Dok", last_name = "Pok", dojo = Dojo.objects.get(id=3))
# Ninja.objects.filter(dojo__id='1')
# Ninja.objects.filter(dojo__id='3')