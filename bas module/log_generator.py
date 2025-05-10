from faker import Faker
import pandas as pd
from mitre_mapping import MITRE_MAP  # Make sure this file exists and is correctly mapped

fake = Faker()

def generate_logs(events, user="intern"):
    logs = []
    for event in events:
        # Try to find a matching MITRE tactic
        tactic = "Unknown"
        for key in MITRE_MAP:
            if key in event:
                tactic = MITRE_MAP[key]
                break

        # Create log entry
        logs.append({
            "timestamp": fake.iso8601(),
            "user": user,
            "event": event,
            "tactic": tactic,
            "ip": fake.ipv4(),
            "location": fake.city(),
            "hostname": fake.hostname(),
            "os": fake.random_element(["Windows", "Linux", "MacOS", "Ubuntu", "Android"]),
            "user_agent": fake.user_agent(),
            "device": fake.random_element(["Desktop", "Laptop", "Mobile", "Server"]),
            "status": fake.random_element(["Success", "Failure"])
        })
    return pd.DataFrame(logs)
