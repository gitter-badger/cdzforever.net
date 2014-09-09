# -*- coding: utf-8 -*-

from fabric.api import local


def _foreman(cmd):
    local('foreman run %s' % cmd)


def runserver():
    _foreman('python manage.py runserver')
