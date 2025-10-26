import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
import ipaddress

@anvil.server.callable
def add_network(item):
  app_tables.networks.add_row(
    id=get_next_id(),
    name= item['name'],
    ip_addr= item['ip'],
  )

@anvil.server.callable
def get_networks():
  return app_tables.networks.search()

@anvil.server.callable
def delete_network(network):
  net_id = network['id']
  ip_addresses = app_tables.address.search(parent_id=net_id)
  for r in ip_addresses:
    r.delete()
  network.delete()
  return True

@anvil.server.callable
def add_ip_address(item):
  app_tables.address.add_row(
    parent_id=item['parent_id'],
    ip=item['ip'],
    ip_int=int(ipaddress.IPv4Address(item['ip'])),
    hostname=item['hostname'],
    mac=item['mac'],
    description=item['description'],
  )
  increment_used_count(item['parent_id'])
  return True

@anvil.server.callable
def get_available_ip(network):
  subnet_net = network['ip_addr']
  net = ipaddress.ip_network(subnet_net, strict=False)
  ip_list = [str(ip) for ip in net.hosts()]
  existing_ip = app_tables.address.search(parent_id=network['id'])
  existing_ip_list = []
  for i in existing_ip:
    existing_ip_list.append(i['ip'])
  ip_remove = set(existing_ip_list)
  result = [item for item in ip_list if item not in ip_remove]
  return result

@anvil.server.callable
def find_parent_network(ip):
  networks = app_tables.networks.search()
  for i in networks:
    if ipaddress.ip_address(ip) in ipaddress.ip_network(i['ip_addr']):
      id = i['id']
      break
  return app_tables.networks.get(id=id)

def get_next_id():
  id = app_tables.networks.search()
  if id:
    return len(id)
  else:
    return 0

def increment_used_count(network_id):
  net = app_tables.networks.get(id=network_id)
  net['used'] += 1