# ElasticSearch Install Script
>[참조](https://www.elastic.co/guide/en/elasticsearch/reference/7.15/deb.html)
```bash
# vi /etc/elasticsearch/elasticsearch.yml

network.host = 0.0.0.0
discovery.seed_hosts: ["127.0.0.1"]
```
