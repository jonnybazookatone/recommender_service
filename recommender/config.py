SECRET_KEY = 'this should be changed'
MAX_HITS = 10000    
MAX_INPUT = 500
CHUNK_SIZE = 100
MAX_NEIGHBORS = 40
NUMBER_SUGGESTIONS = 10
SQLALCHEMY_METRICS_DATABASE_URI = ''
SQLALCHEMY_RECOMMENDER_DATABASE_URI = ''
THRESHOLD_FREQUENCY = 1
SOLRQUERY_URL = 'http://adswhy:9000/solr/collection1/select'
CLUSTER_PROJECTION_PATH = 'utils/data/clusters'
#This section configures this application to act as a client, for example to query solr via adsws
CLIENT = {
  'TOKEN': 'we will provide an api key token for this application'
}
