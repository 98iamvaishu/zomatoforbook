from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
	Book_Name = models.CharField(max_length = 40)
	Book_Author = models.CharField(max_length = 40)
	image = models.ImageField(upload_to = "static/book_image", null = True )
	Summary = models.TextField()
	link = models.TextField(null = True)
	type_of_user = (
	('M', 'Mystery'),
	('O', 'Other'),
	('H', 'Horror'),
	('I', 'Inspirational'),
	('S', 'Science Fiction'))
	type_of_books = models.CharField(max_length = 10,choices = type_of_user, default = 'O' )
	User = models.ForeignKey(User, on_delete = models.CASCADE)
	pdf = models.FileField(upload_to = 'static/book_pdf', null = True , blank = True)

	def __str__(self):
		return self.Book_Name

class Comment(models.Model):
	book_id = models.ForeignKey(Book, on_delete = models.CASCADE)
	comment = models.TextField()
	user = models.ForeignKey(User, on_delete = models.CASCADE)

	def __str__(self):
		return self.book_id.Book_Name



