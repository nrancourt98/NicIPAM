from ._anvil_designer import view_network_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .add_ip_form import add_ip_form
from .list_available_form import list_available_form
from .add_ip_from_available_form import add_ip_from_available_form


class view_network_page(view_network_pageTemplate):
  def __init__(self, network, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.network = network
    self.net_id = network['id']
    self.repeating_panel_addresses.items = app_tables.address.search(tables.order_by('ip_int', ascending=True), parent_id=network['id'])
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
      item['parent_id'] = self.net_id
      result = anvil.server.call('add_ip_address', item)
      if result:
        alert('IP Address added successfully!')
        open_form('view_network_page', self.network)
      else:
        alert('Error: IP Address failed to add when calling the function')

  def button_show_available_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = None
    saved = None
    rp = RepeatingPanel(item_template=list_available_form)
    rp.items = anvil.server.call('get_available_ip', self.network)
    result = alert(
      content = rp,
      title="Available IP Addresses",
      large=True,
      buttons=None,
    )
    if result:
      value={}
      saved = alert(
        content=add_ip_from_available_form(result, item=value),
        title="Add IP Address",
        large=True,
        buttons=[("Add", True)]
      )
    if saved:
      value['parent_id'] = self.network['id']
      value['ip'] = result
      result = anvil.server.call('add_ip_address', value)
      if result:
        alert("Added IP Address Sucessfully!")
        open_form('view_network_page', self.network)
      else:
        alert("Failed to add IP when calling server function!")
    else:
      open_form('view_network_page', self.network)

  def button_scan_click(self, **event_args):
    """This method is called when the button is clicked"""
    confirm = False
    confirm = alert("Would you like to scan this network for new IP addresses?", buttons=[("Yes", True),("No", False)])
    if confirm:
      result = anvil.server.call('scan_subnet', self.network['ip_addr'])
      if len(result) == 0:
        alert("No new IP's have been found!")
      else:
        pass #This will be where the info is displayed and allows to add the IP
        
      