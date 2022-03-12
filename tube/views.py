from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView
from hypertube.settings import MEDIA_ROOT
from .forms import UploadVideoForm
from .models import *

VIDEOS = [
    {
        "id": 0,
        "link": "#",
        "title": "Introduction To Python",
    },
    {
        "id": 1,
        "link": "#",
        "title": "My football training",
    },
    {
        "id": 2,
        "link": "#",
        "title": "Surfing tour",
    },
    {
        "id": 3,
        "link": "#",
        "title": "Football match as a spectator",
    },
]


class MainView(View):
    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        tag = request.GET.get("tag")
        if tag:
            video_tags = VideoTag.objects.filter(tag__name=tag)
            videos = [video_tag.video for video_tag in video_tags]
            return render(request, "tube/main.html", {"videos": videos, "title": "HyperTube | Home"})

        query = request.GET.get("q")
        if query:
            videos = Video.objects.filter(title__icontains=query)
        else:
            videos = Video.find_all() or VIDEOS
        return render(request, "tube/main.html", {"videos": videos, "title": "HyperTube | Home"})


class MyLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'login.html'


class MySignupView(CreateView):
    form_class = UserCreationForm
    success_url = '/login/'
    template_name = 'signup.html'


# class MyUploadView(View):
def upload_file(request):
    if request.method == 'POST':
        form = UploadVideoForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            f = data['video']
            vid = Video.objects.create(
                title=data['title'],
                file=f.name
            )
            for tag in data['tags'].split():
                tg = Tag.objects.create(name=tag)
                VideoTag.objects.create(tag=tg, video=vid).save()
            vid.save()
            tg.save()
            with open(MEDIA_ROOT + f.name, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            return redirect('main')
    else:
        form = UploadVideoForm
    return render(request, 'upload.html', {'form': form})

