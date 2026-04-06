import pywifi
import time

def scan_networks():
    wifi = pywifi.PyWiFi()
    interfaces = wifi.interfaces()

    if len(interfaces) == 0:
        return {}

    iface = interfaces[0]

    iface.scan()
    time.sleep(5)

    results = iface.scan_results()

    networks = {}

    for net in results:
        if net.ssid == "":
            continue

        if net.ssid not in networks:
            networks[net.ssid] = {}

        networks[net.ssid][net.bssid] = net.signal

    return networks