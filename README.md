- [VectorDB Client](#vectordb-client)
  - [Using](#using)
  - [Developing](#developing)
  - [License](#license)
  - [Copyright](#copyright)

## VectorDB Client

A python library for multiple vector databases.

### Using

#### Pinecone

See [pinecone/hello.py](samples/pinecone/hello.py).

Sign up for Pinecone, get an `API_TOKEN` and a `PROJECT_ID`.

Run a working sample as follows.

```
API_TOKEN=... PROJECT_ID=... ENDPOINT=https://us-west4-gcp-free.pinecone.io poetry run samples/pinecone/hello.py
```

#### OpenSearch

Download and run OpenSearch.

```
docker pull opensearchproject/opensearch:latest
docker run -d -p 9200:9200 -p 9600:9600 -e "discovery.type=single-node" opensearchproject/opensearch:latest
```

Run a working sample as follows.

```
USERNAME=admin PASSWORD=admin ENDPOINT=https://localhost:9200 poetry run samples/open_search/hello.py
```


### Developing

See [DEVELOPER_GUIDE](DEVELOPER_GUIDE.md).

### License

This project is licensed under the [Apache v2.0 License](LICENSE.txt).

### Copyright

Copyright Daniel Doubrovkine, and contributors.
