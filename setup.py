from setuptools import setup

setup(name='eve_couchdb',
      version='0.1',
      description='Eve CouchDB extension',
      url='http://github.com/timjacobi/eve-couchdb',
      author='Tim Jacobi',
      author_email='dev@tim-jacobi.com',
      license='MIT',
      packages=['eve_couchdb'],
      zip_safe=False,
      install_requires=['Eve', 'Flask-CouchDB']
)