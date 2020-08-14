from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('article', views.ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),

    # path('', views.article_list, name="list"),
    # path('detail/<int:pk>/', views.article_detail, name="detail"),

    path('article/', views.ArticleAPIView.as_view(), name="classApi-list"),
    path('detail/<int:id>/', views.ArrticleApiDetails.as_view(), name="classApi-detail"),

    path('generic/articles/', views.GenericAPIView.as_view(), name="GenericAPIView-list"),
    path('generic/articles/<int:id>/', views.GenericAPIView.as_view(), name="GenericAPIView-details"),

]