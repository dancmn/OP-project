from ast import literal_eval

from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, MarkerForm
from .models import UserAccount, Marker
from django.forms.models import model_to_dict
import json

def index(request):
    if request.method == 'POST':
        form = MarkerForm(request.POST)
        user = request.user
        markerName = form.data["markerName"]
        description = form.data["description"]
        photo = request.FILES["photo"]
        latitude = form.data["latitude"]
        longitude = form.data["longitude"]
        form.instance.user = user
        marker = Marker(user=user,
                        markerName=markerName,
                        description=description,
                        photo=photo,
                        latitude=latitude,
                        longitude=longitude)
        marker.save()
        return redirect(to='/')
    else:
        form = MarkerForm()
        return render(request, 'index.html', {"open_markers": list(Marker.objects.filter(opened=True)),
                                              "closed_markers": list(Marker.objects.filter(opened=False)),
                                              'form': form})


# Create your views here.
# Home page

# signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# login page
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, name=name, password=password)
            if user:
                login(request, user)
                return redirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


# logout page
def user_logout(request):
    logout(request)
    return redirect('login')


def ymap(request):
    if request.method == 'POST':
        try:
            userName = request.session.get('user')
            user = UserAccount.objects.get(id=userName)
        except:
            return redirect('login')
        markerName = request.POST.get('markerName')
        description = request.POST.get('description')
        pollutionLevel = request.POST.get('pollutionLevel')
        latitude = request.POST.get('latitude')
        longitude = request.POST.get('longitude')
        photo = request.FILES.get('photo')
        marker = Marker(markerName=markerName, description=description, pollutionLevel=pollutionLevel, photo=photo,
                        latitude=latitude, longitude=longitude, user=user)
        marker.save()


def markers(request):
    all_markers = serializers.serialize('json', Marker.objects.all())
    return JsonResponse(all_markers, safe=False)


def join(request):
    data = request
    body = data.body
    dic = bytes.decode(body)
    dic = literal_eval(dic)
    print(body, dic)
    mid = dic["id"]
    m: Marker = Marker.objects.get(pk=mid)
    m.signed.add(request.user)
    m.save()
    return redirect(to="/")
