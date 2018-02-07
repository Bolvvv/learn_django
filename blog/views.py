from django.shortcuts import render
#渲染，把html页面返回给浏览器
from django.http import HttpResponse
#执行响应的代码所在的模块
#代码逻辑处理的主要地点
#项目中大部分代码均在这里编写
# Create your views here.
from . import models
def index(request):
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles':articles})

def article_page(requeset, article_id)
    article = models.Article.objects.get(pk = article_id)
    return render(request, 'blog/article_page.html', {'article':article})