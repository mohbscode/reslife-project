from django.urls import path
from . import views

urlpatterns = [
    # Auth
    path('register/', views.registerPage, name='register'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('', views.home, name='home'),
    path('work_orders/', views.workOrders, name='work_orders'),
    path('all_students/', views.allStudents, name='all_students'),
    path('student/<str:pk>/', views.student, name='student'),
    path('student_page/', views.studentPage, name='student-page'),
    path('accounts/', views.accountSettings, name="account"),
    path('maintenance/', views.maintenance, name='maintenance'),

    # CRUD
    path('create_order/', views.createOrder, name='create_order'),
    path('update_order/<str:pk>/', views.updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', views.deleteOrder, name='delete_order'),
]
