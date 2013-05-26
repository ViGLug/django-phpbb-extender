from HTMLParser import HTMLParser
import re
import bbcode

from .forum_settings import SMILIES_PATH
from .models import PhpbbUsers, PhpbbForums

parser = bbcode.Parser(escape_html=False, replace_links=False)
clean = re.compile(r"(:[\w:]+)(?=])")

def phpbb_to_html(text):
    coloured = text.replace('{SMILIES_PATH}', SMILIES_PATH)
    unquoted = HTMLParser.unescape.__func__(HTMLParser, coloured)
    cleaned = clean.sub('', unquoted)
    return parser.format(cleaned)

username_cache = {}

def get_username(uid):
    if uid not in username_cache:
        username = PhpbbUsers.objects.get(user_id=uid)
        username_cache[uid] = username
    return cache[uid]

forum_cache = {}

def get_forum(uid):
    if uid not in forum_cache:
        forum = PhpbbForums.objects.get(forum_id=uid)
        forum_cache[uid] = forum
    return forum_cache[uid]
