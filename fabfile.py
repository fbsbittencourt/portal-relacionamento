#-*- coding: utf-8 -*-

import os
from fabric.api import *


# Global definitions
# ==================

# Project
env.project = 'mr2digital'
env.user_home = 'mr2digital'


def _path():
    # Project path
    env.project_path = os.path.join(env.root, 'apps_wsgi', env.project)

    # Manage file
    env.manage_file = os.path.join(env.project_path, 'manage.py')

    # Virtualenv paths
    env.virtualenv_root = os.path.join(env.root, '.virtualenvs', '%s_env' % env.project)
    env.virtualenv_active = os.path.join(env.virtualenv_root, 'bin', 'activate')

    # Requirements path
    env.requirements = os.path.join(env.project_path, 'requirements.txt')


def production():
    '''
    Settings for production enviroment
    '''

    # Enviroment
    env.environment = 'production'

    # Remote settings
    env.hosts = ['']
    env.user = 'mr2digital'
    env.password = ''

    # Paths
    env.root = '/home/mr2digital'
    _path()


def update_requirements():
    '''
    Update Python dependencies on remote host
    '''

    require('virtualenv_active', provided_by=('production'))

    command = (
        'source %(virtualenv_active)s; '
        'pip install -r %(requirements)s; '
        'deactivate;'
    )

    run(
        command % {
            'virtualenv_active': env.virtualenv_active,
            'requirements': env.requirements
        }
    )


def deploy():
    '''
    Send code to the remote host.
    '''

    require('project_path', provided_by=('production'))

    with cd(env.project_path):

        # atualiza o repositório
        run('git pull origin master')

    with cd(env.root):
        # touch wsgi file
        run('touch %s/apps_wsgi/%s.wsgi' % (env.root, env.project))


def syncdb():
    '''
    Execute syncdb on remote host, for the first deploy
    '''

    require('manage_file', provided_by=('production'))
    require('virtualenv_active', provided_by=('production'))

    command = (
        'source %(virtualenv_active)s; '
        'python %(manage_file)s syncdb;'
    ) % {
        'virtualenv_active': env.virtualenv_active,
        'manage_file': env.manage_file,
        'environment': env.environment
    }

    run(command)
