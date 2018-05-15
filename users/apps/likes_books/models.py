from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
class Book(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    uploader = models.ForeignKey(User, related_name='uploaded_books')
    liked_users = models.ManyToManyField(User, related_name='liked_books')

# User.objects.create(first_name= "Mike", last_name = "Mike", email = "mail@mail.com")
# User.objects.create(first_name= "Speros", last_name = "Mike", email = "mail@mail.com")
# User.objects.create(first_name= "John", last_name = "Mike", email = "mail@mail.com")
# this_user = User.objects.get(id=1)
# Book.objects.create(name= "Java", desc="book", uploader=this_user)
# Book.objects.create(name= "Python", desc="book", uploader=this_user)
# this_user = User.objects.get(id=2)
# Book.objects.create(name= "PHP", desc="book", uploader=this_user)
# Book.objects.create(name= "Ruby", desc="book", uploader=this_user)
# this_user = User.objects.get(id=3)
# Book.objects.create(name= "C Sharp", desc="book", uploader=this_user)
# Book.objects.create(name= "MEAN", desc="book", uploader=this_user)
# this_user = User.objects.get(id=1)
# this_book = Book.objects.first()
# this_user.liked_books.add(this_book)
# this_book = Book.objects.last()
# this_user.liked_books.add(this_book)

# this_user = User.objects.get(id=2)
# this_book = Book.objects.first()
# this_user.liked_books.add(this_book)
# this_book = Book.objects.get(id=3)
# this_user.liked_books.add(this_book)

# this_user = User.objects.get(id=3)
# this_user.liked_books.add(Book.objects.get(id=1))
# this_user.liked_books.add(Book.objects.get(id=2))
# this_user.liked_books.add(Book.objects.get(id=3))
# this_user.liked_books.add(Book.objects.get(id=4))
# this_user.liked_books.add(Book.objects.get(id=5))
# this_user.liked_books.add(Book.objects.get(id=6))

# this_book = Book.objects.first()
# this_book.liked_users.all()

# this_book = Book.objects.first()
# this_book.uploader

# this_book = Book.objects.get(id=2)
# this_book.liked_users.all()

# this_book = Book.objects.get(id=2)
# this_book.uploader


