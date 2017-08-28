from distutils.core import setup,Extension
from setuptools.command.develop import develop
from setuptools.command.install import install
from distutils.sysconfig import get_python_lib
import subprocess
import os
import sys
import shutil

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        install.run(self)

if not sys.argv[-1]=='sdist':
    path = os.path.join(os.getcwd(),"package_build_scripts")
    files = [os.path.join(path , item) for item in os.listdir(path)]
    for f in files:
        shutil.move(f,os.getcwd())
    subprocess.check_call(['./build_library_package'])
    files = [item for item in os.listdir(os.getcwd()) if item=='ccextractor.py' or item =='_ccextractor.so']
    setup(
       name='ccextractor',
       version = '0.1',
       author      = "Skrill",
       description = "Testing setup script for generating the module",
       packages = ['ccextractor'],
       #package_dir = {'ccextractor':''},
       package_dir = {'ccextractor':''},
        
       package_data = {'ccextractor':['_ccextractor.so','ccextractor.py']},
    include_package_data=True,
       cmdclass={
           'develop': PostDevelopCommand,
           'install':PostInstallCommand,
           },
    )
else:
    setup(
       name='ccextractor',
       version = '0.1',
       author      = "Skrill",
       description = "Testing setup script for generating the module",
       cmdclass={
           'develop': PostDevelopCommand,
           'install':PostInstallCommand,
           },
    )
