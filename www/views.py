from django.shortcuts import render
from www.models import Slider, Gallery, Blog
from datetime import datetime
from django.views.decorators.cache import cache_page


# Create your views here.
@cache_page(60*60*24*30*12)
def index(request):
    sliders = Slider.objects.filter(active=True)[:6]
    gallery = Gallery.objects.filter(active=True).order_by('-id')[:6]
    blogs = Blog.objects.filter(active=True, pdate__lte=datetime.today()).order_by('-pdate')[:2]
    from django.utils import dateformat


    # pdate__lte = datetime.today()
    # info = Info.objects.get()
    return render(request, 'page/index.html', context={
        'gallery': gallery,
        'sliders': sliders,
        'blogs': blogs,

    })
