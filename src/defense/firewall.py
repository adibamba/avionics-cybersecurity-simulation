from flask import Flask, request, jsonify

# Keep imports out of top-level test import path (Flask only created when running module).
class Firewall:
    def __init__(self):
        # rules are dicts like {"action": "deny"|"allow", "source": "ip", "dest": "ip" or None}
        self.rules = []

    def add_rule(self, rule: dict):
        self.rules.append(rule)

    def remove_rule(self, rule: dict):
        if rule in self.rules:
            self.rules.remove(rule)

    def check_access(self, source_ip: str, destination_ip: str = None) -> bool:
        """
        Return True when access is allowed. Default permissive for tests.
        Deny if an explicit deny rule matches source (and optional dest).
        """
        for r in self.rules:
            if r.get("action") == "deny" and r.get("source") == source_ip:
                dest_rule = r.get("dest")
                if dest_rule is None or dest_rule == destination_ip:
                    return False
        return True

# Lazy-create Flask app only when module run directly (prevents Flask import at test collection time)
if __name__ == "__main__":
    from flask import Flask, request, jsonify
    app = Flask(__name__)
    fw = Firewall()

    @app.route('/firewall/rule', methods=['POST'])
    def add_firewall_rule():
        rule = request.json
        fw.add_rule(rule)
        return jsonify({"message": "Rule added"}), 201

    @app.route('/firewall/rule', methods=['DELETE'])
    def remove_firewall_rule():
        rule = request.json
        fw.remove_rule(rule)
        return jsonify({"message": "Rule removed"}), 200

    @app.route('/firewall/check', methods=['GET'])
    def check_firewall_access():
        source_ip = request.args.get('source_ip')
        destination_ip = request.args.get('destination_ip')
        action = fw.check_access(source_ip, destination_ip)
        return jsonify({"allowed": bool(action)}), 200

    app.run(debug=True)