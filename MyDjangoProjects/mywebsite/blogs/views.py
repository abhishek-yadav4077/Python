from datetime import date
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from django.template.loader import render_to_string
from .models import Post

# Create your views here.


# def blogposts(request):
#     return HttpResponse("All blog posts!")
#     return HttpResponse("<h1>All blog posts!</h1>")


# def python_intro(request):
#     return HttpResponse("Python Post")

# def django_basics(request):
#     return HttpResponse("Django basics blog posts")

# def python_oops(request):
#     return HttpResponse("Object Oriented Programming with Python")


#instead of having all above of them separately, use the below one, now it is also length
# def blog_post(request, blog):
#     if blog == "python-intro":
#         res = "<h1>Python Post</h1>"
#     elif blog == "django-basics":
#         res = "<h1>Django basics blog posts</h1>"
#     elif blog == "python-oops":
#         res = "<h1>Object Oriented Programming with Python</h1>"
#     else:
#         return HttpResponseNotFound("<h1>Blog not found</h1>")
#
#     return HttpResponse(res)


# def blog_post_by_number(request, blog):
#     return HttpResponse(blog)


#this helps to no need to add elif elif elif statements, just write key value pair in dictionary
"""
blog_details = [
    {
        "slug": "python-intro",
        "image": "python.jpg",
        "date": date(2025, 10, 15),
        "title": "Python Introduction",
        "preview": "Python is a high-level, interpreted, and general-purpose programming language renowned for its simplicity and code readability. Created by Guido van Rossum and first released in 1991, its name was inspired by the British comedy group Monty Python. Today, Python is maintained by the Python Software Foundation (PSF) and stands as one of the most widely used languages globally, especially across data science, artificial intelligence, and web development.",

        "content": "Key Features\n\
        Simple Syntax: Python uses clean, English-like syntax. It eliminates the need for curly braces or semicolons, relying instead on clean indentation to define blocks of code.\n\
        Interpreted Language: Code is executed line-by-line, which allows for rapid prototyping and faster debugging.\n\
        Dynamically Typed: You do not need to declare variable types (like integer or string) explicitly before using them; Python determines the type at runtime.\n\
        Cross-Platform: It runs seamlessly across different operating systems, including Windows, macOS, and Linux.\n\
        \"Batteries Included\": It boasts an extensive standard library alongside thousands of third-party packages, meaning developers rarely have to write common functionalities from scratch.\n\
        \n\
        Core Use Cases\n\
        Data Science & AI: Python is the industry standard for machine learning, deep learning, and data visualization using libraries like Pandas, TensorFlow, and Scikit-learn.\n\
        Web Development: Powering back-end applications via robust frameworks like Django and Flask.\n\
        Automation & Scripting: Used heavily by system administrators and non-programmers alike to automate repetitive tasks or handle big data files.\n\
        Software Prototyping: Tech companies utilize it to build minimum viable products (MVPs) efficiently before translating them to lower-level languages if necessary."

    },
    {
        "slug": "django-basics",
        "image": "django.jpg",
        "date": date(2025, 10, 20),
        "title": "Django Basics",
        "preview": "Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. Built by experienced developers, it takes care of much of the hassle of web development, allowing you to focus on writing your app without needing to reinvent the wheel. It is free, open-source, and follows the MVT (Model-View-Template) architectural pattern.",

        "content": "Key Features\n\
        \"Batteries Included\": Django comes with almost everything a developer needs out of the box, including user authentication, content administration, site maps, and RSS feeds.\n\
        Exceptionally Secure: It helps developers avoid common security mistakes by default, offering built-in protection against threats like SQL injection, cross-site scripting (XSS), and cross-site request forgery (CSRF).\n\
        Exceedingly Scalable: Django can handle heavy traffic and massive amounts of data. Major companies like Instagram, Pinterest, and Disqus rely on Django to power their platforms.\n\
        Built-in Admin Interface: One of Django's most popular features is its ready-to-use administrative interface, which automatically generates a visual portal for managing application data.\n\
        \n\
        How It Works (MVT Architecture)\n\
        Model: Handles the data structure and interacts with the database (similar to an Object-Relational Mapper or ORM).\n\
        View: Contains the business logic. It fetches data from the Model and passes it to the Template.\n\
        Template: The presentation layer (HTML mixed with Django Template Language) that determines how the data is rendered to the user."

    },
    {
        "slug": "python-oops",
        "image": "oops.png",
        "date": date(2025, 10, 16),
        "title": "Object Oriented Programming",
        "preview": "Object-Oriented Programming (OOP) in Python is a programming paradigm that uses \"objects\" to represent data and methods. Python is a multi-paradigm language, meaning it fully supports OOP, allowing developers to structure code into reusable and modular pieces. At its core, OOP relies on Classes (blueprints or templates) and Objects (instances of those classes).",

        "content": "The Four Pillars of OOP\n\
        Encapsulation: Restricts direct access to methods and variables to prevent accidental data modification. In Python, you denote private attributes using a double underscore prefix (e.g., __variable).\n\
        Inheritance: Allows a new class (child) to adopt the attributes and methods of an existing class (parent). This promotes code reusability.\n\
        Polymorphism: Enables different classes to have methods with the same name but different behaviors. For example, a draw() method could behave differently in a Circle class versus a Square class.\n\
        Abstraction: Hides complex implementation details and only shows the essential features. Python handles this using the built-in abc (Abstract Base Classes) module."

    },
    {
        "slug": "regex",
        "image": "regex.png",
        "date": date(2025, 10, 19),
        "title": "Regular expression in Python",
        "preview": "Regular Expressions (Regex) in Python are powerful patterns used to match, search, extract, and manipulate text. Python provides built-in support for regular expressions through the re module, making it highly efficient for tasks like form validation, data scraping, and log parsing.",

        "content": "Common re Module Functions\n\
        re.search(pattern, string): Scans a string for the first match of the pattern and returns a match object.\n\
        re.match(pattern, string): Checks for a match only at the very beginning of the string.\n\
        re.findall(pattern, string): Finds all occurrences of the pattern and returns them as a list of strings.\n\
        re.sub(pattern, replacement, string): Searches for the pattern and replaces it with the specified text.\n\
        re.split(pattern, string): Splits the string into a list wherever the pattern matches.\n\
        \n\
        Key Regex Metacharacters\n\
        \\d: Matches any digit (0–9).\n\
        \\w: Matches any alphanumeric character or underscore (letters, numbers, _).\n\
        \\s: Matches any whitespace character (spaces, tabs, newlines).\n\
        +: Matches 1 or more occurrences of the preceding character.\n\
        *: Matches 0 or more occurrences of the preceding character.\n\
        ^ and $: Anchor the match to the start (^) or end ($) of a string."

    }
]
"""

