import os

# Use a try-except block to handle cases where Azure SDKs are not installed
try:
    from azure.identity import DefaultAzureCredential
    # Corrected import path for the Monitor client
    from azure.mgmt.monitor import MonitorManagementClient
    AZURE_SDK_AVAILABLE = True
except ImportError:
    AZURE_SDK_AVAILABLE = False

def monitor_simulation():
    """
    Placeholder function for monitoring the simulation using Azure Monitor.

    In a real implementation, this would query logs and metrics from Azure Monitor.
    For local mode, this function simply prints a message and does nothing.
    """
    mode = os.environ.get("SIMULATION_MODE", "local")

    if mode != "cloud":
        print("INFO: Skipping Azure monitoring in non-cloud mode.")
        return

    if not AZURE_SDK_AVAILABLE:
        print("ERROR: Azure SDKs not installed. Cannot monitor. Run 'pip install -r requirements.txt'.")
        return

    print("INFO: Azure monitoring logic would execute here.")
    # In a real scenario, you would use the MonitorManagementClient
    # to query for metrics and logs from your deployed resources.
    return True

def get_monitor_client():
    credential = DefaultAzureCredential()
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        raise ValueError("Set AZURE_SUBSCRIPTION_ID in .env or environment")
    return MonitorManagementClient(credential, subscription_id)

def log_event(resource_id, event_data):
    client = get_monitor_client()
    client.activity_logs.create_or_update(
        resource_id=resource_id,
        parameters=event_data
    )
    return f"Logged event for resource {resource_id}"

def get_metrics(resource_id, metric_name, timespan):
    client = get_monitor_client()
    metrics_data = client.metrics.list(
        resource_id=resource_id,
        timespan=timespan,
        metricnames=metric_name
    )
    return metrics_data

def setup_alerts(resource_id, alert_rule):
    client = get_monitor_client()
    client.alert_rules.create_or_update(
        resource_group_name=alert_rule['resource_group'],
        rule_name=alert_rule['name'],
        parameters=alert_rule['parameters']
    )
    return f"Alert rule {alert_rule['name']} set up for resource {resource_id}"