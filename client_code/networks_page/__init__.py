from ._anvil_designer import networks_pageTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from .delete_network_form import delete_network_form

class networks_page(networks_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.repeating_panel_networks.items = app_tables.networks.search(tables.order_by("vlan_id", ascending=True))

  def button_delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    network = []
    delete = alert(
      content=delete_network_form(network),
      title="Delete Network",
      large=True,
      buttons=[("DELETE", True), ("Cancel", False)]
    )
    if delete:
      r = anvil.server.call('delete_network', network)
      if r:
        alert("Network deleted successfully")
      else:
        alert("Function error")
    else:
      alert("Cancelled")
      
