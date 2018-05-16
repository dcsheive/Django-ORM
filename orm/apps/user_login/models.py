from django.db import models

# Create your models here.
class User(models.Model):
      first_name = models.CharField(max_length=255)
      last_name = models.CharField(max_length=255)
      email = models.CharField(max_length=255)
      age = models.IntegerField()
      created_at = models.DateTimeField(auto_now_add = True)
      updated_at = models.DateTimeField(auto_now = True)
# User.objects.all()
# User.objects.last()
# User.objects.create(first_name="Michael2",last_name="Choi2", email="mail@mail2.com", age="42")
# User.objects.create(first_name="Nina",last_name="Ramsical", email="mail@mail3.com", age="21")
# User.objects.first()
# User.objects.order_by("-first_name")  orders by first name DESC
# a = User.objects.get(id=3)
# a.last_name = "new_name"
# a.save()
# b = User.objects.get(id=4)
# b.delete()
# User.objects.get(id=4).delete()
