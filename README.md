# genpark-inbox-triage-communication-shield-skill

> Cross-Channel Inbox Triage & Communication Shield for Personal AI Agents. 100% Python Standard Library.

Distilled from **Pally**'s inbox-protection methodology, isolating the user from group chat flooding, spam, and non-critical messages across WhatsApp, iMessage, and email.

## Architecture

```mermaid
flowchart TD
    Msg["Incoming Message (WhatsApp / Email / RCS)"] --> VIPCheck{"Is VIP Sender?"}
    Msg --> UrgencyCheck{"Contains Urgent Keywords?"}
    VIPCheck -- Yes --> BothCheck{"Both VIP & Urgent?"}
    UrgencyCheck -- Yes --> BothCheck
    BothCheck -- Yes --> Immediate["Critical Tier: Immediate Push Alert"]
    BothCheck -- No --> Batch["Important Tier: Next Hourly Digest"]
    VIPCheck -- No --> RoutineCheck{"Urgent Keyword?"}
    RoutineCheck -- No --> Routine["Routine Tier: Daily Evening Digest"]
```

## Features
- **Fatigue Protection**: Eliminates attention fragmentation from non-urgent group chats.
- **Configurable Routing Paths**: Differentiates between instant interruptions and passive digest summaries.
