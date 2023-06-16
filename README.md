- [VectorDB Client](#vectordb-client)
  - [Using](#using)
  - [Developing](#developing)
  - [License](#license)
  - [Copyright](#copyright)

## VectorDB Client

A python library for multiple vector databases.

### Using

#### Pinecone

```python
db = PineconeDatabase(connection = http)
auth = ApiToken(token=...)
db.connect(auth)

if not 'my-index' in db.indices:
    index = db.create_index('my-index', { 'dimension': 1024 })
    print(f'\nIndex: {index}')

print(f'\nIndices: {len(db.indices)}')
for idx in db.indices:
    print(f'idx={idx}')
```

#### OpenSearch



### Developing

See [DEVELOPER_GUIDE](DEVELOPER_GUIDE.md).

### License

This project is licensed under the [Apache v2.0 License](LICENSE.txt).

### Copyright

Copyright Daniel Doubrovkine, and contributors.
