#from django.contrib.auth.models import User, Group
from rest_framework import generics
from .serializers import (
    UserSerializer,
    ForumSerializer,
    TopicSerializer,
    PostSerializer,
)

class UsersReadView(generics.ListAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.exclude(user_type=2) # exclude bot
    paginate_by = 100

class UserReadView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    model = serializer_class.Meta.model
    lookup_field = 'user_id'

class UserPostsReadView(generics.ListAPIView):
    serializer_class = PostSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('post_time').reverse()
    lookup_field = 'poster_id'
    paginate_by = 100

class ForumsReadView(generics.ListAPIView):
    serializer_class = ForumSerializer
    model = serializer_class.Meta.model

class ForumReadView(generics.RetrieveAPIView):
    serializer_class = ForumSerializer
    model = serializer_class.Meta.model
    lookup_field = 'forum_id'

class TopicsReadView(generics.ListAPIView):
    serializer_class = TopicSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('topic_time').reverse()
    paginate_by = 100

class TopicReadView(generics.RetrieveAPIView):
    serializer_class = TopicSerializer
    model = serializer_class.Meta.model
    lookup_field = 'topic_id'

class TopicPostsReadView(generics.ListAPIView):
    serializer_class = PostSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('post_time').reverse()
    lookup_field = 'topic_id'
    paginate_by = 100

class PostsReadView(generics.ListAPIView):
    serializer_class = PostSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('post_time').reverse()
    paginate_by = 100

class PostReadView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    model = serializer_class.Meta.model
    lookup_field = 'post_id'
