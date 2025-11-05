class AvionicsSystem:
    def __init__(self):
        self.system_state = {
            "navigation": "offline",
            "communication": "offline",
            "control": "inactive"
        }

    def initialize_system(self):
        self.system_state["navigation"] = "online"
        self.system_state["communication"] = "online"
        self.system_state["control"] = "active"
        return self.system_state

    def simulate_communication(self, message):
        if self.system_state["communication"] == "online":
            return f"Communicating: {message}"
        else:
            return "Communication system is offline."

    def update_control(self, status):
        if status in ["active", "inactive"]:
            self.system_state["control"] = status
            return f"Control system is now {status}."
        else:
            return "Invalid control status."

    def get_system_status(self):
        return self.system_state