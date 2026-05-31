output "resource_group_name" {
  value = azurerm_resource_group.rg.name
}

output "storage_account_name" {
  value = azurerm_storage_account.adls.name
}

output "data_factory_name" {
  value = azurerm_data_factory.adf.name
}

output "databricks_workspace_name" {
  value = azurerm_databricks_workspace.dbw.name
}

output "key_vault_name" {
  value = azurerm_key_vault.kv.name
}

output "log_analytics_workspace_name" {
  value = azurerm_log_analytics_workspace.log.name
}