from django.shortcuts import render
from os import name
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
import cloudinary
import cloudinary.uploader
import cloudinary.api

# Create your views here.
@login_required(login_url='/accounts/login/')
def index(request):
    urrent_user = request.user
    if profile is None:
                profile = Profile.objects.filter(user_id=current_user.id).first()
                locations = Location.objects.all()
                neighbourhood = NeighbourHood.objects.all()
                category = Category.objects.all()
                businesses = Business.objects.filter(user_id=current_user.id)
                contacts = Contact.objects.filter(user_id=current_user.id)
                return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        neighbourhood = profile.neighbourhood
         posts = Post.objects.filter(neighbourhood=neighbourhood).order_by("-created_at")
          return render(request, 'index.html', {'posts': posts})
