from django.urls import path
from .views import ChatListCreateView, ChatDetailView, MessageListCreateView, MessageDetailView

urlpatterns = [
    path('chats/', ChatListCreateView.as_view(), name='chat-list-create'),
    path('chats/<int:pk>/', ChatDetailView.as_view(), name='chat-detail'),
    path('messages/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:chat_id>/', MessageDetailView.as_view(), name='message-detail'),
]
