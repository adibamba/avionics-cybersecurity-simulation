# Avionics Cybersecurity Simulation
## Overview
This project simulates cyber-attacks on avionics systems and implements defense mechanisms to protect against these threats. It provides a comprehensive environment for testing and analyzing the resilience of avionics systems against various cyber threats.

[![Project Status](https://img.shields.io/badge/status-experimental-orange)](https://github.com/)
[![Python](https://img.shields.io/badge/python-3.10+-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

One-line elevator pitch
- Cloud sandbox to simulate cyber-attacks (DoS, MitM, injection, replay) against avionics networks (CAN, ARINC-like) and to test detection/defense strategies. Designed as a portfolio project to demonstrate practical skills in aeronautical systems simulation, cybersecurity, cloud automation (Azure), and observability.

Why this project matters
- Avionics systems have high safety and security requirements. This project demonstrates secure-by-design thinking by simulating attacks and defenses in a safe, isolated cloud environment instead of real aircraft hardware. Great for recruiters to evaluate practical skills in system-level thinking, cloud infra, security engineering, and embedded/network simulation.

Highlights / Recruiter snapshot
- Domain: Aeronautical engineering × Cybersecurity × Cloud (Azure)
- Demonstrates: Attack simulation, defensive controls, logging/monitoring, IaC, containerization, test automation, ML-ready telemetry pipeline.
- Technologies: Python, Scapy, Flask, Azure SDK, Terraform, Docker, pytest, pandas, scikit-learn, TensorFlow.
- Outcomes: reproducible scenarios, metrics/logging, Azure deployment templates, test suite.

Key features
- Config-driven simulation (config/simulation_config.yaml)
- Attack modules: DoS, Man-in-the-Middle, Injection, Replay
- Defense modules: IDS, encryption, authentication, rule-based firewall
- Azure integration: resource automation and monitoring hooks
- Monitoring & logging: structured logs and metric collection for analysis
- Tests: pytest-based unit tests and scenario tests
- Containerization: Dockerfile + deployment guidance
- Ethics-first: purely simulated environment; never run on operational aircraft

Repository layout (important files)
- src/
  - simulation/ — avionics_system.py, network_simulator.py, flight_controller.py
  - attacks/ — dos_attack.py, mitm_attack.py, injection_attack.py, replay_attack.py
  - defense/ — intrusion_detection.py, encryption.py, authentication.py, firewall.py
  - azure/ — azure_deployment.py, azure_monitor.py
  - monitoring/ — logger.py, metrics.py
  - utils/ — config loader
  - main.py — orchestrator
- config/
  - simulation_config.yaml — ready-made scenarios (modify for experiments)
  - azure_config.yaml — Azure deployment parameters
- deployment/
  - terraform/ — IaC for VMs & networking
  - docker/ — Dockerfile
- tests/ — pytest test suite
- requirements.txt — pinned dependencies

Skills showcased (useful for job descriptions)
- Network protocol simulation (packet crafting and analysis with Scapy)
- Threat emulation (DoS, MitM, replay, injection)
- Security controls (IDS design, encryption usage, auth, rule-based firewall)
- Cloud infra automation (Terraform + Azure SDK)
- Observability (structured logging, metrics, Azure Monitor integration)
- Data analysis & ML readiness (pandas, scikit-learn, TensorFlow for anomaly detection)
- Test-driven development (pytest) and CI/CD readiness (Docker + IaC)

Getting started — quick local dev (Windows)
Prereqs
- Python 3.10+ (recommended via pyenv/WLS/installer)
- pip, virtualenv
- Docker (optional for container runs)
- Terraform (for Azure infra)
- Azure CLI / credentials (for Azure deploys)

Quick setup
1. Clone the repo:
   git clone https://github.com/<your-username>/avionics-cybersecurity-simulation.git
   cd avionics-cybersecurity-simulation

2. Create and activate virtual environment (Windows PowerShell):
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1

3. Install dependencies:
   pip install -r requirements.txt

4. Run a smoke simulation (safe, local, config-driven):
   python src/main.py --config config/simulation_config.yaml --mode local

   - main.py accepts flags for mode (local/cloud), config path, logging level.
   - The provided config runs short scenarios (see config/simulation_config.yaml).

Testing
- Run unit tests:
  pytest tests/ -q

Azure deployment (high-level)
- Configure Azure credentials (Azure CLI + service principal recommended)
  az login
  export AZURE_SUBSCRIPTION_ID="..."

- Prepare terraform:
  cd deployment/terraform
  terraform init
  terraform apply

- Use src/azure/azure_deployment.py to programmatically create resources or integrate into CI.

Notes on safety & ethics (read before experimenting)
- This project is strictly for simulation and research. Do NOT run attack modules against production or operational systems.
- Use isolated lab accounts and Azure subscriptions. Do not use any real aircraft or certified avionics hardware for testing.
- Ensure compliance with local laws and organizational policies.

Extending the project (ideas to demonstrate advanced skills)
- Add ARINC 429 / CAN-specific message encoders/decoders and richer timing models
- Implement ML anomaly detection pipeline using telemetry + TensorFlow or scikit-learn
- Integrate Azure Sentinel or ELK stack for SIEM-level dashboards
- CI: GitHub Actions pipeline for lint/test/build and infra validation
- Multi-node distributed experiments using AKS and Helm charts

Sample outputs to show in portfolio / README visuals
- Attack timeline charts (traffic, CPU, packet drop)
- IDS alert dashboard screenshots
- Terraform plan/apply logs (sanitized)
- Unit test coverage badge (after CI)

How recruiters should evaluate code
- Look at src/attacks and src/defense for algorithmic clarity and comments
- Check src/azure for infra patterns and secure credential handling (DefaultAzureCredential)
- Review tests/ for coverage and scenario-driven tests
- Inspect config/ for reproducible experiments

Contributing
- Fork → feature branch → PR with tests and docs
- Keep PRs small and focused; include config changes required to reproduce your result

Contact / Portfolio context
- Add a short, one-line summary of your role on the project and a link to a live demo or walkthrough video (if available). Example:
  "Implemented network simulator and IDS prototype (Python/Scapy), wrote Terraform templates for Azure testbed, and produced five reproducible attack/defense scenarios — demo: <link>"

License
- MIT (update to your preferred license). See LICENSE file in repo.

Acknowledgements / References
- This repo is educational and research-focused. It draws on common avionics network concepts and open-source tooling (Scapy, Azure SDK, Terraform).