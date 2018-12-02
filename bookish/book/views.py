from django.shortcuts import render, HttpResponse, redirect, render_to_response
from book.models import *
from django.contrib.auth import authenticate, login, logout
from datetime import date


def home(request):
	books = Book.objects.all()
	print(books)
	for b in books:
		print(b.Book_Name)
	return render(request, 'home.html', {'books': books})


def signin(request):
	if request.method == "POST":
		email = request.POST['email']
		password = request.POST['password']
		user = authenticate(request, username=email,
							email=email, password=password)
		if user is not None:
			login(request, user)
			fname = request.user.first_name
			return redirect("/")

	return render(request, "signin.html")


def signup(request):
	if request.method == "POST":
		# username = request.POST.get['name']
		fname = request.POST['fname']
		lname = request.POST['lname']
		password = request.POST['pass']
		email = request.POST['email']
		username = email
		user = authenticate(request, username=email, email=email,
							password=password, firstname=fname, lastname=lname)

		if user is None:
			user = User.objects.create_user(username=email, email=email,
											password=password, first_name=fname, last_name=lname)
			login(request, user)
			return redirect("/", {"fname": fname})
			print(name)
		else:
			return HttpRespose("Already exists")
	return render(request, 'signup.html')


def book(request, book_name):

	if request.method == 'POST':
		print("Hai")
		comment = request.POST.get('comment')
		print(comment)
		if comment is not None:
			print("Hello")
			c = Comment(book_id = Book.objects.get(Book_Name=book_name), comment = comment, user = request.user)
			c.save()

		return redirect(f"/book/{book_name}/")
	book = Book.objects.get(Book_Name=book_name)
	comment = Comment.objects.filter(book_id=book)
	return render(request, 'book.html', {'book':book, 'comment':comment})


def signout(request):
	logout(request)
	return redirect("/")


def create(request):

	if request.method == 'POST':
		bname = request.POST.get('bname')
		aname = request.POST.get('aname')
		image = request.FILES.get('image')
		summary = request.POST.get('summary')
		typeofbooks =  request.POST.get('typeofbooks')
		link = request.POST.get('link')
		book = Book(Book_Name=bname, Book_Author=aname, image=image,
					Summary=summary, link=link, User=request.user, type_of_books = typeofbooks)
		book.save()
		return redirect('/')

	# else:
	#     return HttpResponse("Sorry You should login")
	return render(request,'create.html')

def cat(request, tob):

	books = Book.objects.filter(type_of_books = tob)
	return render(request, 'home.html', {'books': books})


