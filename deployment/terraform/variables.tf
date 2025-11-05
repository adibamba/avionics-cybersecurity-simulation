variable "resource_group_name" {
  description = "The name of the resource group where the resources will be deployed."
  type        = string
  default     = "avionics-cybersecurity-simulation-rg"
}

variable "location" {
  description = "Azure location"
  type        = string
  default     = "East US"
}

variable "vm_size" {
  description = "The size of the virtual machines to be created."
  type        = string
  default     = "Standard_B1s"   # free-tier eligible
}

variable "admin_username" {
  description = "The admin username for the virtual machines."
  type        = string
  default     = "adminuser"
}

variable "admin_password" {
  description = "The admin password for the virtual machines."
  type        = string
  sensitive   = true
  # no default here for safety; set in terraform.tfvars
}

variable "storage_account_name" {
  description = "The name of the storage account to be created."
  type        = string
}

variable "container_name" {
  description = "The name of the blob container for storing simulation data."
  type        = string
  default     = "simulation-data"
}