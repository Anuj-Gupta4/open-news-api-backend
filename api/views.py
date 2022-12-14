from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer
from .models import Article
from rest_framework.filters import SearchFilter
from rest_framework import generics

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/article-list/',
        'Search': '/article-search?search=gaida',
        'Detail View': '/article-detail/<str:pk>/',
        'Create': '/article-create/',
        'Update': '/article-update/<str:pk>/',
        'Delete': '/article-delete/<str:pk>/',
        'Fashion News':'article-list/fashion',
        'Sports News':'article-list/sports', 
        'National News':'article-list/national',
        'Political News':'article-list/politics',
        'Other News':'article-list/others', 
        'Finance News':'article-list/finance',
        }
    return Response(api_urls)


# @api_view(['GET'])
# def articleList(request):
#     articles = Article.objects.filter(published=True)
#     print(articles)
#     serializer = ArticleSerializer(articles, many=True)
#     return Response(serializer.data)


class UserListView(generics.ListAPIView):
    # queryset = Article.objects.all()
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer


class UserSearchView(generics.ListAPIView):
    queryset = Article.objects.filter(published=True)
    serializer_class = ArticleSerializer
    filter_backends = [SearchFilter]
    search_fields = ['$tags', '=id', '$headline', '$byline', '$published']


class NationalView(generics.ListAPIView):
    queryset = Article.objects.filter(tags='NATIONAL', published = True)
    serializer_class = ArticleSerializer


class FashionView(generics.ListAPIView):
    queryset = Article.objects.filter(tags='FASHION', published = True)
    serializer_class = ArticleSerializer


class SportsView(generics.ListAPIView):
    queryset = Article.objects.filter(tags='SPORTS', published = True)
    serializer_class = ArticleSerializer


class PoliticsView(generics.ListAPIView):
    queryset = Article.objects.filter(tags='POLITICS', published = True)
    serializer_class = ArticleSerializer


class FinanceView(generics.ListAPIView):
    queryset = Article.objects.filter(tags='FINANCE', published = True)
    serializer_class = ArticleSerializer


class OthersView(generics.ListAPIView):
    queryset = Article.objects.filter(tags='OTHERS', published = True)
    serializer_class = ArticleSerializer


@api_view(['POST'])
def articleCreate(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response("create error")

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
    return Response("update error")


@api_view(['DELETE'])
def articleDelete(request, pk):
    articles = Article.objects.get(id=pk)
    if articles:
        articles.delete()
        return Response('deleted')
    return Response('Does not exist')