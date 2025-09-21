import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#
from scapy.all import ARP, Ether, srp

def arp_scan(network: str, timeout: float = 2) -> list[dict]:
  """
    Send ARP who-has to the entire subnet. Returns list of {'ip','mac'}.
    """
  packet = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=network)
  answered, _ = srp(packet, timeout=timeout, verbose=False)
  return [{"ip": recv.psrc, "mac": recv.hwsrc} for _, recv in answered]

if __name__ == "__main__":
  net = "192.168.1.0/24"
  clients = arp_scan(net)
  print("Discovered devices:")
  for c in clients:
    print(f"  {c['ip']}  ({c['mac']})")
