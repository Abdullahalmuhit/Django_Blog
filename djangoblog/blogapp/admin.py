from django.contrib import admin
from .models import category, author, article, comment
# Register your models here.
class authorModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    class Meta:
        Model=author
admin.site.register(author, authorModel)
class articleModel(admin.ModelAdmin):
    list_display = ["__str__", "posted_on", "updated_on"]
    search_fields = ["__str__", "details"]
    list_filter = ["posted_on", "category"]
    list_per_page = 10
    class Meta:
        Model=article
admin.site.register(article, articleModel)
class categoryModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model=category
admin.site.register(category,categoryModel)

class commentModel(admin.ModelAdmin):
    list_display = ["__str__"]
    search_fields = ["__str__"]
    list_per_page = 10
    class Meta:
        Model=comment
admin.site.register(comment,commentModel)

