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
                neighbourhood = Nextdoor.objects.all()
                category = Category.objects.all()
                businesses = Business.objects.filter(user_id=current_user.id)
                contacts = Contact.objects.filter(user_id=current_user.id)
                return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        neighbourhood = profile.neighbourhood
        posts = Post.objects.filter(neighbourhood=neighbourhood).order_by("-created_at")
        return render(request, 'index.html', {'posts': posts})
    
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first() 
    posts = Post.objects.filter(user_id=current_user.id)
    locations = Location.objects.all()
    neighbourhood = Nextdoor.objects.all()
    category = Category.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    contacts = Contact.objects.filter(user_id=current_user.id)
    return render(request, 'profile.html', {'profile': profile, 'posts': posts, 'locations': locations, 'neighbourhood': neighbourhood, 'categories': category, 'businesses': businesses, 'contacts': contacts})


@login_required(login_url="/accounts/login/")
def update_profile(request):
    if request.method == "POST":
        current_user = request.user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        name = request.POST["first_name"] + " " + request.POST["last_name"]
        neighbourhood = request.POST["neighbourhood"]
        location = request.POST["location"]
        if location == "":
            location = None
        else:
            location = Location.objects.get(name=location)
        if neighbourhood == "":
            neighbourhood = None
        else:
            neighbourhood = Nextdoor.objects.get(name=neighbourhood)
            profile_image = request.FILES["profile_pic"]
            profile_image = cloudinary.uploader.upload(profile_image)
            profile_url = profile_image["url"]
            user = User.objects.get(id=current_user.id)
        if Profile.objects.filter(user_id=current_user.id).exists():
            profile = Profile.objects.get(user_id=current_user.id)
            profile.profile_pic = profile_url
            profile.neighbourhood = neighbourhood
            profile.location = location
            profile.save()
        else:
            profile = Profile(user_id=current_user.id,
                name=name,
                profile_pic=profile_url,
                neighbourhood=neighbourhood,
                location=location,
            )
            profile.save_profile()
            user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email

        user.save()
        return redirect("/profile", {"success": "Profile Updated Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Profile Update Failed"})
    
@login_required(login_url="/accounts/login/")
def create_post(request):
    if request.method == "POST":
        current_user = request.user
        title = request.POST["title"]
        content = request.POST["content"]
        category = request.POST["category"]
        location = request.POST["location"]
        profile = Profile.objects.filter(user_id=current_user.id).first()
        if profile is None:
            profile = Profile.objects.filter(
                user_id=current_user.id).first()  # get profile
            posts = Post.objects.filter(user_id=current_user.id)
            locations = Location.objects.all()
            neighbourhood = Nextdoor.objects.all()
            category = Category.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            return render(request, "profile.html", {"danger": "Update Profile by selecting Your Neighbourhood name to continue 😥!!", "locations": locations, "neighbourhood": neighbourhood, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            neighbourhood = profile.neighbourhood
        if category == "":
            category = None
        else:
            category = Category.objects.get(name=category)
        if location == "":
                location = None
        else:
                location = Location.objects.get(name=location)
        if request.FILES:
                image = request.FILES["image"]
                # upload image to cloudinary and crop it to square
                image = cloudinary.uploader.upload(
                    image, crop="limit", width=800, height=600)
                # image = cloudinary.uploader.upload(image)
                image_url = image["url"]

                post = Post(
                    user_id=current_user.id,
                    title=title,
                    content=content,
                    image=image_url,
                    category=category,
                    location=location,
                    neighbourhood=neighbourhood,
                )
                post.create_post()

                return redirect("/profile", {"success": "Post Created Successfully"})
        else:
                post = Post(
                    user_id=current_user.id,
                    title=title,
                    content=content,
                    category=category,
                    location=location,
                    neighbourhood=neighbourhood,
                )
                post.create_post()

                return redirect("/profile", {"success": "Post Created Successfully"})

    else:
            return render(request, "profile.html", {"danger": "Post Creation Failed"})
