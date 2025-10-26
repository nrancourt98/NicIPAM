from ._anvil_designer import maintenance_pageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class maintenance_page(maintenance_pageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_ip_int_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = False
    result = anvil.server.call('update_ip_ints')
    if result:
      alert("IP integers have been updated!")
    else:
      alert("Function failed")

  def button_update_counts_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = False
    result = anvil.server.call('update_used_counts')
    if result:
      alert("IP counts have been updated!")
    else:
      alert("Function failed")
