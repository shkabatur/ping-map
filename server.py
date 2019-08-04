from multiping import multi_ping
from bottle import *
import json
import socket
import threading


with open('nodes.json', encoding='utf-8') as f:
    nodes = json.load(f)
ips = [n['ip'] for n in nodes]
    
def update_nodes():
    threading.Timer(5.0, update_nodes).start()
    print("hey")
    responses, no_responses = multi_ping(ips, timeout=2, retry=3)
    for n in nodes:
        if n['ip'] in responses:
            n['ping'] = responses[n['ip']] * 1000
            n['result'] = True
        else:
            n['ping'] = 9999
            n['result'] = False

update_nodes()

@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='static/')

@route('/')
def index():
    ip = socket.gethostbyname(socket.gethostname())
    with open('static/index.html') as f:
        tmpl = f.read() 
    return template(tmpl, ip=ip)

@route('/nodes')
def retur_nodes():
    response.content_type = 'application/json'
    return json.dumps(nodes)
    



run(host='localhost', port=80, debug=True)
