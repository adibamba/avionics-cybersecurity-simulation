from flask import Flask, request, jsonify

class Firewall:
    def __init__(self):
        self.rules = []

    def add_rule(self, rule):
        self.rules.append(rule)

    def remove_rule(self, rule):
        self.rules.remove(rule)

    def check_access(self, source_ip, destination_ip):
        for rule in self.rules:
            if rule['source_ip'] == source_ip and rule['destination_ip'] == destination_ip:
                return rule['action']
        return 'ALLOW'

app = Flask(__name__)
firewall = Firewall()

@app.route('/firewall/rule', methods=['POST'])
def add_firewall_rule():
    rule = request.json
    firewall.add_rule(rule)
    return jsonify({"message": "Rule added"}), 201

@app.route('/firewall/rule', methods=['DELETE'])
def remove_firewall_rule():
    rule = request.json
    firewall.remove_rule(rule)
    return jsonify({"message": "Rule removed"}), 200

@app.route('/firewall/check', methods=['GET'])
def check_firewall_access():
    source_ip = request.args.get('source_ip')
    destination_ip = request.args.get('destination_ip')
    action = firewall.check_access(source_ip, destination_ip)
    return jsonify({"action": action}), 200

if __name__ == '__main__':
    app.run(debug=True)