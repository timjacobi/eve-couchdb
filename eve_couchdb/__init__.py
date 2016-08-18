from eve.io.base import DataLayer
from flask.ext import couchdb

class CouchDBCollection():
    def __init__(self, view_results):
        self._rows = view_results
    def __iter__(self):
        for row in self._rows:
            yield row.value
    def count(self, with_limit_and_skip=False, **kwargs):
        return len(self._rows)

class CouchDB(DataLayer):
    def init_app(self, app):
        driver = couchdb.CouchDBManager()
        self.driver = driver

        people_all_view = couchdb.ViewDefinition('people', 'all', '''\
            function(doc){ if(doc.docType === "people"){ emit(null, doc) } }
        ''')

        self.views = {
            'people_all': people_all_view
        }

        driver.add_viewdef(people_all_view)

        driver.setup(app)

    def find_one(self, resource, req, **lookup):
        print(resource)
        return True
    
    def find(self, resource, req, sub_resource_lookup):
        results = self.views[resource+"_all"]()
        return CouchDBCollection(results)