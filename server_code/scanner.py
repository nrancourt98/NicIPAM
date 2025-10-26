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
import ipaddress
import subprocess
import platform
import socket
from concurrent.futures import ThreadPoolExecutor, as_completed


def ping_host(ip):
  param = "-n" if platform.system().lower() == "windows" else "-c"
  try:
    result = subprocess.run(
      ["ping", param, "1", str(ip)],
      stdout=subprocess.DEVNULL,
      stderr=subprocess.DEVNULL
    )
    return result.returncode == 0
  except Exception:
    return False

def resolve_hostname(ip):
  try:
    return socket.gethostbyaddr(str(ip))[0]
  except socket.herror:
    return "Unknown"

@anvil.server.callable
def scan_subnet(subnet):
  hosts = {}
  net = ipaddress.ip_network(subnet, strict=False)
  with ThreadPoolExecutor(max_workers=50) as executor:
    futures = {executor.submit(ping_host, ip): ip for ip in net.hosts()}
    for future in as_completed(futures):
      ip = futures[future]
      if future.result():  # Host is alive
        hostname = resolve_hostname(ip)
        hosts[str(ip)] = {"hostname": hostname, "mac": None}
  return hosts


  
