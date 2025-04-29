import requests
import yaml

# Load Cloudflare config
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)["cloudflare"]

headers = {
    "Authorization": f"Bearer {config['api_token']}",
    "Content-Type": "application/json"
}

url = f"{config['base_url']}zones/{config['zone_id']}/dns_records"

response = requests.get(url, headers=headers)

if response.status_code == 200:
    records = response.json()["result"]
    print(f"\n✅ DNS Records for {config['domain']}:\n")
    for record in records:
        print(f"- Type: {record['type']} | Name: {record['name']} | Content: {record['content']}")
else:
    print("❌ Failed to fetch DNS records.")
    print("Status Code:", response.status_code)
    print("Response:", response.text)
