from django.urls import path
from core.views import  *

app_name = 'core'

urlpatterns = [
    path('', main, name='main'),
    path('sheldue/',sheldue, name='sheldue'),
    path('artickles/',artickles, name='artickles'),
    path('academy/',academy, name='academy'),
]