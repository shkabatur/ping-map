from multiping import MultiPing, multi_ping
from bottle import *
import json
import socket
import threading
import asyncio

with open('nodes.json', encoding='utf-8') as f:
    nodes = json.load(f)
ips = [n['ip'] for n in nodes]


    
def update_nodes():
    threading.Timer(5.0, update_nodes).start()
    responses, no_responses = multi_ping(ips,timeout=4, retry=3)
    for n in nodes:
        if n['ip'] in responses:
            n['ping'] = responses[n['ip']] * 1000
            n['result'] = True
            print("OK")
        else:
            n['ping'] = 9999
            n['result'] = False
            print("FUCK")

update_nodes()

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')

@route('/')
def index(): 
    return static_file('index.html', root='static/')

@route('/edit')
def edit(): 
    return static_file('editor.html', root='static/')

@route('/nodes')
def retur_nodes():
    response.content_type = 'application/json'
    return json.dumps(nodes)
    
threading.Thread(target=update_nodes).start()
threading.Thread(target=run, kwargs = {'host':'localhost', 'port':80, 'debug':True}).start()

#run(host='localhost', port=80, debug=True)


