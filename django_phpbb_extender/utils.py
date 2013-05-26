from HTMLParser import HTMLParser
import re
import bbcode
from .models import PhpbbUsers, PhpbbForums
from .forum_settings import SMILIES_PATH

parser = bbcode.Parser(escape_html=False, replace_links=False)
clean = re.compile(r"(:[\w:]+)(?=])")

def unquote(quoted):
    return HTMLParser.unescape.__func__(HTMLParser, quoted)

def phpbb_to_html(text):
    coloured = text.replace('{SMILIES_PATH}', SMILIES_PATH)
    unquoted = unquote(coloured)
    cleaned = clean.sub('', unquoted)
    return parser.format(cleaned)

cache = {}

def get_cached(obj, uid):
    if type(obj) not in cache:
        cache[type(obj)] = {}
    if uid not in cache[type(obj)]:
        cache[type(obj)][uid] = obj
    return cache[type(obj)][uid]

def get_username(uid):
    obj = PhpbbUsers.objects.get(user_id=uid)
    return get_cached(obj, uid)

def get_forum(uid):
    obj = PhpbbForums.objects.get(forum_id=uid)
    return get_cached(obj, uid)

