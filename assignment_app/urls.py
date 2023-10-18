from django.urls import path
from . import views

urlpatterns = [
    path('show/<str:name>/<int:is_teacher>/', views.show_associated_data, name='show_data'),
    path('student_list/', views.student_list, name='student_list'),
     path('teacher_students/<int:teacher_id>/', views.teacher_students, name='teacher_students'),
    path('student_teachers/<int:student_id>/', views.student_teachers, name='student_teachers'),
path('generate_certificate/<int:teacher_id>/<int:student_id>/', views.generate_certificate, name='generate_certificate'),
 path('api/verify-certificate/', views.verify_certificate, name='verify_certificate'),
 path('api/token/', views.ObtainJSONWebToken.as_view(), name='token_obtain_pair')
]