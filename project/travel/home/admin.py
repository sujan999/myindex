from django.contrib import admin
from .models import Article, Hero, Story, Tag


# Register your models here.

class ArticleModelAdmin(admin.ModelAdmin):
    list_display=["__str__", "date", "draft", "image"]
    list_display_links = ["date"]
    list_editable = ["draft"]
    list_filter = ["date"]

    class Meta:
        model = Article



class HeroModelAdmin(admin.ModelAdmin):
    list_display=["__str__", "date", "caption", "image"]
    list_display_links = ["__str__"]
  
    list_filter = ["date"]

    class Meta:
        model = Hero



class StoryModelAdmin(admin.ModelAdmin):
    list_display = ["__str__","date", "title", "tag", "photographer", "draft"]
    list_dispay_links = ["__str__"]
    list_filter =["date", "tag", "photographer", "draft"]


    class Meta:
        model = Story


admin.site.register(Article, ArticleModelAdmin)
admin.site.register(Hero, HeroModelAdmin)
admin.site.register(Story, StoryModelAdmin)
admin.site.register(Tag)
