# Aria Quantum Azure Deployment Script (PowerShell)
# This script deploys the complete Aria Quantum environment to Azure

param(
    [Parameter(Mandatory=$false)]
    [string]$ResourceGroupName = "aria-quantum-rg",
    
    [Parameter(Mandatory=$false)]
    [string]$Location = "East US 2",
    
    [Parameter(Mandatory=$false)]
    [string]$FunctionAppName = "aria-quantum-interpreter",
    
    [Parameter(Mandatory=$false)]
    [string]$SubscriptionId = ""
)

Write-Host "🚀 Starting Aria Quantum Azure Deployment..." -ForegroundColor Green

# Check if Azure CLI is installed
try {
    az --version | Out-Null
} catch {
    Write-Host "❌ Azure CLI is not installed. Please install it first." -ForegroundColor Red
    exit 1
}

# Login to Azure (if not already logged in)
Write-Host "🔐 Checking Azure login status..." -ForegroundColor Yellow
try {
    az account show | Out-Null
} catch {
    Write-Host "Please login to Azure..." -ForegroundColor Yellow
    az login
}

# Set subscription (if provided)
if ($SubscriptionId) {
    Write-Host "📋 Setting Azure subscription..." -ForegroundColor Yellow
    az account set --subscription $SubscriptionId
}

# Create resource group
Write-Host "📦 Creating resource group..." -ForegroundColor Yellow
az group create --name $ResourceGroupName --location $Location

# Deploy infrastructure
Write-Host "🏗️ Deploying Azure infrastructure..." -ForegroundColor Yellow
az deployment group create `
    --resource-group $ResourceGroupName `
    --template-file "deploy/azure-infrastructure.json" `
    --parameters functionAppName=$FunctionAppName

# Get function app details
$FunctionAppUrl = az functionapp show `
    --name $FunctionAppName `
    --resource-group $ResourceGroupName `
    --query "defaultHostName" -o tsv

Write-Host "✅ Infrastructure deployed successfully!" -ForegroundColor Green
Write-Host "🌐 Function App URL: https://$FunctionAppUrl" -ForegroundColor Cyan

# Deploy function code
Write-Host "📤 Deploying function code..." -ForegroundColor Yellow
func azure functionapp publish $FunctionAppName --python

Write-Host "🎉 Aria Quantum Azure environment deployed successfully!" -ForegroundColor Green
Write-Host ""
Write-Host "📋 Deployment Summary:" -ForegroundColor Cyan
Write-Host "  - Resource Group: $ResourceGroupName" -ForegroundColor White
Write-Host "  - Function App: $FunctionAppName" -ForegroundColor White
Write-Host "  - URL: https://$FunctionAppUrl" -ForegroundColor White
Write-Host ""
Write-Host "🧪 Test endpoints:" -ForegroundColor Cyan
Write-Host "  - Main Interpreter: https://$FunctionAppUrl/api/runAria" -ForegroundColor White
Write-Host "  - Circuit Builder: https://$FunctionAppUrl/api/quantumCircuit" -ForegroundColor White
Write-Host "  - State Analyzer: https://$FunctionAppUrl/api/quantumState" -ForegroundColor White
Write-Host "  - Algorithms: https://$FunctionAppUrl/api/ariaAlgorithms" -ForegroundColor White
Write-Host "  - Storage: https://$FunctionAppUrl/api/ariaStorage" -ForegroundColor White
