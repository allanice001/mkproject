variables = (
    ('author_name', '', "Author's name"),
    ('author_email', '', "Author's email"),
    ('app_id', 'myappid', 'The AppEngine application id.'),
)

post_commands = (
    'wget http://bitbucket.org/wkornewald/django-nonrel/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-django-nonrel-tip/django .',
    'rm -rf wkornewald-django-nonrel-tip',

    'wget http://bitbucket.org/wkornewald/djangoappengine/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-djangoappengine-tip djangoappengine',
    'rm -rf wkornewald-djangoappengine-tip',

    'wget http://bitbucket.org/wkornewald/djangotoolbox/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-djangotoolbox-tip/djangotoolbox .',
    'rm -rf wkornewald-djangotoolbox-tip',

    'wget http://bitbucket.org/twanschik/django-autoload/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv twanschik-django-autoload-tip/autoload .',
    'rm -rf twanschik-django-autoload-tip',

    'wget http://bitbucket.org/wkornewald/django-dbindexer/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-django-dbindexer-tip/dbindexer .',
    'rm -rf wkornewald-django-dbindexer-tip',

    'wget http://bitbucket.org/wkornewald/django-mediagenerator/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-django-mediagenerator-tip/mediagenerator .',
    'rm -rf wkornewald-django-mediagenerator-tip',

    'wget http://bitbucket.org/offline/django-annoying/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv offline-django-annoying-tip/annoying .',
    'rm -rf offline-django-annoying-tip',
)
