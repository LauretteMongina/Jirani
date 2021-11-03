from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from .models import NeighbourHood, Profile, Business, Post
from .forms import UpdateProfileForm, NeighbourHoodForm, PostForm,RegistrationForm, BusinessForm
from django.contrib.auth.models import User
import datetime as dt
# Create your views here.

def registration(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            email = form.cleaned_data.get('email')
            login(request, user)
            return redirect('index')
    else:
        form = RegistrationForm()
    return render(request, 'registration/registration.html', {'form': form})


def index(request):
    return render(request, 'index.html')

@login_required(login_url='login')
def profile(request):
    profile = Profile.objects.get(user = request.user)
    if request.method == 'POST':
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            return redirect('profile', user.username)
    else:
        profile_form = UpdateProfileForm(instance=request.user.profile)
    params = {
        'profile_form': profile_form,
        'profile':profile,
    }
    return render(request, 'profile.html', params)

def single_hood(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    posts = Post.objects.filter(hood=hood)
    posts = posts[::-1]
    params = {
        'hood': hood,
        'business': business,
        'posts': posts
    }
    return render(request, 'single.html', params)

def business(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    if request.method == "POST":
        form = BusinessForm(request.POST)
        if form.is_valid():
            biz = form.save(commit=False)
            biz.hood = hood
            biz.user = request.user.profile
            biz.save()
            return redirect('single-hood', hood.id)
    else:
         form = BusinessForm()
    return render(request, 'biz.html', {'hood':hood,'business':business,'form': form,})

def news(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    posts = Post.objects.filter(hood=hood)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('single-hood', hood.id)
    else:
         form = PostForm()
    return render(request, 'news.html', {'hood':hood,'posts':posts,'form': form})

def hoods(request):
    hoodss = NeighbourHood.objects.all()
    hoodss = hoodss[::-1]
    params = {
        'hoodss': hoodss,
    }
    return render(request, 'hoods.html', params)


def new_hood(request):
    if request.method == 'POST':
        form = NeighbourHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = request.user.profile
            hood.save()
            return redirect('hood')
    else:
        form = NeighbourHoodForm()
    return render(request, 'new.html', {'form': form})
def join_hood(request, id):
    neighbourhood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = neighbourhood
    request.user.profile.save()
    return redirect('hood')
def leave_hood(request, id):
    hood = get_object_or_404(NeighbourHood, id=id)
    request.user.profile.neighbourhood = None
    request.user.profile.save()
    return redirect('hood')

@login_required(login_url='/accounts/login/')
def businesses(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    business = Business.objects.filter(neighbourhood=hood)
    return render(request, 'business.html', {'business': business})

@login_required(login_url='/accounts/login/')
def post(request, hood_id):
    hood = NeighbourHood.objects.get(id=hood_id)
    post = Post.objects.filter(hood=hood)
    return render(request, 'post.html', {'post': post})

