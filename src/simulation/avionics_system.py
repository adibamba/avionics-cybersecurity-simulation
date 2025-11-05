class AvionicsSystem:
    """
    Represents the collection of avionics subsystems on the aircraft.
    It manages the state and health of each component based on a configuration.
    """
    def __init__(self, config=None):
        """
        Initializes the avionics system based on a configuration dictionary.

        Args:
            config (dict, optional): A dictionary containing system definitions,
                                     like the 'avionics' section from the YAML file.
                                     Defaults to None for testability.
        """
        self.systems = {}

        # If a config is provided, load the systems from it
        if config and "systems" in config:
            for system_config in config["systems"]:
                sys_id = system_config.get("id")
                if sys_id:
                    self.systems[sys_id] = {
                        "name": system_config.get("name", "Unknown"),
                        "status": system_config.get("status", "offline")
                    }
        
        # If no config or systems, create a default one for basic functionality
        if not self.systems:
            self.systems["default"] = {"name": "Default System", "status": "nominal"}

    def get_system_status(self, system_id: str) -> str:
        """
        Returns the status of a specific avionics subsystem.
        """
        system = self.systems.get(system_id)
        return system["status"] if system else "not_found"

    def update_system_status(self, system_id: str, new_status: str):
        """
        Updates the status of a specific avionics subsystem.
        """
        if system_id in self.systems:
            self.systems[system_id]["status"] = new_status
            return True
        return False

    def receive_command(self, command: str):
        """
        A placeholder method for receiving commands from the FlightController.
        """
        # In a real simulation, this would affect system state.
        pass