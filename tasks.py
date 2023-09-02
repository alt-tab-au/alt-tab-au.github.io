# -*- coding: utf-8 -*-

from invoke import task
from invoke.main import program

from pelican.settings import DEFAULT_CONFIG, get_settings_from_file

OPEN_BROWSER_ON_SERVE = False

SETTINGS = {
    '_dev_config_path': 'pelicanconf.py',
    '_publish_config_path': 'publishconf.py',

    # Github Pages configuration
    '_git_remote': 'origin',
    '_git_branch': 'gh-pages',
    '_git_commit': "'Publish site'",

    '_open_browser': False
}
SETTINGS.update(DEFAULT_CONFIG)
LOCAL_CONFIG = get_settings_from_file(SETTINGS['_dev_config_path'])
SETTINGS.update(LOCAL_CONFIG)


@task
def livereload(c):
    """Automatically reload browser tab upon file modification."""
    from livereload import Server

    def cached_build():
        cmd = '-s {_dev_config_path} -e CACHE_CONTENT=true LOAD_CONTENT_CACHE=true'
        pelican_run(cmd.format(**SETTINGS))

    cached_build()
    server = Server()
    theme_path = SETTINGS['THEME']
    server.watch(SETTINGS['_dev_config_path'], cached_build)
    server.watch(f'{theme_path}/templates/**/*.html', cached_build)
    
    # content files
    for extension in ['.md', '.rst']:
        content_glob = f'{SETTINGS["PATH"]}/**/*{extension}'
        server.watch(content_glob, cached_build)

    # static files
    for extension in ['.css', '.js']:
        static_glob = f'{theme_path}/static/**/*{extension}'
        server.watch(static_glob, cached_build)

    if SETTINGS['_open_browser']:
        # Open site in default browser
        import webbrowser
        webbrowser.open("http://{BIND}:{PORT}".format(**SETTINGS))

    server.serve(host=SETTINGS['BIND'], port=SETTINGS['PORT'], root=SETTINGS['OUTPUT_PATH'])


@task
def publish(c):
    """Publish site to GitHub Pages."""
    preview(c)
    c.run('ghp-import -o -p -f'
          '-r {_git_remote} '
          '-b {_git_branch} '
          '-m {_git_commit} '
        '{OUTPUT_PATH}'.format(**SETTINGS))


def pelican_run(cmd):
    import shlex
    from pelican import main as pelican_main
    cmd += ' ' + program.core.remainder  # allows to pass-through args to pelican
    pelican_main(shlex.split(cmd))

@task
def preview(c):
    """(re)build production copy of site"""
    pelican_run('-d -s {_publish_config_path}'.format(**SETTINGS))

@task
def clean(c):
    """Clear all generated files"""
    import os, shutil
    if os.path.isdir(SETTINGS['OUTPUT_PATH']):
        shutil.rmtree(SETTINGS['OUTPUT_PATH'])
        os.makedirs(SETTINGS['OUTPUT_PATH'])

@task
def build(c):
    """(re)build local version of site"""
    pelican_run('-d -s {_dev_config_path}'.format(**SETTINGS))

@task
def servepreview(c):
    """Serve preview copy of site at http://$HOST:$PORT/"""
    import sys
    from pelican.server import ComplexHTTPRequestHandler, RootedHTTPServer

    preview(c)
    class AddressReuseTCPServer(RootedHTTPServer):
        allow_reuse_address = True

    server = AddressReuseTCPServer(
        SETTINGS['OUTPUT_PATH'],
        (SETTINGS['BIND'], SETTINGS['PORT']),
        ComplexHTTPRequestHandler)

    if SETTINGS['_open_browser']:
        # Open site in default browser
        import webbrowser
        webbrowser.open("http://{BIND}:{PORT}".format(**SETTINGS))

    sys.stderr.write('Serving at {BIND}:{PORT} ...\n'.format(**SETTINGS))
    server.serve_forever()
