"""
Flask-Environments
------------------

Environment tools and configuration for Flask applications

Resources
`````````

- `Documentation <http://packages.python.org/Flask-Environments/>`_
- `Issue Tracker <http://github.com/mattupstate/flask-environments/issues>`_
- `Code <http://github.com/mattupstate/flask-environments/>`_
- `Development Version
  <http://github.com/mattupstate/flask-environments/zipball/develop#egg=Flask-RQ-dev>`_

"""
from setuptools import setup

setup(
    name='Flask-Environments',
    version='0.1',
    url='http://packages.python.org/flask-environments/',
    license='MIT',
    author='Matthew Wright',
    author_email='matt@nobien.net',
    description='Environment tools and configuration for Flask applications',
    long_description=__doc__,
    py_modules=['flask_environments'],
    zip_safe=False,
    platforms='any',
    install_requires=['Flask', 'pyyaml'],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
