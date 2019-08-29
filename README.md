# RocksDB examples

- column_families_example.py
  - The conversion of `rocksdb/examples/column_families_example.cc` to the python-rocksdb version

## Environment setup

- Python 3.6.8
- [Python RocksDB 0.7.0](https://github.com/twmht/python-rocksdb)
- [RocksDB 5.18](https://github.com/facebook/rocksdb/)

The RocksDB and python binding could be installed via the following quick installation script:
```
apt-get install python-virtualenv python-dev librocksdb-dev
virtualenv venv
source venv/bin/activate
pip install python-rocksdb
```