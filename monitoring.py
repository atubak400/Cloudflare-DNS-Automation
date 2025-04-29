import requests
import yaml
from datetime import datetime
import os

# Logging helper
def log_message(message):
    os.makedirs("logs", exist_ok=True)
    with open("logs/monitoring.log", "a") as f:
        f.write(f"[{datetime.now()}] {message}\n")

# Load config
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)["cloudflare"]

zone_id = config["zone_id"]
base_url = config["base_url"]
headers = {
    "Authorization": f"Bearer {config['api_token']}",
    "Content-Type": "application/json"
}

# Fetch current DNS records
url = f"{base_url}zones/{zone_id}/dns_records"
response = requests.get(url, headers=headers)

if response.status_code not in [200, 201]:
    error_msg = f"❌ Failed to fetch DNS records: {response.text}"
    print(error_msg)
    log_message(error_msg)
    exit()

actual_records = response.json()["result"]
actual_lookup = {(r["type"], r["name"]): r["content"] for r in actual_records}

# Compare expected vs actual
print("\n🔍 DNS Compliance Check:\n")
log_message("🔍 DNS Compliance Check:")

for record in config["expected_records"]:
    key = (record["type"], record["name"])
    expected = record["content"]
    actual = actual_lookup.get(key)

    if actual == expected:
        result = f"✅ {record['type']} {record['name']} → {expected}"
    else:
        result = f"❌ {record['type']} {record['name']} → Expected: {expected}, Found: {actual or 'Missing'}"

    print(result)
    log_message(result)
