from django.contrib import admin
from .models import Listing
from .models import FeaturedPlayer
from .models import News
from .models import Post
admin.site.register(Listing)
admin.site.register(FeaturedPlayer)
admin.site.register(News)
admin.site.register(Post)
# Register your models here.
