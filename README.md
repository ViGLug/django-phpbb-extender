Requirements
------------

Be sure to have installed python-devel, mysql (client) and mysql-devel

    easy_install -U distribute
    pip install MySQL-python
    pip install Django
    pip install djangorestframework
    pip install bbcode

Installation
------------

    git clone git://github.com/viglug/django-phpbb-extender.git

Configuration
-------------
    
    cd django_phpbb_extender # project settings directory
    cp settings.py.example settings.py
    vi settings.py # configure at least your database
    cd ..
    export DJANGO_PHPBB_EXTENDER_KEY="secret_key" # change it!
    python manage.py inspectdb > django_phpbb_extender/models.py

Run
---

    python manage.py runserver 0.0.0.0:8000
