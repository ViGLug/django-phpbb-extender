from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django_phpbb_extender.models import PhpbbPosts, PhpbbUsers
from django_phpbb_extender.utils import get_username, phpbb_to_html
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
        return phpbb_to_html(item.post_subject)
    
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