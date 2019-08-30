import rocksdb
from pprint import pprint


def main():
    # example 1
    options = rocksdb.Options()
    options.create_if_missing = True

    db = rocksdb.DB('column_families_example.db', options, column_families={}, read_only=False)
    cf_handle = db.create_column_family(b'new_cf', rocksdb.ColumnFamilyOptions())
    cf_handle = db.create_column_family(b'test_cf', rocksdb.ColumnFamilyOptions())
    del db

    # example 2
    column_families = {
        b'default': rocksdb.ColumnFamilyOptions(),  # default CF is already exists, so this is redundant
        b'new_cf': rocksdb.ColumnFamilyOptions(),
        b'test_cf': rocksdb.ColumnFamilyOptions(),
    }
    db = rocksdb.DB("column_families_example.db", options, column_families=column_families)
    print(f'after create column family:')
    pprint(db.column_families)

    default_cf = db.get_column_family(b'default')
    new_cf = db.get_column_family(b'new_cf')
    test_cf = db.get_column_family(b'test_cf')

    db.put((new_cf, b'key'), b'value')
    v = db.get((new_cf, b'key'), b'key')
    print(f'\n(new_cf, key): {v}')

    print('\nbatch write demo:')
    batch = rocksdb.WriteBatch()

    batch.put((default_cf, b'key2'), b'value2')
    batch.put((default_cf, b'default_2'), b'test')
    batch.put((new_cf, b'key3'), b'value3')
    batch.delete((default_cf, b'key'))
    db.write(batch)

    # IMPORTANT: I don't know what is the reason,
    # but if you make an iterator of a column family, and then drop this column family
    # you will get "signal 11: SIGSEGV" or "malloc_consolidate(): invalid chunk size (signal 6: SIGABRT)"
    # it = db.iteritems(test_cf)  # also iterkeys(), itervalues()
    # it.seek_to_first()  # need to seek to make iterator valid
    # print(list(it))

    # drop CF, only default CF remains
    db.drop_column_family(new_cf)
    db.drop_column_family(test_cf)
    pprint(db.column_families)


if __name__ == '__main__':
    main()
