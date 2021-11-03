from setuptools import setup

from calendarcli import GUI
def readme():
    with open("README.md") as f:
        return str(f.read())


setup(
    name = 'calendar-cli-kku',
    version = '0.0.a6',
    packages = ['calendarcli'],
    description='test file',
    long_description=readme(),
    long_description_content_type='text/markdown',
    url = "https://github.com/VillSource/calendar-cli",
    install_requires=[
        'rich',
        'typer',
        'inquirer',
        'eel',
        'julian',
        'tzlocal',
        'monthdelta'
    ],
    entry_points = {
        'console_scripts': [
            'ccal = calendarcli.__mian__:main',
        ]
    })


if __name__ == '__main__':
    from configparser import ConfigParser
    config = ConfigParser()
    config.read('./calendarcli/data/setting.ini')
    config.set('calendar','ID','None')
    with open('./calendarcli/data/setting.ini', 'w') as f:
        config.write(f)