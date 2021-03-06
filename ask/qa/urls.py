from django.contrib import admin
from django.urls import path
from qa import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    path('login/', views.login_view),
    path('signup/', views.signup),
    path('question/<int:id>/', views.question_details),
    path('ask/', views.ask),
    path('popular/', views.popular),
    path('new/', views.main),
]
