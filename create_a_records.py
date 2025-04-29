import requests
import yaml

# Load Cloudflare config
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)["cloudflare"]

# Set API headers
headers = {
    "Authorization": f"Bearer {config['api_token']}",
    "Content-Type": "application/json"
}

# List of A records to create
a_records = [
    {"name": "devops", "content": "162.255.119.110"},
    {"name": "gym", "content": "162.255.119.110"},
    {"name": "music", "content": "162.255.119.110"},
]

# Base URL for DNS records
base_url = f"{config['base_url']}zones/{config['zone_id']}/dns_records"

# Step 1: Get existing records
response = requests.get(base_url, headers=headers)
existing_records = response.json()["result"] if response.status_code == 200 else []

# Step 2: Create new records only if they don't exist
for record in a_records:
    full_name = f"{record['name']}.{config['domain']}"
    already_exists = any(r["type"] == "A" and r["name"] == full_name for r in existing_records)

    if already_exists:
        print(f"⚠️ A record already exists: {full_name}")
        continue  # Skip if record exists

    # Data for the new A record
    data = {
        "type": "A",
        "name": record["name"],
        "content": record["content"],
        "ttl": 3600,
        "proxied": False
    }

    # Create the A record
    response = requests.post(base_url, headers=headers, json=data)

    if response.status_code in [200, 201]:
        print(f"✅ Created A record: {full_name} -> {record['content']}")
    else:
        print(f"❌ Failed to create A record: {full_name}")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
