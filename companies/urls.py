from django.urls import path

from . import views

app_name = 'companies'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailsView.as_view(), name='detail'),
    path('<int:company_id>/apply', views.apply, name='apply')
]
