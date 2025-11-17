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
def update_ip_ints():
  addresses = app_tables.address.search()
  for ip in addresses:
    ip['ip_int'] = int(ipaddress.IPv4Address(ip['ip']))
  return True

@anvil.server.callable
def update_used_counts():
  networks = app_tables.networks.search()
  for nets in networks:
    addresses = app_tables.address.search(parent_id=nets['id'])
    nets['used'] = len(addresses)
  return True

@anvil.server.callable
def clean_orphaned():
  ids = []
  for net in app_tables.networks.search():
    ids.append(net['id'])
  for address in app_tables.address.search():
    if not ids.__contains__(address['parent_id']): 
      address.delete()
  return True

@anvil.server.callable
def set_dhcp_all_false():
  for net in app_tables.address.search():
    net['dhcp'] = False
  return True
  