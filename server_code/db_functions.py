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
@anvil.server.callable
def add_network(item):
  app_tables.networks.add_row(
    id= get_next_id(),
    name= item['name'],
    ip_addr= item['ip'],
  )

@anvil.server.callable
def get_networks():
  return app_tables.networks.search()



def get_next_id():
  id = app_tables.networks.search()
  if id:
    return len(id)
  else:
    return 0