from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django_phpbb_extender.models import PhpbbPosts, PhpbbTopics
from django_phpbb_extender.utils import (
    get_username,
    get_forum,
    unquote,
    phpbb_to_html,
)
from django_phpbb_extender.forum_settings import (
    FORUM_PATH,
    FORUM_NAME,
    FORUM_DESC,
)

class PostsRSS(Feed):
    title = FORUM_NAME
    link = FORUM_PATH
    description = FORUM_DESC
    
    def items(self):
        return PhpbbPosts.objects.order_by('-post_time')[:20]
    
    def item_title(self, item):
        return unquote(item.post_subject)
    
    def item_description(self, item):
        user = get_username(item.poster_id)
        username = user.username
        text = phpbb_to_html(item.post_text)
        return "[<b>%s</b>] %s " % (username, text)
    
    def item_link(self, item):
        return FORUM_PATH+'viewtopic.php?p=%s#p%s' % (
            item.post_id, item.post_id)

class PostsAtom(PostsRSS):
    feed_type = Atom1Feed
    subtitle = PostsRSS.description

class TopicsRSS(Feed):
    title = FORUM_NAME
    link = FORUM_PATH
    description = FORUM_DESC
    
    def items(self):
        return PhpbbTopics.objects.order_by('-topic_time')[:10]
    
    def item_title(self, item):        
        forum = get_forum(item.forum_id)
        text = phpbb_to_html(item.topic_title)
        return "[%s] %s" % (forum.forum_name, text)
    
    def item_description(self, item):
        username = item.topic_first_poster_name
        post = PhpbbPosts.objects.get(post_id=item.topic_first_post_id)
        text = phpbb_to_html(post.post_text)
        return "[<b>%s</b>] %s " % (username, text)
    
    def item_link(self, item):
        return FORUM_PATH+'viewtopic.php?t=%s' % (item.topic_id)

class TopicsAtom(PostsRSS):
    feed_type = Atom1Feed
    subtitle = TopicsRSS.description