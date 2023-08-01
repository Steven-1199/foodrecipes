from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from .models import User, Recipe, Review_Rating, CollectionName, Collections, Following
from django.db import IntegrityError
from django import forms
from django.forms import ModelForm
from django.contrib.auth.decorators import login_required
from django.db.models import Avg,Count
import json
from django.http import JsonResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt





#Create your views here.
class share_recipe_form(ModelForm):
    class Meta:
        model = Recipe
        fields=('title','description','ingredients','totalTime','directions','image', 'categories')
        widgets={'description': forms.Textarea(),'ingredients': forms.Textarea(attrs={'placeholder': 'Seperate by Colon'}),'directions': forms.Textarea(attrs={"style": "display:none", "class": "step_finish"}), 'categories': forms.TextInput(attrs={"style": "display:none", "class": "categories"})}
    
class preference_form(ModelForm):
    class Meta:
        model= User
        fields = ('allergy_ingrediets','favorite_ingrediets')
        widgets = {'allergy_ingrediets': forms.Textarea(attrs={'placeholder': 'Seperate by Colon'}),'favorite_ingrediets': forms.Textarea(attrs={'placeholder': 'Seperate by Colon'})}

class edit_profile_form(ModelForm):
    class Meta:
        model = User
        fields = ('avatar', 'email', 'bio', 'first_name', 'last_name', 'username')
        widgets = {'first_name': forms.TextInput,'last_name': forms.TextInput}

class reviews_rating_form(forms.Form):
    review = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Write a review here...'}))
    rating = forms.IntegerField()
    rating.widget = forms.NumberInput()
    rating.widget.attrs = {"style": "display:none" ,'class':'ratingInput'}

@login_required(login_url='login')
def unSave(request, recipeId):
    recipe = Recipe.objects.get(id=recipeId)
    collectionName = CollectionName.objects.filter(user = request.user)
    for i in collectionName:
        if Collections.objects.filter(collection_name = i, recipe = recipe).exists():
            Collections.objects.filter(collection_name = i, recipe = recipe).delete()
    url=reverse('recipe', kwargs={'recipeId': recipeId})
    return HttpResponseRedirect(url)

@login_required(login_url='login')
@csrf_exempt
def loadCollectionItem(request, collectionName):
    collectionItems = []
    try:
        tem = CollectionName.objects.get(user = request.user, collection_name = collectionName)
        tem = Collections.objects.filter(collection_name = tem)
        for item in tem:
            collectionItems.append({
                "id": item.id,
                "collection_name_id": item.collection_name.id,
                'recipe_id': item.recipe.id,
                "recipe_rating":item.recipe.rating(),
                "recipe_review":item.recipe.review(),
                "recipe_img": item.recipe.image.url,
                "recipe_title": item.recipe.title,
            })
    except:
        return JsonResponse({'message':"error while loading collection"}, status=400)

    return JsonResponse({"collectionItems":collectionItems}, status=200)
    

