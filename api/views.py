from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
		'List':'/article-list/',
		'Detail View':'/article-detail/<str:pk>/',
		'Create':'/article-create/',
		'Update':'/article-update/<str:pk>/',
		'Delete':'/article-delete/<str:pk>/',
		}

    return Response(api_urls)

@api_view(['GET'])
def articleList(request):
    articles = Article.objects.all()
    print(articles)
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def articleCreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save() 
    return Response(serializer.data)

@api_view(['GET'])
def articleDetail(request, pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(articles, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def articleUpdate(request, pk):
    articles = Article.objects.get(id=pk)
    serializer = ArticleSerializer(instance=articles, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data) 

@api_view(['DELETE'])
def articleDelete(request, pk):
    articles = Article.objects.get(id=pk)
    articles.delete()
    return Response('deleted')