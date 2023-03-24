
# Create your views here.

from django.http import HttpResponse
from django.template import loader
from blog.models import Blog


def blog(request):
    posts = Blog.objects.all().order_by('-Date')
    template = loader.get_template('index.html')
    context = {
        'posts': posts,
    }
    return HttpResponse(template.render(context, request))



