import os
import threading
import redis
import names
import uuid
import random

#If you add more server variables in the env-secret.yaml add them here too.
server = str(os.getenv("REDIS_HOST"))
pass1 = str(os.getenv("REDIS_PASS"))

r = redis.Redis(host=server, port=6379, db=0, password=pass1)



# print(rand_keyspace)
# session = cluster.connect()
# session.execute("CREATE KEYSPACE %s WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor' : 2 };" % (rand_keyspace))
# session.execute('use %s' % (rand_keyspace))
# session.execute('CREATE TABLE users(user_id UUID, name text, credits int, PRIMARY KEY (user_id));')


while True:
    for j in range(99999):
        rand_key=names.get_first_name()
        rand_val=str(random.randint(1,10000))
        r.set(rand_key, rand_val)
        r.get(rand_key)
