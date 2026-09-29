import sys
import json
from client import InboxTriageShield

shield = InboxTriageShield()

def handle_request(req):
    method = req.get("method")
    req_id = req.get("id")
    
    if method == "initialize":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "protocolVersion": "2024-11-05",
                "capabilities": {"tools": {}},
                "serverInfo": {"name": "genpark-inbox-triage-communication-shield-skill", "version": "1.0.0"}
            }
        }
    elif method == "tools/list":
        return {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": {
                "tools": [
                    {
                        "name": "evaluate_message",
                        "description": "Triage incoming message for VIP priority and delivery routing",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "sender": {"type": "string"},
                                "text": {"type": "string"},
                                "channel": {"type": "string"}
                            },
                            "required": ["sender", "text"]
                        }
                    },
                    {
                        "name": "get_digest",
                        "description": "Fetch collected message digests filtered by tier",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "tier": {"type": "string"}
                            }
                        }
                    }
                ]
            }
        }
    elif method == "tools/call":
        params = req.get("params", {})
        tool_name = params.get("name")
        args = params.get("arguments", {})
        
        if tool_name == "evaluate_message":
            res = shield.evaluate_message(args["sender"], args["text"], args.get("channel", "whatsapp"))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}
        elif tool_name == "get_digest":
            res = shield.get_digest(args.get("tier"))
            return {"jsonrpc": "2.0", "id": req_id, "result": {"content": [{"type": "text", "text": json.dumps(res, indent=2)}]}}

    return {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": "Method not found"}}

def main():
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            res = handle_request(req)
            sys.stdout.write(json.dumps(res) + "\n")
            sys.stdout.flush()
        except Exception as e:
            err_res = {"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": str(e)}}
            sys.stdout.write(json.dumps(err_res) + "\n")
            sys.stdout.flush()

if __name__ == "__main__":
    main()
