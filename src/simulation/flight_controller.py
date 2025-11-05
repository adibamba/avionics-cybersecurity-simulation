class FlightController:
    def __init__(self, avionics_system):
        self.avionics_system = avionics_system
        self.flight_status = "Grounded"

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