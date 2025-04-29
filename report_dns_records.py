import requests
import yaml
import json
import os
from datetime import datetime

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)["cloudflare"]

zone_id = config["zone_id"]
base_url = config["base_url"]
headers = {
    "Authorization": f"Bearer {config['api_token']}",
    "Content-Type": "application/json"
}

# Fetch DNS records
url = f"{base_url}zones/{zone_id}/dns_records"
response = requests.get(url, headers=headers)

if response.status_code not in [200, 201]:
    print("❌ Failed to fetch DNS records:", response.text)
    exit()

records = response.json()["result"]

# Prepare report file path
os.makedirs("reports", exist_ok=True)
timestamp = datetime.now().strftime("%Y-%m-%d")
report_path = f"reports/dns_snapshot_{timestamp}.json"

# Save as JSON
with open(report_path, "w") as f:
    json.dump(records, f, indent=2)

print(f"✅ DNS snapshot saved to {report_path}")
