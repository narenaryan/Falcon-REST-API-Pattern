import os
import rethinkdb as r
from rethinkdb.errors import RqlRuntimeError, RqlDriverError


RDB_HOST = os.environ.get('RDB_HOST') or 'localhost'
RDB_PORT = os.environ.get('RDB_PORT') or 28015

PROJECT_DB = 'todo'
PROJECT_TABLE = 'notes'

db_connection = r.connect(RDB_HOST,RDB_PORT)


#This is just for cross-checking database and table exists 
def dbSetup():
    print PROJECT_DB,db_connection
    try:
        r.db_create(PROJECT_DB).run(db_connection)
        print 'Database setup completed.'
    except RqlRuntimeError:
        try:
            r.db(PROJECT_DB).table_create(PROJECT_TABLE).run(db_connection)
            print 'Table creation completed'
        except:
            print 'Table already exists.Nothing to do'

dbSetup()
 