from ._anvil_designer import networks_pageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .delete_network_form import delete_network_form
from .add_network_form import add_network_form

class networks_page(networks_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_networks.items = app_tables.networks.search(tables.order_by("vlan_id", ascending=True))

  def button_delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    network = {}
    delete = alert(
      content=delete_network_form(item=network),
      title="Delete Network",
      large=True,
      buttons=[("DELETE", True), ("Cancel", False)]
    )
    if delete:
      r = anvil.server.call('delete_network', network['name'])
      if r:
        alert("Network deleted successfully")
        open_form('networks_page')
      else:
        alert("Function error")

  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    item = {}
    add = alert(
      content=add_network_form(item=item),
      title="Add Network",
      large=True,
      buttons=[("ADD", True), ("CANCEL", False)]
    )
    if add:
      result = anvil.server.call('add_network', item)
      if result:
        alert("Network Added Sucessfully!")
        open_form('networks_page')
      else:
        alert("Failed to add network")
