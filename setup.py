from setuptools import setup
from setuptools.command.install import install
import subprocess

class PostInstallCommand(install):
    def run(self):
        install.run(self)
        try:
            subprocess.check_call(['ollama', 'pull', 'llama3'])
        except subprocess.CalledProcessError as e:
            print(f"Error on fetch ollama model: {e}")
            exit(0)

setup(
    name='bash_wizard',
    version='0.0.1',
    packages=['bash_wizard'],
    cmdclass={
        'install': PostInstallCommand,
    },
)
