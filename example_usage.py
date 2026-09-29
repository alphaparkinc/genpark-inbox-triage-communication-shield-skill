from client import InboxTriageShield

shield = InboxTriageShield(high_priority_senders=["founder_partner", "alex_investor"])

# Ingest various incoming messages
m1 = shield.evaluate_message("founder_partner", "Urgent: Term sheet signature deadline is 5pm today", channel="imessage")
m2 = shield.evaluate_message("groupon_deals", "50% off pizza today only", channel="email")

print("Evaluated Messages:")
print(f" - [{m1['tier']}] Routed to: {m1['route']}")
print(f" - [{m2['tier']}] Routed to: {m2['route']}")

daily_digest = shield.get_digest(tier="ROUTINE")
print("Pending Routine Digest Items:", len(daily_digest))
