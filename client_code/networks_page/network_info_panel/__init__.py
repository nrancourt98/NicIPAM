from ._anvil_designer import network_info_panelTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class network_info_panel(network_info_panelTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    used_text = str(self.item['used']) + "/" + str(self.item['total'])
    # Any code you write here will run before the form opens.
    self.label_used.text = used_text

  def button_open_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('view_network_page', self.item)
