from django.shortcuts import render
from django.http import HttpResponse

posts = [ 
	{ 
		'author' : 'Saloni Tyagi' ,
		'title'  : 'Blog Post 1' ,
		'Date_posted' : '20 june 2019',
		'content' : 'First Blog Post'
	} ,
	{
		'author' : 'Yukta Anand',
		'title' : 'Blog Post 2' ,
		'Date_posted' : '21 june 2019',
		'content' : 'Second Blog Post'

	}
]


def home(request):
	context = {
		'posts' : posts 
	}
	return render(request , 'blog/home.html/', context)

def about(request):
	return render(request, 'blog/about.html', {'title' : 'About'})