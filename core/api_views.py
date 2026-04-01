from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from .models import Student, Subject, Grade
from .serializers import StudentSerializer, SubjectSerializer, GradeSerializer 


class StudentListCreateAPIView(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
@api_view(['GET', 'POST'])
def subject_list_create(request):
    if request.method == 'GET':
        subjects = Subject.objects.all()
        serializer = SubjectSerializer(subjects, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = SubjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def subject_detail(request, pk):
    try:
        subject = Subject.objects.get(pk=pk)
    except Subject.DoesNotExist:
        return Response({'error': 'Subject not found'}, status=404)

    if request.method == 'GET':
        serializer = SubjectSerializer(subject)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SubjectSerializer(subject, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    elif request.method == 'DELETE':
        subject.delete()
        return Response({'message': 'Deleted successfully'}, status=204)
    
class GradeListCreateAPIView(generics.ListCreateAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer
    
    def get_queryset(self):
        queryset = Grade.objects.all()
        
        student_id = self.request.query_params.get('student_id')
        subject_id = self.request.query_params.get('subject_id')

        if student_id:
            queryset = queryset.filter(student__id=student_id)
        if subject_id:
            queryset = queryset.filter(subject__id=subject_id)

        return queryset
    
class GradeRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Grade.objects.all()
    serializer_class = GradeSerializer 


class RegisterAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print("Request Data:", request.data)
        print(request.content_type)
        print(request.data.keys())
        
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        if not username or not email or not password:
            return Response(
                {'error': 'username, email and password are required'},
                status=400
            )

        if User.objects.filter(username=username).exists():
            return Response(
                {'error': 'username already exists'},
                status=400
            )

        if User.objects.filter(email=email).exists():
            return Response(
                {'error': 'email already exists'},
                status=400
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        token = Token.objects.create(user=user)

        return Response(
            {
                'message': 'user registered successfully',
                'user': {
                    'username': user.username,
                    'email': user.email
                },
                'token': token.key
            },
            status=201
        )
        
class LoginAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        print(" Login request:", request.data)
        
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response(
                {'error': 'username and password are required'},
                status=400
            )

        user = authenticate(username=username, password=password)

        if user is None:
            return Response(
                {'error': 'invalid credentials'},
                status=401
            )

        token, created = Token.objects.get_or_create(user=user)

        return Response(
            {
                'message': 'login successful',
                'token': token.key
            },
            status=200
        )
    
