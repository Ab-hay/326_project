from django.contrib.auth.models import AbstractUser
from django.db import models


class Person(AbstractUser):
    description = models.TextField(blank=True)

    def __str__(self):
        return "User(<{}>)".format(self.username)


class FoodComment(models.Model):

	commenter = models.ForeignKey("Person", on_delete=models.SET_NULL, null=True)

	commentPost = models.ForeignKey("FoodPost", on_delete=models.SET_NULL, null=True)

	commentContent = models.TextField(
		max_length=1000, help_text="Enter comment"
	)

	commentScore = models.IntegerField()

	commentDateTime = models.DateTimeField(null=True, blank=True)

	class Meta:
		ordering = ["commentDateTime"]

	def __str__(self):
		return self.commentContent

	def display_author(self):
		return self.commenter


class FoodPost(models.Model):

	postScore = models.IntegerField()

	location = models.CharField(
		max_length=1000, help_text="Enter coords for the food"
	)

	postUser = models.ForeignKey("Person", on_delete=models.SET_NULL, null=True
		)

	postDate = models.DateTimeField(null=True, blank=True)

	postInfo = models.CharField(
		max_length=1000, help_text="Enter info about the food",default="Food is here"
	)

	class Meta:
		ordering = ["postDate"]

	def __str__(self):
		return self.postInfo

