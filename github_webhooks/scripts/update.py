#!/usr/bin/env python
import os
import subprocess

def chown():
    chown = subprocess.Popen(['chown', '-R', 'www-data:www-data', 'message_board/'],
                        cwd='/sites/projects/',
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = chown.communicate()
    return out, err

def pull():
    pull = subprocess.Popen(['git', 'pull'],
                        cwd='/sites/projects/message_board/',
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = pull.communicate()
    return out, err

def collect():
    collect = subprocess.Popen(['/sites/virtualenvs/message_board/bin/python', './manage.py', 'collectstatic', '--noinput'],
                        cwd='/sites/projects/message_board/',
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = collect.communicate()
    return out, err

def restart():
    restart = subprocess.Popen(['service', 'apache2', 'restart'],
                        stdout=subprocess.PIPE, 
                        stderr=subprocess.PIPE)

    out, err = restart.communicate()
    return out, err
