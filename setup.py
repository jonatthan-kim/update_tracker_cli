from setuptools import setup, find_packages

setup(
    name='UpdateTracker',
    version='0.0.1',
    author='Jinoh Kim',
    author_email='juju08217@daum.net',
    description='tracking update of python packages or library',
    packages=find_packages(),
    install_requires=[
        'Click',
        'requests'  # 이건 나중에 더 생각해보기
    ],
    entry_points={
        "console_scripts": [
            "track=update_tracker.cli:track"
        ]
    }
)