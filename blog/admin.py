from django.contrib import admin

# Register your models here.注册模型类
from blog.models import Article

admin.site.register(Article)