Flask-Environments
==================

.. module:: flask_environments

Flask-Environments provides environment tools and configuration for Flask applications

Resources
`````````

- `Documentation <http://packages.python.org/Flask-Environments/>`_
- `Issue Tracker <http://github.com/mattupstate/flask-environments/issues>`_
- `Code <http://github.com/mattupstate/flask-environments/>`_
- `Development Version
  <http://github.com/mattupstate/flask-environments/zipball/develop#egg=Flask-Environments-dev>`_


Contents
========
* :ref:`installation`
* :ref:`getting-started`


.. _installation:

Installation
============

    $ pip install flask-environments


.. _getting-started:

Getting Started
===============

The following code illustrates how to setup environment based configuration. The
first thing to do is create a configuration file. These can be created using Python
or Yaml. 

Python::

    from flask.ext.environments import BaseConfig as Config

    class Development(Config):
        DEBUG = True
        DATABASE = 'development_db'

    class Production(Config):
        DATABASE = 'production_db'

Yaml::

    COMMON: &common
      DEBUG: False
      TESTING: False

    DEVELOPMENT: &development
      <<: *common
      DEBUG: True
      DATABASE: 'development_db'

    PRODUCTION: &production
      <<: *common
      DATABASE: 'production_db'

Next, create your application and initialize the Environments extensions::

    from flask import Flask
    from flask.ext.environments import Environments

    app = Flask(__name__)
    env = Environments(app)

Then simply use the `from_object` method or the `from_yaml` method to load
the configuration::
    
    env.from_object('myapp.config')
    env.from_yaml(os.path.join(os.getcwd(), 'myapp', 'config.yml'))

Only the values for the specified environment will be applied.

Flask-Environments assumes an operating system environment variable named `FLASK_ENV`
will be set to one of your possible environments. If it is not set, it will default
to `DEVELOPMENT`. 

To change the default environment or the environment varibale name pass the `var_name`
or `default_env` parameters to the Environments constructor like so::

    from flask import Flask
    from flask.ext.environments import Environments

    app = Flask(__name__)
    env = Environments(app, var_name='CUSTOM_VAR_NAME', default_env='CUSTOM_ENV')
