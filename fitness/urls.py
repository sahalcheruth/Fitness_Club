from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    # Redirect root to login

    
    path('', lambda request: redirect('login'), name='home_redirect'),

    # Yoga
    path('yoga/', views.class_list, name='class_list'),
    path('book/<int:class_id>/', views.book_class, name='book_class'),

    # Zumba
    path('zumba/', views.zumba_class_list, name='zumba_class_list'),
    path('zumba/book/<int:class_id>/', views.book_zumba_class, name='book_zumba_class'),

    # HIIT
    path('hiit/', views.hiit_class_list, name='hiit_class_list'),
    path('hiit/book/<int:class_id>/', views.book_hiit_class, name='book_hiit_class'),

    # Auth
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
