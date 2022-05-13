from lib2to3.pgen2 import token
from django.shortcuts import redirect, render
from .models import DemoUrl
from .forms import UrlForm
from .short import Shortner
# Create your views here.


def index(request,token):
    urls = DemoUrl.objects.all()
    print(urls.values())
    for i in urls:
        print(i)
    long_url = DemoUrl.objects.filter(short_url = token)[0]
    return redirect(long_url.long_url)

def getUrl(request):
    form = UrlForm(request.POST)
    token = ""
    if request.method == "POST":
        if form.is_valid():
            NewUrl = form.save(commit=False)
            token = Shortner().issue_token()
            token_list = [key['short_url'] for key in DemoUrl.objects.values()]
            while token in token_list:
                token = Shortner().issue_token()
            NewUrl.short_url = token
            NewUrl.save()
        else:
            form = UrlForm()
            token = "Invalid URL"
    return render(request, 'demoapp/index.html', {'form': form, 'token': token})
