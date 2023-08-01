from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.db.models import Avg,Count
from django.db.models.functions import Coalesce


class User(AbstractUser):
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(default=None, blank=True, null=True)
    avatar = models.ImageField(default=None, blank=True, null=True)
    first_name = models.TextField(default=None, blank=True, null=True)
    last_name = models.TextField(default=None, blank=True, null=True)
    allergy_ingrediets = models.TextField(default=None, blank=True, null=True)
    favorite_ingrediets = models.TextField(default=None, blank=True, null=True)
    def count_recipe(self):
        return self.recipe_user.aggregate(count_recipe=Count("id"))
    def count_follower(self):
        return self.follow_user.aggregate(count_follower=Count("follow_by"))
   
class Recipe(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE, related_name='recipe_user')
    create_at = models.DateField(default=timezone.localtime())
    title = models.TextField()
    description = models.TextField()
    ingredients = models.TextField()
    image = models.ImageField(null=True, upload_to='images/')
    directions = models.TextField()
    totalTime = models.IntegerField()
    categories = models.TextField(null=True)
    recipe_allergy_ingrediets = models.TextField(default=None, blank=True, null=True)
    recipe_favorite_ingrediets = models.TextField(default=None, blank=True, null=True)
    def rating(self):
       
        return self.recipe_review_rating.aggregate(avg_rating=Coalesce(Avg('rating'),0.0))
       
    def review(self):
        return self.recipe_review_rating.aggregate(count_review=Count('review'))
    def category(self):
        return self.categories.split(",")

    


class Review_Rating(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="review_rating_user")
    review = models.TextField(null=False)
    rating = models.IntegerField(null=False)
    recipe = models.ForeignKey(Recipe, null=False, on_delete=models.CASCADE, related_name='recipe_review_rating')
    create_at = models.DateField(default=timezone.localtime())

class CollectionName(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name='collection_name_user')
    collection_name = models.TextField(null=False)
    collectionImg = models.TextField(null=True, blank=True, default=None)
    def itemCount(self):
        return self.collections_collection_name.aggregate(count_item = Count('recipe'))
    def serialize(self):
        return {
            "id": self.id,
            "collection_name": self.collection_name,
            "collectionImg": self.collectionImg,
           
        }
    class Meta:
        unique_together = ['user','collection_name']
class Collections(models.Model):
    collection_name = models.ForeignKey(CollectionName, null=False, on_delete=models.CASCADE, related_name="collections_collection_name")
    recipe = models.ForeignKey(Recipe, null=False, on_delete=models.CASCADE)

class Following(models.Model):
    follow_by = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="follow_by_user")
    follow = models.ForeignKey(User, null=False, on_delete=models.CASCADE, related_name="follow_user")


