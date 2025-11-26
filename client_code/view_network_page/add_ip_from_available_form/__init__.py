from ._anvil_designer import add_ip_from_available_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class add_ip_from_available_form(add_ip_from_available_formTemplate):
  def __init__(self, ip_address, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
  
    # Any code you write here will run before the form opens.
    self.label_ip_addr.text = ip_address
    self.check_box_dhcp.checked = True
