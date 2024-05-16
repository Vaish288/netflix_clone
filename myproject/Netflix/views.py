from django.contrib.auth import authenticate, login
#from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from .forms import SignupForm
from .models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import MoviesSerializer, TVShowsSerializer, EpisodeSerializer


#def getData(request):
    #app = Movies.objects.all()
    #serializer = DataSerializer(app, many=True)
    #return Response(serializer.data)

@api_view(['POST'])
#def postData(request):
    #serializer = DataSerializer(data=request.data)
    #if serializer.is_valid():
        #serializer.save()
    #return Response(serializer.data)

def in_view(request):
    if request.method=='POST':
        return redirect('signup')
    return render(request, 'in.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('login')  
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('subscription')  # Redirect to the subscription page
    return render(request, 'login.html')

def subscription_view(request):
    if request.method == 'POST':
        plan_id = request.POST.get('plan')
        if plan_id:
            return redirect('home')
    plans = SubscriptionPlan.objects.all()
    return render(request, 'subscription.html', {'plans': plans})
    
@api_view(['GET'])
def home(request):
    movies = Movies.objects.all()
    tv_shows=TVShows.objects.all()
    movies_serializer = MoviesSerializer(movies, many=True)
    tvShow_serializer = TVShowsSerializer(tv_shows, many=True)
    return Response(
        {
            'Movies': movies_serializer.data,
            'TV_Shows': tvShow_serializer.data,
        }
        )

@api_view(['GET'])
def episodes(request):
    episodes= Episodes.objects.all()
    tv_shows=TVShows.objects.all()
    episode_serializer=EpisodeSerializer(episodes, many=True)
    tvShow_serializer = TVShowsSerializer(tv_shows, many=True)
    return Response(
        {
            'TV_shows':tvShow_serializer.data,
            'Episodes':episode_serializer.data

        }
    )