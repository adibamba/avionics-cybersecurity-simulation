class FlightController:
    def __init__(self, avionics_system=None):
        self.avionics_system = avionics_system
        self.flight_status = "Grounded"

    def attach(self, avionics_system):
        """Attach or swap the avionics system at runtime."""
        self.avionics_system = avionics_system
        return True

    def issue_command(self, command: str) -> bool:
        """Send a command to the attached avionics system (no-op if none)."""
        if self.avionics_system and hasattr(self.avionics_system, "receive_command"):
            try:
                self.avionics_system.receive_command(command)
            except Exception:
                pass
        return True

    def send_command(self, command: str) -> bool:
        return self.issue_command(command)

    def take_off(self):
        if self.avionics_system.check_systems():
            self.flight_status = "In Air"
            return "Takeoff successful."
        else:
            return "Takeoff failed: Systems check incomplete."

    def land(self):
        if self.flight_status == "In Air":
            self.flight_status = "Landed"
            return "Landing successful."
        else:
            return "Landing failed: Aircraft is not in the air."

    def get_flight_status(self):
        return self.flight_status

    def execute_maneuver(self, maneuver):
        if self.flight_status == "In Air":
            return f"Executing maneuver: {maneuver}"
        else:
            return "Cannot execute maneuver: Aircraft is not in the air."