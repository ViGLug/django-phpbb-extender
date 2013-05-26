from .models import PhpbbConfig

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