from django.views.generic import TemplateView
from django_phpbb_extender.models import PhpbbTopics, PhpbbPosts
from django_phpbb_extender.forum_settings import FORUM_NAME, FORUM_PATH
from django_phpbb_extender.utils import get_username, phpbb_to_html

class Posts(TemplateView):
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context = super(Posts, self).get_context_data(**kwargs)
        context["title"] = FORUM_NAME
        context["category"] = "posts"
        posts = PhpbbPosts.objects.order_by('-post_time')[:10]
        latest = []
        for post in posts:
            latest.append((
                get_username(post.poster_id).username,
                post.post_subject,
                phpbb_to_html(post.post_text),
                FORUM_PATH+"viewtopic.php?p=%s#p%s" % (
                        post.post_id, post.post_id),
            ))
        context["latest"] = latest
        return context

class Topics(TemplateView):
    template_name = "base.html"
    
    def get_context_data(self, **kwargs):
        context = super(Topics, self).get_context_data(**kwargs)
        context["title"] = FORUM_NAME
        context["category"] = "topics"
        topics = PhpbbTopics.objects.order_by('-topic_time')[:10]
        latest = []
        for topic in topics:
            post = PhpbbPosts.objects.get(post_id=topic.topic_first_post_id)
            latest.append((
                topic.topic_first_poster_name,
                topic.topic_title,
                phpbb_to_html(post.post_text),
                FORUM_PATH+"viewtopic.php?t=%s" % topic.topic_id,
            ))
        context["latest"] = latest
        return context