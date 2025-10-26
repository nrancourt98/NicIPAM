from ._anvil_designer import networks_list_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class networks_list_form(networks_list_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.
    self.label_name.text = self.item['name']
    self.label_subnet.text = self.item['ip_addr']
    self.label_total.text = self.item['total']
    self.label_used.text = self.item['used']
    self.label_remaining.text = (self.item['total'] - self.item['used'])

  def button_open_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('view_network_page', self.item)
