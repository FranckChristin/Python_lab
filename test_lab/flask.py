import redis

r = redis.StrictRedis(host= 'localhost', port = 6379, db=0) #utliser les commandes redis stricte

d = {'pere':'jean', 'mere':'pauline','soeurs':['aude','doudou']}

r.hmset('who', d)
print(r.hgetall('who'))