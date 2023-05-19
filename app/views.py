from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User
from .models import *
from .serializers import *

# Create your views here.
@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        request = request.data
        username = request.get('username')
        password = request.get('password')
        if not username or not password:
            return Response({"message":"missing credentials"}, status=status.HTTP_403_FORBIDDEN) 
        try:
            user = User.objects.get(username=username)
        except:
            return Response({"message":"user does not exist"}, status=status.HTTP_403_FORBIDDEN)
        if not user.check_password(password):
            return Response({"message":"incorrect credentials"}, status=status.HTTP_403_FORBIDDEN)
        score = Score.objects.filter(user = user).first()
        if score:
            score = score.score
        else:
            score = 0
        return Response({"user": user.username, "score":score, "userId": user.id}, status=status.HTTP_200_OK)
    
@api_view(['POST'])
def score_increase(request):
    if request.method == 'POST':
        request = request.data
        username = request.get('username')
        data = request.get('data')
        if not username:
            return Response({"message":"missing credentials"}, status=status.HTTP_403_FORBIDDEN) 
        try:
            user = User.objects.get(username=username)
        except:
            return Response({"message":"user does not exist"}, status=status.HTTP_403_FORBIDDEN)
        
        score = Score.objects.filter(user=user).first()
        if not score:
            data["user"] = user.id
            serializer = ScoreSerializer(data=data)
        else:
            serializer = ScoreSerializer(score, data=data, partial = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"user": user.username, "score":data["score"], "userId": user.id}, status=status.HTTP_200_OK)