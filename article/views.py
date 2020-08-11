from django.shortcuts import render
from django.http import JsonResponse, HttpResponse

from .models import Article
from .serializers import ArticleSerializer