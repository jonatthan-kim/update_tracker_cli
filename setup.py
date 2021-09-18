# python setup.py bdist_wheel 
# twine upload dist/update_tracker-

from setuptools import setup, find_packages
from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='update_tracker',
    version='0.0.3',
    description='tracking update of python packages or library',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jinoh Kim',
    author_email='juju08217@daum.net',
    url='https://github.com/Independent-Dev',
    license='MIT',
    py_modules=['update_tracker'],
    python_requires=">=3.6",
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests',
        "python-dateutil"
    ],
    entry_points={
        "console_scripts": [
            "track=update_tracker.cli:track"
        ]
    }
)