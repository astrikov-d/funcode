# coding: utf-8
import os
import site
import sys

from django.core.wsgi import get_wsgi_application

os.environ['PYTHON_EGG_CACHE'] = '/tmp/python-eggs/'
prev_sys_path = list(sys.path)
pwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(pwd + '/../../venv/')
sys.path = [pwd] + sys.path

for python_dir in os.listdir('lib'):
    site_packages_dir = os.path.join('lib', python_dir, 'site-packages')
    if os.path.exists(site_packages_dir):
        site.addsitedir(os.path.abspath(site_packages_dir))

new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../')
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../../conf')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "prod.settings")

application = get_wsgi_application()
