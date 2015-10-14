from setuptools import setup

setup(name='MapRequests',
      version='1.0',
      description='OpenShift App',
      author='Dakota Benjamin',
      author_email='dmb2@clevelandmetroparks.com',
      url='http://www.python.org/sigs/distutils-sig/',
      install_requires=[
          'Flask==0.10.1',
          'Flask-Bootstrap==3.3.5.6',
          'Flask-WTF==0.12',
          'Jinja2==2.8',
          'MarkupSafe==0.23',
          'WTForms==2.0.2',
          'Werkzeug==0.10.4',
          'argparse==1.2.1',
          'dominate==2.1.16',
          'itsdangerous==0.24',
          'wsgiref==0.1.2'
      ],
      )
