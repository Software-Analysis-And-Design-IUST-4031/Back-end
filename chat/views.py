from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.pagination import PageNumberPagination
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer

User = get_user_model()

class ChatPagination(PageNumberPagination):
    page_size = 10

class ChatListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        chats = Chat.objects.filter(participants=request.user)
        chat_data = []
        for chat in chats:
            chat_data.append({
                "id": chat.id,
                "participants": [user.get_username() for user in chat.participants.all()],
                "messages": MessageSerializer(chat.messages.all(), many=True).data
            })
        return Response(chat_data)

    def post(self, request):
        participants_data = request.data.get('participants')
        if not participants_data:
            return Response({"detail": "Participants are required."}, status=status.HTTP_400_BAD_REQUEST)

        participants = [request.user]
        for participant in participants_data:
            user = get_object_or_404(User, user_id=participant)
            participants.append(user)

        chat = Chat.objects.create()
        chat.participants.add(*participants)
        chat.save()

        serializer = ChatSerializer(chat)
        return Response({"message": "Chat created!", "chat": serializer.data}, status=status.HTTP_201_CREATED)
    
class ChatDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, pk):
        chat = get_object_or_404(Chat, pk=pk)
        if request.user not in chat.participants.all():
            return Response({"detail": "You are not a participant in this chat."}, status=status.HTTP_400_BAD_REQUEST)

        paginator = ChatPagination()
        messages = chat.messages.all()
        paginated_messages = paginator.paginate_queryset(messages, request)
        serializer = MessageSerializer(paginated_messages, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, pk):
        chat = get_object_or_404(Chat, pk=pk)
        if request.user not in chat.participants.all():
            return Response({"detail": "You are not a participant in this chat."}, status=status.HTTP_400_BAD_REQUEST)

        content = request.data.get('content')
        if not content:
            return Response({"detail": "Message content is required."}, status=status.HTTP_400_BAD_REQUEST)

        message = Message.objects.create(chat=chat, sender=request.user, content=content)
        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)

class MessageListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        chat_id = request.query_params.get('chat_id')
        if not chat_id:
            return Response({"detail": "Chat ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        chat = get_object_or_404(Chat, pk=chat_id)
        if request.user not in chat.participants.all():
            return Response({"detail": "You are not a participant in this chat."}, status=status.HTTP_400_BAD_REQUEST)

        paginator = ChatPagination()
        messages = chat.messages.all()
        paginated_messages = paginator.paginate_queryset(messages, request)
        serializer = MessageSerializer(paginated_messages, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request):
        chat_id = request.data.get('chat_id')
        if not chat_id:
            return Response({"detail": "Chat ID is required."}, status=status.HTTP_400_BAD_REQUEST)

        chat = get_object_or_404(Chat, pk=chat_id)
        if request.user not in chat.participants.all():
            return Response({"detail": "You are not a participant in this chat."}, status=status.HTTP_400_BAD_REQUEST)

        content = request.data.get('content')
        if not content:
            return Response({"detail": "Message content is required."}, status=status.HTTP_400_BAD_REQUEST)

        message = Message.objects.create(chat=chat, sender=request.user, content=content)
        return Response(MessageSerializer(message).data, status=status.HTTP_201_CREATED)

class MessageDetailView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, chat_id):
        chat = get_object_or_404(Chat, pk=chat_id)
        if request.user not in chat.participants.all():
            return Response({"detail": "You are not a participant in this chat."}, status=status.HTTP_400_BAD_REQUEST)

        messages = Message.objects.filter(chat_id=chat_id)
        serializer = MessageSerializer(messages, many=True)
        return Response(serializer.data)
