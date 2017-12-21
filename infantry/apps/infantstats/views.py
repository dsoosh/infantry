from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from . import forms
from . import urls


def basic_stats(request):
    return render(request, "base.html")


def upload(request):
    assert isinstance(request, HttpRequest)
    if request.method == "POST":
        form = forms.UploadForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "upload.html", context={"form": form})
        else:
            return HttpResponseRedirect(reverse(urls.base_url))
    return render(request, "upload.html", context={"form": forms.UploadForm()})
