from HTMLParser import HTMLParser
import re
import bbcode

from .forum_settings import SMILIES_PATH
from .models import PhpbbUsers

parser = bbcode.Parser(escape_html=False, replace_links=False)
clean = re.compile(r"(:[\w:]+)(?=])")

def phpbb_to_html(text):
    coloured = text.replace('{SMILIES_PATH}', SMILIES_PATH)
    unquoted = HTMLParser.unescape.__func__(HTMLParser, coloured)
    cleaned = clean.sub('', unquoted)
    return parser.format(cleaned)

cache = {}

def get_username(uid):
    if uid not in cache:
        cache[uid] = PhpbbUsers.objects.get(user_id=uid)
    return cache[uid]
