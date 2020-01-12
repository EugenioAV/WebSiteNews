from django.views import View
from django.shortcuts import render
from TechNews.models import *

# Create your views here.
class Home(View):
    data = dict()

    def get(self, request):
        articles = Article.objects.all()
        self.data['articles'] = articles

        return render(request, 'index.html', self.data)


class ArticleView(View):

    def get(self, request, post_id):
        article = Article.objects.filter(id=post_id).values()[0]
        return render(request, 'article.html',article)