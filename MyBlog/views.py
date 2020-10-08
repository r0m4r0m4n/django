from django.http import HttpRequest
from django.shortcuts import redirect


def redirect_blog(request):
    return redirect('posts_list_url', permanent=True)