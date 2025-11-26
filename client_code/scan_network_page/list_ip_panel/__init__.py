from ._anvil_designer import list_ip_panelTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class list_ip_panel(list_ip_panelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_add_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = anvil.server.call('add_scanned_ip', self.label_ip.text, self.label_mac.text, self.label_hostname.text)
    if result:
      alert("IP has been added to parent network!")
      open_form('scan_network_page')
    else:
      alert("A parent network could not be found, please create the network before adding the IP.")

  def button_delete_click(self, **event_args):
    """This method is called when the button is clicked"""
    result = anvil.server.call('delete_scan_ip', self.label_ip.text)
    if result:
      alert("IP has been removed from the scan list.")
      open_form('scan_network_page')
    else:
      alert("Error removing the IP from the scan list!")
