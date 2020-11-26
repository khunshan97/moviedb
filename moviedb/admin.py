from django.contrib import admin
from .models import Movie, Review

# from import_export import resources
from users.models import NewUser

# Register your models here.
admin.site.register(Movie)
admin.site.register(Review)
# admin.site.register(NewUser)
#
#
# class MovieResource(resources.ModelResource):
#     class Meta:
#         model = Movie
