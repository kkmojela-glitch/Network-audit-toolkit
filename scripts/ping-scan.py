import os

def ping_host(ip):
    response = os.system(f"ping -c 1 {ip} > /dev/null 2>&1")
    if response == 0:
        return True
    else:
        return False

network = "192.168.1."

print("Starting Network Scan...\n")

for i in range(1, 21):
    ip = network + str(i)
    
    if ping_host(ip):
        print(f"[UP]   {ip}")
    else:
        print(f"[DOWN] {ip}")

print("\nScan Complete.")
