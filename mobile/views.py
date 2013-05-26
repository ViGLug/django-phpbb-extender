from django.views.generic import TemplateView
from django_phpbb_extender.models import PhpbbTopics, PhpbbPosts
from django_phpbb_extender.forum_settings import FORUM_NAME
from django_phpbb_extender.utils import phpbb_to_html

class Topics(TemplateView):
    template_name = "topics.html"
    
    def get_context_data(self, **kwargs):
        context = super(Mobile, self).get_context_data(**kwargs)
        context["title"] = FORUM_NAME
        topics = PhpbbTopics.objects.order_by('-topic_time')[:10]
        latest = []
        for topic in topics:
            post = PhpbbPosts.objects.get(post_id=topic.topic_first_post_id)
            latest.append((
                topic,
                phpbb_to_html(post.post_text),
            ))
        context["latest"] = latest
        return context