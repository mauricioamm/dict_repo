from django.contrib import admin
from django.urls import path
from dictapp.views import listagem, update, delete, principal, criar, principal_hidden
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('listagem', listagem, name='url_listagem'),
    path('', listagem, name='url_listagem'),
    #path('novo/', nova_transacao, name= 'url_nova'),
    path('criar/', criar, name= 'url_criar'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    #path('page2/', page2, name='url_page2'),
    #path('', principal, name='url_principal'),
    path('principal/<int:pk>/', principal, name='url_principal'),
    path('principal_hidden/<int:pk>/', principal_hidden, name='url_principal_hidden'),

]
