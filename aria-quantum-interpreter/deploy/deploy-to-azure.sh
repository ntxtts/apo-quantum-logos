#!/bin/bash

# Aria Quantum Azure Deployment Script
# This script deploys the complete Aria Quantum environment to Azure

set -e

# Configuration
RESOURCE_GROUP="aria-quantum-rg"
LOCATION="East US 2"
FUNCTION_APP_NAME="aria-quantum-interpreter"
SUBSCRIPTION_ID=""

echo "🚀 Starting Aria Quantum Azure Deployment..."

# Check if Azure CLI is installed
if ! command -v az &> /dev/null; then
    echo "❌ Azure CLI is not installed. Please install it first."
    exit 1
fi

# Login to Azure (if not already logged in)
echo "🔐 Checking Azure login status..."
if ! az account show &> /dev/null; then
    echo "Please login to Azure..."
    az login
fi

# Set subscription (if provided)
if [ ! -z "$SUBSCRIPTION_ID" ]; then
    echo "📋 Setting Azure subscription..."
    az account set --subscription "$SUBSCRIPTION_ID"
fi

# Create resource group
echo "📦 Creating resource group..."
az group create \
    --name "$RESOURCE_GROUP" \
    --location "$LOCATION"

# Deploy infrastructure
echo "🏗️ Deploying Azure infrastructure..."
az deployment group create \
    --resource-group "$RESOURCE_GROUP" \
    --template-file deploy/azure-infrastructure.json \
    --parameters functionAppName="$FUNCTION_APP_NAME"

# Get function app details
FUNCTION_APP_URL=$(az functionapp show \
    --name "$FUNCTION_APP_NAME" \
    --resource-group "$RESOURCE_GROUP" \
    --query "defaultHostName" -o tsv)

echo "✅ Infrastructure deployed successfully!"
echo "🌐 Function App URL: https://$FUNCTION_APP_URL"

# Deploy function code
echo "📤 Deploying function code..."
func azure functionapp publish "$FUNCTION_APP_NAME" --python

echo "🎉 Aria Quantum Azure environment deployed successfully!"
echo ""
echo "📋 Deployment Summary:"
echo "  - Resource Group: $RESOURCE_GROUP"
echo "  - Function App: $FUNCTION_APP_NAME"
echo "  - URL: https://$FUNCTION_APP_URL"
echo ""
echo "🧪 Test endpoints:"
echo "  - Main Interpreter: https://$FUNCTION_APP_URL/api/runAria"
echo "  - Circuit Builder: https://$FUNCTION_APP_URL/api/quantumCircuit"
echo "  - State Analyzer: https://$FUNCTION_APP_URL/api/quantumState"
echo "  - Algorithms: https://$FUNCTION_APP_URL/api/ariaAlgorithms"
echo "  - Storage: https://$FUNCTION_APP_URL/api/ariaStorage"
