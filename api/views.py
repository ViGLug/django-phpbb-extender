#from django.contrib.auth.models import User, Group
from rest_framework import filters, generics
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
    paginate_by = 100
    def get_queryset(self):
        poster_id = self.kwargs['poster_id']
        queryset = self.model.objects.filter(poster_id=poster_id)
        return queryset.order_by('-post_time')

class ForumsReadView(generics.ListAPIView):
    serializer_class = ForumSerializer
    model = serializer_class.Meta.model
    filter_backends = (filters.OrderingFilter,)
    ordering = ('left_id',)

class ForumReadView(generics.RetrieveAPIView):
    serializer_class = ForumSerializer
    model = serializer_class.Meta.model
    lookup_field = 'forum_id'

class ForumTopicsReadView(generics.ListAPIView):
    serializer_class = TopicSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    def get_queryset(self):
        forum_id = self.kwargs['forum_id']
        queryset = self.model.objects.filter(forum_id=forum_id)
        return queryset.order_by('-topic_last_post_time')

class TopicsReadView(generics.ListAPIView):
    serializer_class = TopicSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('-topic_time')
    paginate_by = 100

class TopicReadView(generics.RetrieveAPIView):
    serializer_class = TopicSerializer
    model = serializer_class.Meta.model
    lookup_field = 'topic_id'

class TopicPostsReadView(generics.ListAPIView):
    serializer_class = PostSerializer
    model = serializer_class.Meta.model
    paginate_by = 100
    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        queryset = self.model.objects.filter(topic_id=topic_id)
        return queryset.order_by('-post_time')

class PostsReadView(generics.ListAPIView):
    serializer_class = PostSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.order_by('-post_time')
    paginate_by = 100

class PostReadView(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    model = serializer_class.Meta.model
    lookup_field = 'post_id'
