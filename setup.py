from setuptools import setup, find_packages

setup(
    name='update_tracker',
    version='0.0.1',
    description='tracking update of python packages or library',
    author='Jinoh Kim',
    author_email='juju08217@daum.net',
    url='https://github.com/Independent-Dev',
    license='MIT',
    py_modules=['update_tracker'],
    python_requires=">=3.6",
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests'
    ],
    entry_points={
        "console_scripts": [
            "track=update_tracker.cli:track"
        ]
    }
)