import os
from src.simulation.avionics_system import AvionicsSystem
from src.simulation.network_simulator import NetworkSimulator
from src.simulation.flight_controller import FlightController
from src.attacks.dos_attack import DoSAttack
from src.attacks.mitm_attack import MITMAttack
from src.attacks.injection_attack import InjectionAttack
from src.attacks.replay_attack import ReplayAttack
from src.defense.intrusion_detection import IntrusionDetection
from src.defense.encryption import Encryption
# import authentication module robustly (some files expose functions, others a wrapper class)
import src.defense.authentication as authentication_module
from src.defense.firewall import Firewall
from src.azure.azure_deployment import deploy_simulation
from src.azure.azure_monitor import monitor_simulation
from src.monitoring.logger import Logger
from src.monitoring.metrics import Metrics
from src.utils.config import load_config

def main():
    config = load_config('config/simulation_config.yaml')
    
    logger = Logger()
    metrics = Metrics()
    
    avionics_system = AvionicsSystem(config['avionics'])
    network_simulator = NetworkSimulator(config['network'])
    flight_controller = FlightController(avionics_system)
    
    # Deploy the simulation environment in Azure
    deploy_simulation(config.get('azure', {}))
    
    # Initialize defense mechanisms
    intrusion_detection = IntrusionDetection()
    encryption = Encryption()
    # Ensure Authentication API exists regardless of how authentication.py is implemented
    if hasattr(authentication_module, "Authenticator"):
        Authentication = authentication_module.Authenticator
    else:
        # fallback wrapper that calls functions if available, or returns True by default
        class Authentication:
            def authenticate_user(self, username: str, password: str) -> bool:
                fn = getattr(authentication_module, "authenticate_user", None)
                return fn(username, password) if fn else True
            def authenticate_system(self, system_id: str, token: str) -> bool:
                fn = getattr(authentication_module, "authenticate_system", None)
                return fn(system_id, token) if fn else True

    authentication = Authentication()
    firewall = Firewall()
    
    # Simulate attacks
    dos_attack = DoSAttack(network_simulator)
    mitm_attack = MITMAttack(network_simulator)
    injection_attack = InjectionAttack(avionics_system)
    replay_attack = ReplayAttack(network_simulator)
    
    # Run the simulation
    logger.log("Starting simulation...")
    # Add logic to orchestrate the simulation, attacks, and defenses here
    
    # Monitor the simulation
    monitor_simulation()
    
    logger.log("Simulation completed.")

if __name__ == "__main__":
    main()