from django.contrib import admin
from django.urls import path, include
from qa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test),
    path('login/', views.test),
    path('signup/', views.test),
    path('question/<int:id>/', views.test),
    path('ask/', views.test),
    path('popular/', views.test),
    path('new/', views.test),
]
