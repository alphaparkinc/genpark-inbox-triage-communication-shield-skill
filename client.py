"""Inbox Triage Communication Shield.
100% Python Standard Library.
"""

import time

class InboxTriageShield:
    """Classifies cross-channel incoming communications and shields the user from chat fatigue."""
    def __init__(self, high_priority_senders=None):
        self.high_priority_senders = set(high_priority_senders or [])
        self.message_queue = []

    def add_vip_sender(self, sender):
        self.high_priority_senders.add(sender)

    def evaluate_message(self, sender, text, channel="whatsapp"):
        urgent_keywords = ["urgent", "asap", "emergency", "deadline", "canceled", "reschedule"]
        text_lower = text.lower()
        
        is_vip = sender in self.high_priority_senders
        has_urgent_keyword = any(k in text_lower for k in urgent_keywords)
        
        if is_vip and has_urgent_keyword:
            tier = "CRITICAL"
            route = "IMMEDIATE_NOTIFICATION"
        elif is_vip or has_urgent_keyword:
            tier = "IMPORTANT"
            route = "NEXT_BATCH_DIGEST"
        else:
            tier = "ROUTINE"
            route = "DAILY_DIGEST"

        record = {
            "sender": sender,
            "channel": channel,
            "text": text,
            "tier": tier,
            "route": route,
            "timestamp": time.time()
        }
        self.message_queue.append(record)
        return record

    def get_digest(self, tier=None):
        if tier:
            return [m for m in self.message_queue if m["tier"] == tier]
        return list(self.message_queue)
