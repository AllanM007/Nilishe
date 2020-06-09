from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import UserProfile, Review

@admin.register( UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
	model = UserProfile
	prepopulated_fields = {"slug":("user",)}

@admin.register( Review)
class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('user', 'rating', 'name', 'body', 'reviewed_on')
    list_filter = ['reviewed_on', 'name']
    search_fields = ['body']