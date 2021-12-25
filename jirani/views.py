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
    current_user = request.user
    if Profile is None:
                profile = Profile.objects.filter(user_id=current_user.id).first()
                locations = Location.objects.all()
                nextdoor = Nextdoor.objects.all()
                category = Category.objects.all()
                businesses = Business.objects.filter(user_id=current_user.id)
                contacts = Contact.objects.filter(user_id=current_user.id)
                return render(request, "profile.html", {"danger": "Update Profile by selecting Your nextdoor name to continue 😥!!", "locations": locations, "nextdoor": nextdoor, "categories": category, "businesses": businesses, "contacts": contacts})
    else:
        nextdoor = Profile.nextdoor
        return render(request, 'index.html')
    
@login_required(login_url='/accounts/login/')
def profile(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first() 
    posts = Post.objects.filter(user_id=current_user.id)
    locations = Location.objects.all()
    nextdoor = Nextdoor.objects.all()
    category = Category.objects.all()
    businesses = Business.objects.filter(user_id=current_user.id)
    contacts = Contact.objects.filter(user_id=current_user.id)
    return render(request, 'profile.html', {'profile': profile, 'posts': posts, 'locations': locations, 'nextdoor': nextdoor, 'categories': category, 'businesses': businesses, 'contacts': contacts})


@login_required(login_url="/accounts/login/")
def update_profile(request):
    if request.method == "POST":
        current_user = request.user
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        name = request.POST["first_name"] + " " + request.POST["last_name"]
        nextdoor = request.POST["nextdoor"]
        location = request.POST["location"]
        if location == "":
            location = None
        else:
            location = Location.objects.get(name=location)
        if nextdoor == "":
            nextdoor = None
        else:
            nextdoor = Nextdoor.objects.get(name=nextdoor)
            profile_image = request.FILES["profile_pic"]
            profile_image = cloudinary.uploader.upload(profile_image)
            profile_url = profile_image["url"]
            user = User.objects.get(id=current_user.id)
        if Profile.objects.filter(user_id=current_user.id).exists():
            profile = Profile.objects.get(user_id=current_user.id)
            profile.profile_pic = profile_url
            profile.nextdoor = nextdoor
            profile.location = location
            profile.save()
        else:
            profile = Profile(user_id=current_user.id,
                name=name,
                profile_pic=profile_url,
                nextdoor=nextdoor,
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
            nextdoor = Nextdoor.objects.all()
            category = Category.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            return render(request, "profile.html", {"danger": "Update Profile by selecting Your nextdoor name to continue 😥!!", "locations": locations, "nextdoor": nextdoor, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            nextdoor = profile.nextdoor
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
                    nextdoor=nextdoor,
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
                    nextdoor=nextdoor,
                )
                post.create_post()

                return redirect("/profile", {"success": "Post Created Successfully"})

    else:
            return render(request, "profile.html", {"danger": "Post Creation Failed"})
        
@login_required(login_url="/accounts/login/")
def create_business(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST["name"]
        email = request.POST["email"]
        profile = Profile.objects.filter(user_id=current_user.id).first()
        if profile is None:
            profile = Profile.objects.filter(user_id=current_user.id).first()
            posts = Post.objects.filter(user_id=current_user.id)
            locations = Location.objects.all()
            nextdoor = Nextdoor.objects.all()
            category = Category.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            return render(request, "profile.html", {"danger": "Update Profile by selecting Your nextdoor name to continue 😥!!", "locations": locations, "nextdoor": nextdoor, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            nextdoor = profile.nextdoor
        if nextdoor == "":
            nextdoor = None
        else:
            nextdoor = Nextdoor.objects.get(name=nextdoor)
            business = Business(
            user_id=current_user.id,
            name=name,
            email=email,
            nextdoor=nextdoor,
        )
        business.create_business()

        return redirect("/profile", {"success": "Business Created Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Business Creation Failed"})

@login_required(login_url="/accounts/login/")
def create_contact(request):
    if request.method == "POST":
        current_user = request.user
        name = request.POST["name"]
        email = request.POST["email"]
        phone = request.POST["phone"]
        profile = Profile.objects.filter(user_id=current_user.id).first()
        if profile is None:
            profile = Profile.objects.filter(
                user_id=current_user.id).first()  # get profile
            posts = Post.objects.filter(user_id=current_user.id)
            locations = Location.objects.all()
            nextdoor = Nextdoor.objects.all()
            category = Category.objects.all()
            businesses = Business.objects.filter(user_id=current_user.id)
            contacts = Contact.objects.filter(user_id=current_user.id)
            return render(request, "profile.html", {"danger": "Update Profile by selecting Your nextdoor name to continue 😥!!", "locations": locations, "nextdoor": nextdoor, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
        else:
            nextdoor= profile.nextdoor
        if nextdoor == "":
            nextdoor = None
        else:
            nextdoor = Nextdoor.objects.get(name=nextdoor)

        contact = Contact(
            user_id=current_user.id,
            name=name,
            email=email,
            phone=phone,
            nextdoor=nextdoor,
        )
        contact.create_contact()

        return redirect("/profile", {"success": "Contact Created Successfully"})
    else:
        return render(request, "profile.html", {"danger": "Contact Creation Failed"})
    
@login_required(login_url="/accounts/login/")
def posts(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()  # get profile
        posts = Post.objects.filter(user_id=current_user.id)
        locations = Location.objects.all()
        nextdoor = Nextdoor.objects.all()
        category = Category.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        return render(request, "profile.html", {"danger": "Update Profile by selecting Your nextdoor name to continue 😥!!", "locations": locations, "nextdoor": nextdoor, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        nextdoor = profile.nextdoor
        posts = Post.objects.filter(nextdoor=nextdoor).order_by("-created_at")
        return render(request, "posts.html", {"posts": posts})
    
@login_required(login_url="/accounts/login/")
def alerts(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()  # get profile
        posts = Post.objects.filter(user_id=current_user.id)
        locations = Location.objects.all()
        nextdoor = Nextdoor.objects.all()
        category = Category.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        return render(request, "profile.html", {"danger": "Update Profile by selecting Your nextdoor name to continue 😥!!", "locations": locations, "nextdoor": nextdoor, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        nextdoor = profile.nextdoor
        category = Category.objects.get(name="Alerts")
        posts = Post.objects.filter(nextdoor=nextdoor, category=category).order_by("-created_at")
        return render(request, "alerts.html", {"posts": posts})
    
@login_required(login_url="/accounts/login/")
def business(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()  # get profile
        posts = Post.objects.filter(user_id=current_user.id)
        locations = Location.objects.all()
        nextdoor = Nextdoor.objects.all()
        category = Category.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        return render(request, "profile.html", {"danger": "Update Profile by selecting Your nextdoor name to continue 😥!!", "locations": locations, "nextdoor": nextdoor, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        nextdoor = profile.nextdoor
        businesses = Business.objects.filter(
            nextdoor=profile.nextdoor)
        return render(request, "business.html", {"businesses": businesses})
    
@login_required(login_url="/accounts/login/")
def contacts(request):
    current_user = request.user
    profile = Profile.objects.filter(user_id=current_user.id).first()
    if profile is None:
        profile = Profile.objects.filter(
            user_id=current_user.id).first()  # get profile
        posts = Post.objects.filter(user_id=current_user.id)
        locations = Location.objects.all()
        nextdoor = Nextdoor.objects.all()
        category = Category.objects.all()
        businesses = Business.objects.filter(user_id=current_user.id)
        contacts = Contact.objects.filter(user_id=current_user.id)
        return render(request, "profile.html", {"danger": "Update Profile by selecting Your nextdoor name to continue 😥!!", "locations": locations, "nextdoor": nextdoor, "categories": category, "businesses": businesses, "contacts": contacts, "posts": posts})
    else:
        nextdoor = profile.nextdoor
        contacts = Contact.objects.filter(
            nextdoor=profile.nextdoor).order_by("-created_at")
        return render(request, "contacts.html", {"contacts": contacts, "nextdoor": Profile.nextdoor})
    
@login_required(login_url="/accounts/login/")
def search(request):
    if 'search_term' in request.GET and request.GET["search_term"]:
        search_term = request.GET.get("search_term")
        searched_businesses = Business.objects.filter(name__icontains=search_term)
        message = f"Search For: {search_term}"

        return render(request, "search.html", {"message": message, "businesses": searched_businesses})
    else:
        message = "You haven't searched for any term"
        return render(request, "search.html", {"message": message})


