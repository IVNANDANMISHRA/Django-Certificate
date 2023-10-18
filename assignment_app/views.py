from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from rest_framework_jwt.utils import jwt_payload_handler

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
from .models import Teacher, Student,Certificate

def show_associated_data(request, id, is_teacher):
    if is_teacher:
        teacher = Teacher.objects.get(pk=id)
        students = teacher.students.all()
        return render(request, 'assignment_app/students.html', {'students': students, 'is_teacher': is_teacher})
    else:
        student = Student.objects.get(pk=id)
        teachers = student.teachers.all()
        return render(request, 'assignment_app/teachers.html', {'teachers': teachers, 'is_teacher': is_teacher})
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

# assignment_app/views.py



def teacher_students(request, teacher_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    students = teacher.students.all()
    return render(request, 'teacher_students.html', {'teacher': teacher, 'students': students})

def student_teachers(request, student_id):
    student = Student.objects.get(pk=student_id)
    teachers = student.teachers.all()
    return render(request, 'student_teachers.html', {'student': student, 'teachers': teachers})


def generate_certificate(request, teacher_id, student_id):
    teacher = Teacher.objects.get(pk=teacher_id)
    student = Student.objects.get(pk=student_id)

    certificate, created = Certificate.objects.get_or_create(teacher=teacher, student=student)
    if created:
        certificate.generate_certificate()
        certificate.save()

    return render(request, 'certificate.html', {'certificate': certificate})

class ObtainJSONWebToken(APIView):
    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)  # Authenticate the user
            if user:
                payload = jwt_payload_handler(user)
                token = jwt_encode_handler(payload)
                return Response({'token': token})
            else:
                return Response({'detail': 'Invalid credentials.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'Both username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def verify_certificate(request):
    data = request.data
    teacher_id = data.get('teacher_id')
    student_id = data.get('student_id')
    
    try:
        certificate = Certificate.objects.get(teacher_id=teacher_id, student_id=student_id)
        return Response({'valid': True, 'certificate_text': certificate.certificate_text}, status=status.HTTP_200_OK)
    except Certificate.DoesNotExist:
        return Response({'valid': False}, status=status.HTTP_404_NOT_FOUND)