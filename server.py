from multiping import MultiPing, multi_ping
from bottle import *
import json
import socket
import threading
import asyncio

with open('nodes.json', encoding='utf-8') as f:
    nodes = json.load(f)
print('initialization <> id(nodes) = {}'.format(id(nodes)))
ips = [n['ip'] for n in nodes]

my_request = []
    
def update_nodes():
    threading.Timer(5.0, update_nodes).start()
    responses, no_responses = multi_ping(ips,timeout=4, retry=3)
    for n in nodes:
        if n['ip'] in responses:
            n['ping'] = responses[n['ip']] * 1000
            n['result'] = True
            #print("OK")
        else:
            n['ping'] = 9999
            n['result'] = False
            #print("FUCK")

@post('/change-nodes')
def change_nodes():
    with open('nodes.json', 'w',  encoding='utf-8') as f:
        f.write(json.dumps(request.json)) 
    nodes = request.json
    ips = [n['ip'] for n in nodes]
    print('change_nodes <> id(nodes) = {}'.format(id(nodes)))


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
    print('return nodes <> id(nodes) = {}'.format(id(nodes)))
    return json.dumps(nodes)
    
threading.Thread(target=update_nodes).start()
threading.Thread(target=run, kwargs = {'host':'localhost', 'port':80, 'debug':True}).start()

#run(host='localhost', port=80, debug=True)


