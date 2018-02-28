# Save in-memory database object to a file with custom formatting
dbfilename = 'people-file'

# assume 'endrec.', 'enddb.' and '=>' are not used in the data
ENDDB = 'enddb.'
ENDREC = 'endrec.'
RECSEP = '=>'

def storeDbase(db, dbfilename = dbfilename):
    "formatted dump of database to flat file"
    dbfile = open(dbfilename, 'w')
    for key in db:
        print (key, file=dbfile)
        for (name, value) in db[key].items():
            print(name + RECSEP + repr(value), file = dbfile)
        print (ENDREC, file = dbfile)
    print (ENDDB, file = dbfile)
    dbfile.close()



if __name__ == '__main__':
    from initdata import db
    storeDbase(db)