from HTMLParser import HTMLParser
import re
import bbcode
from django.contrib.syndication.views import Feed
from api.models import PhpbbConfig, PhpbbPosts, PhpbbUsers

def get_config(value):
    return PhpbbConfig.objects.get(config_name=value).config_value

FORUM_PATH = "%s%s:%s/" % (
    get_config('server_protocol'),
    get_config('server_name'),
    get_config('server_port')
)
FORUM_NAME = get_config('sitename')
FORUM_DESC = get_config('site_desc')
SMILIES_PATH = FORUM_PATH+get_config('smilies_path')

parser = bbcode.Parser(escape_html=False, replace_links=False)
clean = re.compile(r"(:[\w:]+)(?=])")

def phpbb_to_html(text):
    decoded = text.decode('utf-8')
    coloured = decoded.replace('{SMILIES_PATH}', SMILIES_PATH)
    unquoted = HTMLParser.unescape.__func__(HTMLParser, coloured)
    cleaned = clean.sub('', unquoted)
    return parser.format(cleaned)

cache = {}
def get_username(uid):
    if uid not in cache:
        cache[uid] = PhpbbUsers.objects.get(user_id=uid)
    return cache[uid]

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
        return FORUM_PATH+'viewtopic.php?p=%s#p%s' % (item.post_id, item.post_id)