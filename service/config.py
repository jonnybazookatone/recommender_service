RECOMMENDER_SECRET_KEY = 'this should be changed'
RECOMMENDER_MAX_HITS = 10000    
RECOMMENDER_MAX_INPUT = 500
RECOMMENDER_CHUNK_SIZE = 100
RECOMMENDER_MAX_NEIGHBORS = 40
RECOMMENDER_NUMBER_SUGGESTIONS = 10
RECOMMENDER_THRESHOLD_FREQUENCY = 1
RECOMMENDER_SOLR_PATH = 'http://0.0.0.0:9000/solr/select'
RECOMMENDER_CLUSTER_PROJECTION_PATH = 'utils/data/clusters'
SQLALCHEMY_BINDS = {}
# Define the autodiscovery endpoint
DISCOVERER_PUBLISH_ENDPOINT = '/resources'
# Advertise its own route within DISCOVERER_PUBLISH_ENDPOINT
DISCOVERER_SELF_PUBLISH = False