from elasticsearch import Elasticsearch
from elasticsearch.helpers import bulk
import config
from elasticsearch.exceptions import ElasticsearchException
from tweet_utils import get_tweet, id_field, tweet_mapping


idx_name = 'twitter'
doc_type = 'tweet'
mapping = {doc_type: tweet_mapping}
bulk_chunk_size = config.es_bulk_chunk_size


def create_index(es,idx_name,mapping):
    es.indices.create(idx_name, body = {'mappings': mapping})


def load(tweets):    
    es = Elasticsearch(host = config.es_host, port = config.es_port)

    if es.indices.exists(idx_name):
        print ('index {} already exists'.format(idx_name))
        try:
            es.indices.put_mapping(doc_type, tweet_mapping, idx_name)
        except ElasticsearchException as e:
            print('error adding mapping:\n'+str(e))
            es.indices.delete(idx_name)
            create_index(es, idx_name, mapping)
    else:
        print('index {} does not exist'.format(idx_name))
        create_index(es, idx_name, mapping)
    
    k = 0
    data = []
    tweets_len = len(tweets)
    for doc in tweets:
        tweet = get_tweet(doc)
        bulk_doc = {
            "_index": idx_name,
            "_type": doc_type,
            "_id": tweet[id_field],
            "_source": tweet
            }
        data.append(bulk_doc)
        k+=1
        
        if k % bulk_chunk_size == 0 or k == tweets_len:
            print "ElasticSearch bulk index (index: {INDEX}, type: {TYPE})...".format(INDEX=index_name, TYPE=doc_type)
            success, _ = bulk(es, data)
            print 'ElasticSearch indexed %d documents' % success
            data = []
