from ._anvil_designer import view_network_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .add_ip_form import add_ip_form


class view_network_page(view_network_pageTemplate):
  def __init__(self, network, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.network = network
    self.net_id = network['id']
    self.repeating_panel_addresses.items = app_tables.address.search(parent_id=network['id'])
    self.label_network_name.text = network['name']
    self.label_vlan.text = "VLAN ID: " + str(network['vlan_id'])
    self.label_total_used.text = "USED: " + str(network['used']) + "/" + str(network['total'])
    self.label_ip.text = "SUBNET: " + network['ip_addr']

  def link_return_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('networks_page')

  def button_add_address_click(self, **event_args):
    """This method is called when the button is clicked"""
    item = {}
    saved = False
    saved = alert(
      content = add_ip_form(item=item),
      title="Add IP Address",
      large=True,
      buttons=[("Add", True)]
    )
    if saved:
      item['id'] = self.net_id
      result = anvil.server.call('add_ip_address', item)
      if result:
        alert('IP Address added successfully!')
        open_form('view_network_page', self.network)
      else:
        alert('Error: IP Address failed to add when calling the function')
