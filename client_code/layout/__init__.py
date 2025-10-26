from ._anvil_designer import layoutTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


class layout(layoutTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def link_home_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('home_page')

  def link_networks_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('networks_page')

  def link_scan_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('scan_network_page')

  def link_maintenance_click(self, **event_args):
    """This method is called when the link is clicked"""
    open_form('maintenance_page')
