from django.shortcuts import render

# from django.http import HttpResponse


# Create your views here.
posts = [
    {
        "author": "Mai",
        "title": "Blog Post 1",
        "content": "First blog content",
        "date_created": "May 10, 2023",
        "blog_image": "cat.png",
    },
    {
        "author": "Nico",
        "title": "Blog Post 2",
        "content": "Second blog content",
        "date_created": "July 17, 2023",
        "blog_image": "relax.png",
    },
    {
        "author": "Ngoc",
        "title": "Blog Post 3",
        "content": "Third blog content",
        "date_created": "April 20, 2023",
        "blog_image": "savings.png",
    }
]


def home(request):
    # return HttpResponse("Home")
    context = {
        "title": "Home",
        "posts": posts
    }
    return render(request, "home.html", context)


def about(request):
    # return HttpResponse("About")
    return render(request, "about.html", {"title": "About"})
