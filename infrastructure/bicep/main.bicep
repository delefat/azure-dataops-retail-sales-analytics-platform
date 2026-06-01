@description('Azure deployment location')
param location string = resourceGroup().location

@description('Deployment environment')
@allowed([
  'dev'
  'stg'
  'prd'
])
param environment string = 'dev'

@description('Project name')
param projectName string = 'retaildataops'

@description('Synapse SQL administrator username')
param synapseSqlAdminLogin string = 'sqladminuser'

@secure()
@description('Synapse SQL administrator password')
param synapseSqlAdminPassword string

@description('Synapse workspace location')
param synapseLocation string = 'centralindia'

var suffix = take(uniqueString(resourceGroup().id), 6)

var storageAccountName = take(toLower('${projectName}${environment}${suffix}'), 24)
var dataFactoryName = take('${projectName}-adf-${environment}-${suffix}', 63)
var databricksName = take('${projectName}-dbw-${environment}-${suffix}', 63)
var synapseName = take('${projectName}-syn-${environment}-${suffix}', 50)
var keyVaultName = take('${projectName}-kv-${environment}-${suffix}', 24)
var logAnalyticsName = take('${projectName}-log-${environment}-${suffix}', 63)
var commonTags = {
  environment: environment
  project: projectName
  owner: 'Dele Fatoba'
  managedBy: 'Bicep'
}

resource storageAccount 'Microsoft.Storage/storageAccounts@2023-05-01' = {
  name: storageAccountName
  location: location
  tags: commonTags
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    isHnsEnabled: true
    minimumTlsVersion: 'TLS1_2'
    allowBlobPublicAccess: false
  }
}

resource blobService 'Microsoft.Storage/storageAccounts/blobServices@2023-05-01' = {
  parent: storageAccount
  name: 'default'
}

resource rawContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-05-01' = {
  parent: blobService
  name: 'raw'
  properties: {
    publicAccess: 'None'
  }
}

resource bronzeContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-05-01' = {
  parent: blobService
  name: 'bronze'
  properties: {
    publicAccess: 'None'
  }
}

resource silverContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-05-01' = {
  parent: blobService
  name: 'silver'
  properties: {
    publicAccess: 'None'
  }
}

resource goldContainer 'Microsoft.Storage/storageAccounts/blobServices/containers@2023-05-01' = {
  parent: blobService
  name: 'gold'
  properties: {
    publicAccess: 'None'
  }
}

resource dataFactory 'Microsoft.DataFactory/factories@2018-06-01' = {
  name: dataFactoryName
  location: location
  tags: commonTags
  identity: {
    type: 'SystemAssigned'
  }
}

resource databricks 'Microsoft.Databricks/workspaces@2024-05-01' = {
  name: databricksName
  location: location
  tags: commonTags
  sku: {
    name: 'premium'
  }
   properties: {
    managedResourceGroupId: subscriptionResourceId(
      'Microsoft.Resources/resourceGroups',
      'rg-${projectName}-databricks-managed-${environment}-${suffix}'
    )
  }
}

resource synapseWorkspace 'Microsoft.Synapse/workspaces@2021-06-01' = {
  name: synapseName
  location: synapseLocation
  tags: commonTags
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    defaultDataLakeStorage: {
      accountUrl: storageAccount.properties.primaryEndpoints.dfs
      filesystem: rawContainer.name
    }
    publicNetworkAccess: 'Enabled'
    managedVirtualNetwork: 'default'
    sqlAdministratorLogin: synapseSqlAdminLogin
    sqlAdministratorLoginPassword: synapseSqlAdminPassword
  }
}

resource synapseAllowAzureServices 'Microsoft.Synapse/workspaces/firewallRules@2021-06-01' = {
  parent: synapseWorkspace
  name: 'AllowAllWindowsAzureIps'
  properties: {
    startIpAddress: '0.0.0.0'
    endIpAddress: '0.0.0.0'
  }
}

resource synapseStorageRole 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(storageAccount.id, synapseWorkspace.id, 'Storage Blob Data Contributor')
  scope: storageAccount
  properties: {
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      'ba92f5b4-2d11-453d-a403-e96b0029c9fe'
    )
    principalId: synapseWorkspace.identity.principalId
    principalType: 'ServicePrincipal'
  }
}
resource keyVault 'Microsoft.KeyVault/vaults@2023-07-01' = {
  name: keyVaultName
  location: location
  tags: commonTags
  properties: {
    tenantId: subscription().tenantId
    sku: {
      family: 'A'
      name: 'standard'
    }
    enableRbacAuthorization: true
  }
}

resource logAnalytics 'Microsoft.OperationalInsights/workspaces@2023-09-01' = {
  name: logAnalyticsName
  location: location
  tags: commonTags
  properties: {
    sku: {
      name: 'PerGB2018'
    }
    retentionInDays: 30
  }
}

resource adfStorageRole 'Microsoft.Authorization/roleAssignments@2022-04-01' = {
  name: guid(storageAccount.id, dataFactory.id, 'Storage Blob Data Contributor')
  scope: storageAccount
  properties: {
    roleDefinitionId: subscriptionResourceId(
      'Microsoft.Authorization/roleDefinitions',
      'ba92f5b4-2d11-453d-a403-e96b0029c9fe'
    )
    principalId: dataFactory.identity.principalId
    principalType: 'ServicePrincipal'
  }
}

output storageAccountName string = storageAccount.name
output dataFactoryName string = dataFactory.name
output databricksWorkspaceName string = databricks.name
output keyVaultName string = keyVault.name
output logAnalyticsWorkspaceName string = logAnalytics.name
output synapseWorkspaceName string = synapseWorkspace.name
