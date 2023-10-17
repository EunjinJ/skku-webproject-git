from django.contrib import admin

# Register your models here.
from board.models import Trip, TripComment, Review, ReviewComment
admin.site.register(Trip)
admin.site.register(TripComment)
admin.site.register(Review)
admin.site.register(ReviewComment)