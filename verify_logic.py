import requests
import time

BASE_URL = "http://localhost:8000/api"

def report_incident(zone):
    print(f"Reporting incident in {zone}...")
    resp = requests.post(f"{BASE_URL}/incidents/", json={"zone_id": zone})
    if resp.status_code == 200:
        print("Success.")
    else:
        print(f"Failed: {resp.text}")

def check_status(zone):
    resp = requests.get(f"{BASE_URL}/zones/{zone}/status")
    data = resp.json()
    print(f"[{zone}] Severity: {data['severity']}, Count (3h): {data['incident_count']}")

# Reset first
requests.post(f"{BASE_URL}/config/reset")

# Report 6 incidents in Zone A (Expect Red)
for _ in range(6):
    report_incident("Zone A")
    
check_status("Zone A")
