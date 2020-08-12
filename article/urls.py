from django.urls import path

from . import views

urlpatterns = [
    # path('', views.article_list, name="list"),
    # path('detail/<int:pk>/', views.article_detail, name="detail"),

    path('article/', views.ArticleAPIView.as_view(), name="classApi-list"),
    path('detail/<int:id>/', views.ArrticleApiDetails.as_view(), name="classApi-detail"),


]