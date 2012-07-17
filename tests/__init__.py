
import os
import unittest

from flask import Flask

from flask_environments import Environments


class FlaskEnvironmentsTestCase(unittest.TestCase):

    DEFAULT_ENV = None
    VAR_NAME = None
    DATABASE_VALUE = 'development_db'

    def setUp(self):
        self.app = Flask(__name__)
        self.environments = Environments(self.app,
                                         var_name=self.VAR_NAME,
                                         default_env=self.DEFAULT_ENV)

    def test_from_object(self):
        self.environments.from_object('tests.config')
        self.assertEqual(self.app.config['DATABASE'], self.DATABASE_VALUE)

    def test_from_yaml(self):
        path = os.path.join(os.getcwd(), 'tests', 'config.yml')
        self.environments.from_yaml(path)
        self.assertEqual(self.app.config['DATABASE'], self.DATABASE_VALUE)


class StagingEnvironmentTestCase(FlaskEnvironmentsTestCase):

    DATABASE_VALUE = 'staging_db'

    def setUp(self):
        os.environ.setdefault('FLASK_ENV', 'STAGING')
        super(StagingEnvironmentTestCase, self).setUp()


class ProductionEnvironmentTestCase(FlaskEnvironmentsTestCase):

    VAR_NAME = 'FLASK_ENVIRONMENT'
    DATABASE_VALUE = 'production_db'

    def setUp(self):
        os.environ.setdefault('FLASK_ENVIRONMENT', 'PRODUCTION')
        super(ProductionEnvironmentTestCase, self).setUp()
