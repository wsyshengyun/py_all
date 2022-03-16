from asyncio import queues
from queue import Queue
from threading import Thread
import subprocess 
from queue import Queue

num_threads = 10 
q = Queue()
def pingme(i, queue):
    while True:
        ip = queue.get() 
        ret = subprocess.call('ping -c 1 %s' % ip[0], shell=True, stdout=open('/dev/null', 'w'), stderr=subprocess.STDOUT)
        if ret == 0:
            print('%s-%s is up!' % (ip[1], ip[0]))
        elif ret==1:
            print('%s is down' % (ip[1], ip[0]))
        queue.task_done() 
        
for i in range(num_threads):
    t = Thread(target=pingme, args=(i, q))
    t.setDaemon(True)
    t.start() 

# db = pymysql.connect(host='10.50.99.247',
#                      user='network',
#                      password='xxx',
#                      port=3306,
#                      db = 'network',
#                      charset = 'utf8'
#                      )

# cursor = db.cursor()
# cursor.execute('select ipadd, name from net_dev where `group`')
# data = cursor.fetchall()
# for i in data:
#     q.put(i) 
# q.join() 

        



