from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name="index"),
    path('register', views.register_login, name="register"),
    path('login', views.register_login, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("shareRecipes", views.shareRecipes, name="shareRecipes"),
    path("newCollectionItem", views.newCollectionItem, name="newCollectionItem"),
    path("unSave/<int:recipeId>", views.unSave, name="unSave"),
    path("recipe/<int:recipeId>", views.recipe, name="recipe"),     
    path("deleteCollectionItem/<int:collectionItemId>", views.deleteCollectionItem, name="deleteCollectionItem"),
    path("deleteCollection/<int:collectionId>", views.deleteCollection, name="deleteCollection"),          
    path("profile/<int:userId>", views.profile, name="profile"),
    path("follow/<int:userId>", views.follow, name="follow"),
    path("unfollow/<int:userId>", views.unfollow, name="unfollow"),
    path("profile/loadCollection", views.loadCollection, name="loadCollection"),
    path("profile/loadCollectionItem/<str:collectionName>", views.loadCollectionItem, name="loadCollectionItem"),
    path("editProfile", views.editProfile, name="editProfile"),
    path("preference", views.preference, name="preference"),
]
