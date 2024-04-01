from .resources.compare.data import CompareData

def initialize_routes(api):
    api.add_resource(CompareData, '/compare-data')
