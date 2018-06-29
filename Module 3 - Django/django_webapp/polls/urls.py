from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index'),
    # site.com/polls/1
    path('<int:poll_id>/', views.detail, name='detail'),
    # site.com/1/results
    path('<int:poll_id>/results/', views.results, name='results'),
    # site.com/1/vote
    path('<int:poll_id>/vote/', views.vote, name='vote')
]