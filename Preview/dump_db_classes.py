import shelve
db = shelve.open('class-shelve')
for key in db:
    print(key, '=>\n ', db[key].name, db[key].pay, db[key])

bob = db['bob']
print(bob.lastName())
print(db['tom'].lastName())