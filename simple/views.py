from django.template.loader import get_template
from django.http import HttpResponse
from django.template import Context
import datetime

def hello(request):
    now = datetime.datetime.now()
    return HttpResponse("Hello World!"+str(now))

def now(request):
    now = datetime.datetime.now()
    return HttpResponse(str(now))

def now_plus(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return HttpResponse(str(dt))

def index(request):
    now = datetime.datetime.now()
    t = get_template('index.html')
    html = t.render(Context('now':str(now)))
    return HttpResponse(html)