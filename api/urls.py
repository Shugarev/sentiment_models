from django.urls import path

from . import views

#app_name = 'api'

urlpatterns = [
    path('v4/check_text_order/', views.get_text_sentiment, name='get_text_sentiment')
]