@login_required(login_url='login')
@csrf_exempt
def newCollectionItem(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            recipe = Recipe.objects.get(id = data['recipe_id'])
            for collectionName in data['collectionName']:
                tem = CollectionName.objects.get(id = collectionName)
                saveToCollection = Collections(recipe = recipe, collection_name = tem)
                saveToCollection.save()
        except:
            return JsonResponse({"message": "Invalid collection"}, status=400)

    url=reverse('recipe', kwargs={'recipeId': recipe.id})
    return HttpResponseRedirect(url)
    #return JsonResponse({"message": "success",},status=200)


@login_required(login_url='login')
@csrf_exempt
def loadCollection(request):
    try:
        collectionName = CollectionName.objects.filter(user = request.user)

    except:
        return JsonResponse({'errors': "Can't load collection"}, status=400)
    a = []
    collectionItemCount = []
    if request.path=="/profile/loadCollection":
        for v in collectionName:
            collectionItemCount.append(v.itemCount())
            if Collections.objects.filter(collection_name = v):
                
                a.append(Collections.objects.filter(collection_name = v)[0].recipe.image.url)
                v.collectionImg  = "as"
            else:
                a.append("")
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            newCollectionName = CollectionName(user=request.user, collection_name= data["collectionName"])
            newCollectionName.save()
        except:
            return JsonResponse({'errors': "Can't save collection"}, status=400)
        return JsonResponse({'message':'success'}, status=200)
    
    return JsonResponse({"collectionName":list(collectionName.values()), 'a': a,"collectionItemCount":collectionItemCount}, safe=False)

@login_required(login_url='login')
@csrf_exempt
def deleteCollection(request, collectionId):
    try:
        collection = CollectionName.objects.get(id=collectionId)
        collection.delete()
    except:
        return JsonResponse({'errors': "Can't delete collection"}, status=400)
    return JsonResponse({'message':'success'}, status=200)

@login_required(login_url='login')
@csrf_exempt
def deleteCollectionItem(request, collectionItemId):
    try:
        collectionItem = Collections.objects.get(id=collectionItemId)
        collectionItem.delete()
    except:
        return JsonResponse({'errors': "Can't delete collection"}, status=400)
    return JsonResponse({'message':'success'}, status=200)
@login_required(login_url='login')
def preference(request):
    preferenceForm = preference_form(instance=request.user)
    if request.method == 'POST':
        preferenceForm = preference_form(request.POST,instance=request.user)
        if preferenceForm.is_valid():
            preferenceForm.save()
            url=reverse('profile',kwargs={'userId':request.user.id})
            return HttpResponseRedirect(url)
    return render(request, 'base/preference.html',{'preferenceForm':preferenceForm})

@login_required(login_url='login')
def follow(request, userId):
    followUser = User.objects.get(id=userId)
    tem = Following(follow_by = request.user, follow = followUser)
    tem.save()
    url=reverse('profile',kwargs={'userId':userId})
    return HttpResponseRedirect(url)

@login_required(login_url='login')
def unfollow(request, userId):
    followUser = User.objects.get(id=userId)
    tem = Following.objects.get(follow_by = request.user, follow = followUser)
    tem.delete()
    url=reverse('profile',kwargs={'userId':userId})
    return HttpResponseRedirect(url)

@login_required(login_url='login')
def editProfile(request):
    editProfileForm = edit_profile_form(instance=request.user)
    if request.method == 'POST':
        editProfileForm = edit_profile_form(request.POST, request.FILES, instance=request.user)
        if editProfileForm.is_valid():
            editProfileForm.save()
            url=reverse('profile',kwargs={'userId':request.user.id})
            return HttpResponseRedirect(url)
    return render(request, 'base/editProfile.html',{'editProfileForm':editProfileForm})

def profile(request, userId):
    try:
        userProfile = User.objects.get(id=userId)
        recipes = Recipe.objects.filter(user= userProfile.id)
        following = Following.objects.filter(follow_by=userProfile)
        print(userProfile.avatar.url)
        if(request.user.is_authenticated):
            followOrNot = Following.objects.filter(follow_by= request.user, follow = userProfile).exists()
        else:
            followOrNot= False
        
    except:
        return HttpResponseRedirect(reverse('index'),)
    
    return render(request, 'base/profile.html',{"userProfile":userProfile, "recipes":recipes,"followOrNot":followOrNot,"following":following})

def recipe(request, recipeId):
    reviewsRatingForm = reviews_rating_form(request.POST)
    try:
        recipe = Recipe.objects.get(id=recipeId)
        reviews_ratings_output = Review_Rating.objects.filter(recipe = recipe)
    except IntegrityError:
        return HttpResponseRedirect(reverse('index'))
    recipe.ingredients=recipe.ingredients.split(";")
    recipe.directions=recipe.directions.split("; Step")
    recipe.directions = [e[4:] for e in recipe.directions]
    recipe.directions[0] = recipe.directions[0][4:]
    newDirections = list()
    for i, v in enumerate(recipe.directions):
        newDirections.append({'value': v, 'index': i +1})
    save = False
    if request.user.is_authenticated:
        collectionName = CollectionName.objects.filter(user = request.user)
        
        for i in collectionName:
            if Collections.objects.filter(collection_name = i, recipe = recipe).exists():
                save = True
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('login'))
        try:
            review_rating = Review_Rating(user=request.user, recipe=recipe, review = reviewsRatingForm.data['review'], rating=reviewsRatingForm.data['rating'])
            review_rating.save()
        except IntegrityError:
            return HttpResponseRedirect(reverse('index'))
        
    return render(request, 'base/recipe.html', {'recipe': recipe,'newDirections':newDirections, 'reviewsRatingForm':reviewsRatingForm,"reviews_ratings_output":reviews_ratings_output, 'save': save})

@login_required(login_url = 'login')
def shareRecipes(request):
    recipeForm = share_recipe_form(request.POST, request.FILES)
    if request.method == 'POST':
       if recipeForm.is_valid():
            recipe = recipeForm.save(commit=False)
            recipe.user = request.user
            recipe.save()
            url = reverse('recipe', kwargs={'recipeId': recipe.id})
            return HttpResponseRedirect(url)
       else:
           print(recipeForm.errors)
    return render(request, 'base/share_recipes.html', {'recipeForm':recipeForm})
def home(request):
    
    preference = {}
    categoryName = request.GET.get('category')
    if categoryName:
        recipes = Recipe.objects.filter(categories__contains = categoryName)
    else:
        recipes = Recipe.objects.all()
    if request.method == 'POST':
        recipes = Recipe.objects.filter(title__contains = request.POST['search'])
    if request.user.is_authenticated:
        if request.user.allergy_ingrediets:
            lts_all = request.user.allergy_ingrediets.split(";")
        else:
            lts_all = []
        if request.user.favorite_ingrediets:
            lts_fav = request.user.favorite_ingrediets.split(";")
        else:
            lts_fav = []
        for recipe in recipes:
            tem_all = list()
            tem_fav = list()
            for v in lts_all:
                if v.lower() in recipe.ingredients.lower():
                    tem_all.append(v)
            for v in lts_fav:
                if v.lower() in recipe.ingredients.lower():
                    tem_fav.append(v)
            recipe.recipe_allergy_ingrediets = tem_all
            recipe.recipe_favorite_ingrediets = tem_fav      

    return render(request, 'base/home.html',{'recipes': recipes,"categoryName":categoryName})
def register_login(request):
    if request.method == 'POST':
        if 'register_form' in request.POST:
            username = request.POST['username']
            email = request.POST['email']
            password = request.POST['password']
            comfirmation = request.POST['comfirmation']
            if password != comfirmation:
                return render(request, "base/register_login.html", {
                "message": "Passwords must match."
            })
            try:
                user = User.objects.create_user(username, email, password)
                saved_item = CollectionName(user = user, collection_name ="Saved Items")
                user.save()
                saved_item.save()
            except IntegrityError:
                return render(request, "base/register_login.html", {
                "message": "Username already exists."
            })
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        if 'login_form' in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("index"))
            else:
                 return render(request, "base/register_login.html", {
                "message": "Invalid username and/or password."
            })


    return render(request, 'base/register_login.html')

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


"""
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py sass base/static/base/styles.scss base/static/base/styles.css --watch
"""