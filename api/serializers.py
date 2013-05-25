from rest_framework import serializers
from .models import (
    PhpbbUsers,
    PhpbbForums,
    PhpbbTopics,
    PhpbbPosts,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhpbbUsers
        fields = (
            'user_id',
            'username',
            'user_avatar',
        )

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhpbbForums
        fields = (
            'forum_id',
            'forum_name',
            'forum_desc',
            'forum_last_post_id',
        )

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhpbbTopics
        fields = (
            'topic_id',
            'forum_id',
            'topic_title',
        )

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhpbbPosts
        fields = (
            'post_id',
            'topic_id',
            'forum_id',
            'poster_id',
            'post_text',
        )
