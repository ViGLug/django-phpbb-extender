from rest_framework import serializers
from django_phpbb_extender.models import (
    PhpbbUsers,
    PhpbbForums,
    PhpbbTopics,
    PhpbbPosts,
)
from django_phpbb_extender.utils import phpbb_to_html

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
    post_text_html = serializers.SerializerMethodField('get_post_text_html')
    
    def get_post_text_html(self, obj):
        return phpbb_to_html(obj.post_text)
    
    class Meta:
        model = PhpbbPosts
        fields = (
            'post_id',
            'topic_id',
            'forum_id',
            'poster_id',
            'post_text_html',
        )
