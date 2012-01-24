variables = (
    ('author_name', '', "Author's name"),
    ('author_email', '', "Author's email"),
    ('app_id', 'myappid', 'The AppEngine application id.'),
)

post_commands = (
    'wget http://bitbucket.org/wkornewald/django-nonrel/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-django-nonrel-*/django .',
    'rm -rf wkornewald-django-nonrel-*',

    'wget http://bitbucket.org/wkornewald/djangoappengine/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-djangoappengine-* djangoappengine',
    'rm -rf wkornewald-djangoappengine-*',

    'wget http://bitbucket.org/wkornewald/djangotoolbox/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-djangotoolbox-*/djangotoolbox .',
    'rm -rf wkornewald-djangotoolbox-*',

    'wget http://bitbucket.org/twanschik/django-autoload/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv twanschik-django-autoload-*/autoload .',
    'rm -rf twanschik-django-autoload-*',

    'wget http://bitbucket.org/wkornewald/django-dbindexer/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-django-dbindexer-*/dbindexer .',
    'rm -rf wkornewald-django-dbindexer-*',

    'wget http://bitbucket.org/wkornewald/django-mediagenerator/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv wkornewald-django-mediagenerator-*/mediagenerator .',
    'rm -rf wkornewald-django-mediagenerator-*',

    'wget http://bitbucket.org/offline/django-annoying/get/tip.zip',
    'unzip -q tip.zip',
    'rm tip.zip',
    'mv offline-django-annoying-*/annoying .',
    'rm -rf offline-django-annoying-*',
)
