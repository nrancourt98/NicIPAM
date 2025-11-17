from ._anvil_designer import address_templateTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..edit_address_form import edit_address_form

class address_template(address_templateTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def button_edit_click(self, **event_args):
    """This method is called when the button is clicked"""
    alert(
      content = edit_address_form(item=self.item)
    )
