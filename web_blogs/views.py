from django.shortcuts import render

# Create your views here.
def index(request):
    """The Home page for Web Blog."""
    return render(request, 'web_blogs/index.html')