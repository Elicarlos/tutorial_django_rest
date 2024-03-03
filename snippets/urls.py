from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
]


#Não precisamos necessariamente adicionar 
#esses padrões de URL extras, mas isso nos dá uma maneira simples e limpa de nos referirmos a um formato específico.
urlpatterns = format_suffix_patterns(urlpatterns)