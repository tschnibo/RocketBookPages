from setuptools import setup

setup(
    name='rocketqr',
    version='0.1',
    py_modules=['rocketqr', 'templates', 'constants','utils'],
    install_requires=[
        'Click','console-menu','Pillow','PyPDF2','qrcode','reportlab','six'
    ],
    entry_points='''
        [console_scripts]
        rocketqr=rocketqr:set_up
    ''',
)
