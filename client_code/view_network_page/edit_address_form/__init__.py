from ._anvil_designer import edit_address_formTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.js

class edit_address_form(edit_address_formTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_ip_click(self, **event_args):
    """This method is called when the button is clicked"""
    text = self.item['ip']
    anvil.js.call_js('copyclip', text)
    anvil.Notification('IP has been copied to clipboard!').show()
    self.raise_event('x-close-alert')

  def button_mac_click(self, **event_args):
    """This method is called when the button is clicked"""
    text = self.item['mac']
    anvil.js.call_js('copyclip', text)
    anvil.Notification('MAC has been copied to clipboard!').show()
    self.raise_event('x-close-alert')

  def button_mac_dash_click(self, **event_args):
    """This method is called when the button is clicked"""
    text = self.item['mac']
    newtext = text.replace(':', '-')
    anvil.js.call_js('copyclip', newtext)
    anvil.Notification('MAC has been copied to clipboard!').show()
    self.raise_event('x-close-alert')

  def button_mac_nospace_click(self, **event_args):
    """This method is called when the button is clicked"""
    text = self.item['mac']
    newtext = text.replace(':', '')
    anvil.js.call_js('copyclip', newtext)
    anvil.Notification('MAC has been copied to clipboard!').show()
    self.raise_event('x-close-alert')

  def button_toggle_dhcp_click(self, **event_args):
    """This method is called when the button is clicked"""
    state = anvil.server.call('toggle_dhcp', self.item['ip'])
    if state:
      anvil.Notification(self.item['ip'] + " has DHPC status of True").show()
    else:
      anvil.Notification(self.item['ip'] + " has DHPC status of False").show()
    net = app_tables.networks.get(id=self.item['parent_id'])
    self.raise_event('x-close-alert')
    open_form('view_network_page', net)
