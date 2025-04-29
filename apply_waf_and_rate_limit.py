import requests
import yaml
from datetime import datetime
import os

# Helper function to log messages
def log_message(message):
    log_path = "logs/waf_setup.log"
    os.makedirs(os.path.dirname(log_path), exist_ok=True)
    with open(log_path, "a") as log_file:
        log_file.write(f"[{datetime.now()}] {message}\n")

# Load config
with open("config.yaml", "r") as file:
    config = yaml.safe_load(file)["cloudflare"]

headers = {
    "Authorization": f"Bearer {config['api_token']}",
    "Content-Type": "application/json"
}

zone_id = config["zone_id"]
base_url = config["base_url"]

# 1. Add WAF rule to block known bots
waf_url = f"{base_url}zones/{zone_id}/firewall/rules"
waf_rule = {
    "action": "block",
    "filter": {
        "expression": "(http.user_agent contains 'BadBot')",
        "paused": False,
        "description": "Block Bad Bots"
    },
    "description": "Block known bad bots",
    "priority": 1
}

waf_response = requests.post(waf_url, headers=headers, json=[waf_rule])
if waf_response.status_code in [200, 201]:
    waf_id = waf_response.json()[0]["id"]
    with open("logs/waf_rule_id.txt", "w") as f:
        f.write(waf_id)
    message = f"✅ WAF rule created. ID: {waf_id}"
    print(message)
    log_message(message)
else:
    error = f"❌ Failed to create WAF rule: {waf_response.text}"
    print(error)
    log_message(error)

# 2. Set up Rate Limiting
rate_limit_url = f"{base_url}zones/{zone_id}/rate_limits"
rate_limit_rule = {
    "threshold": 10,
    "period": 1,
    "action": {
        "mode": "simulate",  # Change to "block" to enforce
        "timeout": 60
    },
    "match": {
        "request": {
            "methods": ["GET", "POST"],
            "schemes": ["HTTP", "HTTPS"],
            "url": f"*{config['domain']}/*"
        }
    },
    "enabled": True,
    "description": "Limit requests per IP"
}

rl_response = requests.post(rate_limit_url, headers=headers, json=rate_limit_rule)
if rl_response.status_code in [200, 201]:
    rl_id = rl_response.json()["id"]
    with open("logs/rate_limit_id.txt", "w") as f:
        f.write(rl_id)
    message = f"✅ Rate limiting rule created. ID: {rl_id}"
    print(message)
    log_message(message)
else:
    error = f"❌ Failed to create rate limiting rule: {rl_response.text}"
    print(error)
    log_message(error)
