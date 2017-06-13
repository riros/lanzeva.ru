from django.shortcuts import render
from www.models import Slider, Gallery
from datetime import datetime


# Create your views here.
from django.utils.translation import ugettext as _
def index(request):
    sliders = Slider.objects.filter(active=True)[:6]
    gallery = Gallery.objects.filter(active=True).order_by('-id')[:6]
    test = _('Hello')
    # pdate__lte = datetime.today()
    # info = Info.objects.get()
    return render(request, 'page/index.html', context={
        'gallery': gallery,
        'sliders': sliders,
        'info': test
    })
