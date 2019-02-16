import rocksdb

options = rocksdb.Options()
options.create_if_missing = True

db = rocksdb.DB("rocksdb_column_families_example.db", options)

cf = db.create_column_family(b"new_cf", rocksdb.ColumnFamilyOptions())

del db

column_families = {}

# kDefaultColumnFamilyName == 'default'
column_families[b"default"] = rocksdb.ColumnFamilyOptions()
column_families[b"new_cf"] = rocksdb.ColumnFamilyOptions()

db = rocksdb.DB("rocksdb_column_families_example.db", options, column_families = column_families)

# e.g) db.column_families
# [<ColumnFamilyHandle name: b'default', id: 0, state: valid>, <ColumnFamilyHandle name: b'cf', id: 1, state: valid>]

default_column_family = db.get_column_family(b'default')
new_cf_column_family = db.get_column_family(b'new_cf')

db.put( (new_cf_column_family, b'key'), b'value' )
print( db.get( (new_cf_column_family, b'key') ) ) # b'value'

batch = rocksdb.WriteBatch()

batch.put( (default_column_family, b'key2'), b'value2' )
batch.put( (new_cf_column_family, b'key3'), b'value3' )
batch.delete( (default_column_family, b'key') ) 

db.write(batch)

db.drop_column_family(new_cf_column_family)

# e.g) db.column_families
# [<ColumnFamilyHandle name: b'default', id: 0, state: valid>]
