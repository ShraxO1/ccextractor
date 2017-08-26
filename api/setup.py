from distutils.core import setup,Extension
from setuptools.command.develop import develop
from setuptools.command.install import install
import subprocess
import os
import shutil

class PostDevelopCommand(develop):
    """Post-installation for development mode."""
    def run(self):
        path = os.path.join(os.getcwd(),"package_build_scripts")
        files = [os.path.join(path , item) for item in os.listdir(path)]
        for f in files:
            shutil.move(f,os.getcwd())

        subprocess.check_call(['./build_library_package'])
        develop.run(self)

class PostInstallCommand(install):
    """Post-installation for installation mode."""
    def run(self):
        path = os.path.join(os.getcwd(),"package_build_scripts")
        files = [os.path.join(path , item) for item in os.listdir(path)]
        for f in files:
            shutil.move(f,os.getcwd())

        subprocess.check_call(['./build_library_package'])
        install.run(self)

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