'''
    {
    # "python-intro": "<h1>Python Post</h1>",
    "python-intro": "Introduction to Python",
    # "django-basics": "<h1>Django basics blog posts</h1>",
    "django-basics": "Django basics blog posts",
    # "python-oops": "<h1>Object Oriented Programming with Python</h1>",
    "python-oops": "Object Oriented Programming with Python",
    # "regex":"Regular expression in Python"
    "regex": "Regular expression in Python",

    "tkinter": None
}
'''


# def blogposts(request):

    #not dynamic, we need to hard coding the path
    # res_data = """
    # <ul>
    #     <li><a href="allposts/python-intro">Python Intro</a></li>
    #     <li><a href="allposts/django-basics">Django Basics</a></li>
    #     <li><a href="allposts/python-oops">Object Oriented Programming with Python</a></li>
    # </ul>
    # """
    # return HttpResponse(res_data)


def home_page(request):
    # return HttpResponse("Home page of the Blogs") #plain text
    # return HttpResponse("<h1>Home page of the Blogs</h1>")

    # res_data = render_to_string("blogs/index.html") #this function converts html files into  a string
    # return HttpResponse(res_data)

    # sorted_blogs = sorted(blog_details, key=lambda post:post['date'], reverse=True)
    # latest_blogs = sorted_blogs[:2]
    # return render(request, "blogs/index.html", {"l_blogs": latest_blogs})


    # sorted_blogs = sorted(blog_details, key=lambda post: post['date'], reverse=True)
    # latest_blogs = sorted_blogs[:2]

    latest_blogs = Post.objects.all().order_by("-date")[:2]
    return render(request, "blogs/index.html", {"l_blogs": latest_blogs})


def blogposts(request):

    #this is more dynamic
    # list_item = ""

    # blog_list = list(blog_names.keys())
    # return render(request, "blogs/allposts.html", {"blogs": blog_list})


    # for b in blog_list:
    #     blog_path = reverse("blog-post", args=[b])
    #     list_item += f'<li><a href="{blog_path}">{b.capitalize()}</a></li>'
    #
    # res_data = f"<ur>{list_item}</ul>"
    # return HttpResponse(res_data)


    # return render(request, "blogs/allposts.html", {"blogs": blog_details})

    blog_details = Post.objects.all()
    return render(request, "blogs/allposts.html", {"blogs": blog_details})


def process_blog_name(blog):
    # "python-intro" --> ["python", "intro"] --> "python intro" --> "Python Intro"
    blog_list = blog.split("-")
    # return " ".join(blog_list).title()
    return " ".join(blog_list)

"""
def get_blog_by_slug(blog_url):
    for blog in blog_details:
        if blog['slug'] == blog_url:
            return blog
    return None
"""

def blog_post(request, blog):
    # try:
    #     res = blog_names[blog]
    # except Exception:
    #     return HttpResponseNotFound("<h1>Blog not found</h1>")
    # else:
    #     return HttpResponse(res)

    try:
        # res = get_blog_by_slug(blog)

        # return render(request, "blogs/posts.html", {"blog_text": res, "blog_name": process_blog_name(blog)})

        res = Post.objects.all(slug=blog)
        return render(request, "blogs/posts.html", {"post": res})

    except Exception:
        # return HttpResponseNotFound("<h1>Blog not found</h1>")


        # res_data = render_to_string("404.html")
        # return HttpResponseNotFound(res_data)

        raise Http404()




