from django.urls import path
from views.example import ExampleView


urlpatterns = [
    path('example', ExampleView.as_view(),)
]
