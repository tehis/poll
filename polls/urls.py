from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name = 'index'),
    path('specifics/<int:pk>/', views.DetailView.as_view(), name = 'detail'),
    path('<int:pk>/results/', views.ResultView.as_view(), name = 'results'),
    path('<int:questionId>/vote/', views.vote, name = 'vote')
]