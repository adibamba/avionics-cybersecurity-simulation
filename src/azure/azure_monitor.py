import os
from azure.monitor import MonitorClient
from azure.identity import DefaultAzureCredential

def get_monitor_client():
    credential = DefaultAzureCredential()
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        raise ValueError("Set AZURE_SUBSCRIPTION_ID in .env or environment")
    return MonitorClient(credential, subscription_id)

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