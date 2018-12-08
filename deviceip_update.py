#!/usr/bin/env python3


# If `default` isn't set, it will automatically be set to the router (usable for tethering).
# `actions` can be used to turn off/start programs


import json
import nmap
import socket
import objc
import sys
from pathlib import Path
import os

VAR_FILE = '~/Dropbox/bin/theos.sh'

def get_config():
    directory = os.path.dirname(os.path.abspath(__file__))
    with open(directory + '/config.json') as data_file:    
        return json.load(data_file)


def get_ssid():
    objc.loadBundle('CoreWLAN',
                    bundle_path='/System/Library/Frameworks/CoreWLAN.framework',
                    module_globals=globals())

    ssid = None
    for iname in CWInterface.interfaceNames():
        interface = CWInterface.interfaceWithName_(iname)
        ssid = interface.ssid()

    return ssid

def update_with_device(device):
    print("Picked device: " + device['name'] + ", IP: " + device['IP'] + ", port:", device['port'])

    file_path = VAR_FILE.replace('~', str(Path.home()))
    with open(file_path, "w") as file:
        file.write("export THEOS_DEVICE_IP=" + device['IP'] + '\n')
        file.write("export THEOS_DEVICE_PORT=" + str(device['port']) + '\n')


def update_with_network(network):
    device_name = None
    if (len(sys.argv) > 1):
        device_name = sys.argv[1]

    print("picked network: " + network["name"])
    default_device = None
    for device in network['devices']:
        if (device_name != None and device_name == device['name']):
            return update_with_device(device);

        if (device['name'] == network['default']):
            if (device_name == None):
                return update_with_device(device);
            default_device = device

    update_with_device(default_device);


def scan_networks():
    default_network = None
    for network in config['networks']:
        if ('IP' in network and ip.startswith(network['IP'].split('*')[0])):
            print("starts with: " + network['IP'])
            update_with_network(network)
            return
        elif (ssid and ssid.startswith(network['name'].split('*')[0])):
            print("found name: " + network['name'])
            update_with_network(network)
            return

        if (network['name'] == config['default']):
            print("found default network")
            default_network = network

    print("did not find anything, setting default")
    update_with_network(default_network)


config = get_config()
ssid = get_ssid()
ip = socket.gethostbyname(socket.gethostname())

scan_networks()
