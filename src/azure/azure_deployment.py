import os
from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.containerinstance import ContainerInstanceManagementClient

def get_resource_client():
    credential = DefaultAzureCredential()
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")
    if not subscription_id:
        raise ValueError("Set AZURE_SUBSCRIPTION_ID in .env or environment")
    return ResourceManagementClient(credential, subscription_id)

def create_resource_group(resource_group_name, location):
    client = get_resource_client()
    return client.resource_groups.create_or_update(resource_group_name, {"location": location})

def deploy_virtual_machine(resource_group_name, vm_name, location):
    compute_client = ComputeManagementClient(get_resource_client().credentials, os.environ.get("AZURE_SUBSCRIPTION_ID"))
    # Define VM parameters here (omitted for brevity)
    # compute_client.virtual_machines.begin_create_or_update(resource_group_name, vm_name, vm_parameters)
    return f"Virtual Machine {vm_name} deployed in {resource_group_name}"

def deploy_container_instance(resource_group_name, container_group_name, location):
    container_client = ContainerInstanceManagementClient(get_resource_client().credentials, os.environ.get("AZURE_SUBSCRIPTION_ID"))
    # Define container parameters here (omitted for brevity)
    # container_client.container_groups.begin_create_or_update(resource_group_name, container_group_name, container_group)
    return f"Container instance {container_group_name} deployed in {resource_group_name}"