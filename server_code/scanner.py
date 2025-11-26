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

@anvil.server.callable
def scan_subnet(subnet):
  for ip in ipaddress.IPv4Network(subnet, strict=False):
    ip_str = str(ip)
    # Step 1: Ping host (quietly)
    ping_result = subprocess.run(
      ["ping", "-c", "1", "-W", "1", ip_str],
      stdout=subprocess.DEVNULL,
      stderr=subprocess.DEVNULL
    )
    if ping_result.returncode == 0:
      # Step 2: Get MAC from ARP cache
      try:
        arp_output = subprocess.check_output(["arp", "-n", ip_str]).decode()
        mac = None
        for line in arp_output.splitlines():
          if ip_str in line:
            parts = line.split()
            if len(parts) >= 3:
              mac = parts[2]
      except Exception:
        mac = None
        # Step 3: Resolve hostname
      try:
        nslookup_output = subprocess.check_output(["nslookup", ip_str]).decode()
        hostname = None
        for line in nslookup_output.splitlines():
          if "name =" in line:
            hostname = line.split("name =")[-1].strip()
      except Exception:
        hostname = None
      app_tables.scans.add_row(ip=ip_str, mac=mac, hostname=hostname)



  
