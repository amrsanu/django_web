"""Views for the blog App"""

from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

post_data = [
    {
        "slug": "hike-in-mountains",
        "image": "mountains.jpg",
        "author": "Amrendra",
        "date": datetime.now(),
        "title": "Mountain Hiking",
        "excerpt": """Hiking is a long, vigorous walk, usually on trails or 
        footpaths in the countryside. Walking for pleasure 
        developed in Europe during the eighteenth century.""",
        "content": """
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Illum, iure pariatur! Nemo facilis impedit quidem voluptate ut. 
        Expedita tempore quam sapiente nihil, libero, eos ab reprehenderit molestias autem asperiores maiores.
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Illum, iure pariatur! Nemo facilis impedit quidem voluptate ut. 
        Expedita tempore quam sapiente nihil, libero, eos ab reprehenderit molestias autem asperiores maiores.
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Illum, iure pariatur! Nemo facilis impedit quidem voluptate ut. 
        Expedita tempore quam sapiente nihil, libero, eos ab reprehenderit molestias autem asperiores maiores.
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Illum, iure pariatur! Nemo facilis impedit quidem voluptate ut. 
        Expedita tempore quam sapiente nihil, libero, eos ab reprehenderit molestias autem asperiores maiores.
                Lorem ipsum dolor sit amet consectetur, adipisicing elit. 
        Illum, iure pariatur! Nemo facilis impedit quidem voluptate ut. 
        Expedita tempore quam sapiente nihil, libero, eos ab reprehenderit molestias autem asperiores maiores.
        """,
    },
    {
        "slug": "programming-is-fun",
        "image": "programming-is-fun.jpg",
        "author": "Amrendra",
        "date": datetime.now(),
        "title": "Programming is Fun",
        "excerpt": """Logic errors can be difficult to solve. 
        Sometimes they are difficult to find, too. 
        The code compiles and runs, but it …""",
        "content": """
        Logic errors can be difficult to solve. Sometimes they are difficult to find, too. 
        The code compiles and runs, but it behaves in a way you didn't expect.
        One way to track down a logic error is to walk line-by-line through your code. 
        Explain what each statement does as if you are talking to someone 
        who knows nothing about programming.  As you explain the logic, you might see a 
        disconnect between what you want to happen and what the code is actually doing. By 
        changing your perspective (from writing code to explaining what it does) the error
        can become obvious.
        "A very simple but particularly useful technique for finding the cause of a problem is 
        simply to explain it to someone else. The other person should look over your shoulder at the screen, 
        and nod his or her head constantly (like a rubber duck bobbing up and down in a bathtub). 
        They do not need to say a word; the simple act of explaining, step by step, what the code is 
        supposed to do often causes the problem to leap off the screen and announce itself." 
        (The Pragmatic Programmer 2nd Edition, p 94)
        """,
    },
]


def get_date(post):
    """To return the date for sorting"""
    return post["date"]


def starting_page(request):
    """Starting page: /"""
    sorted_posts = sorted(post_data, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(
        request=request,
        template_name="blog/index.html",
        context={"posts": latest_posts},
    )


def posts(request):
    """To sho all the posts"""
    return render(
        request=request,
        template_name="blog/all-posts.html",
        context={
            "posts": post_data,
        },
    )


def post_details(request, slug):
    """To open the post individually"""
    for post in post_data:
        if slug == post["slug"]:
            return render(
                request=request,
                template_name="blog/post-detail.html",
                context={"post_detail": post},
            )
    return render(request=request, template_name="404.html")
