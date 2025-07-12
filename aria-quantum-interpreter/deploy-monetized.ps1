# Deploy ASTRO Quantum System to Azure
# Run this script to deploy your monetized quantum platform

param(
    [string]$FunctionAppName = "astro-quantum-system",
    [string]$ResourceGroup = "ASTRO-Quantum-RG_group", 
    [string]$Location = "East US",
    [string]$StorageAccount = "astroquantumstorage"
)

Write-Host "🚀 Deploying ASTRO Quantum System for Monetization (Alpha Pi Omega Corp, paulm@alphapiomega.com)..." -ForegroundColor Green

# Check if Azure CLI is installed and logged in
try {
    $account = az account show --query "name" -o tsv
    Write-Host "✅ Logged in to Azure as: $account" -ForegroundColor Green
} catch {
    Write-Host "❌ Please install Azure CLI and login with 'az login'" -ForegroundColor Red
    exit 1
}

# Check if Functions Core Tools is installed
try {
    $funcVersion = func --version
    Write-Host "✅ Azure Functions Core Tools version: $funcVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ Please install Azure Functions Core Tools" -ForegroundColor Red
    Write-Host "Install via: npm install -g azure-functions-core-tools@4" -ForegroundColor Yellow
    exit 1
}

# Create resource group
Write-Host "📦 Creating resource group..." -ForegroundColor Yellow
az group create --name $ResourceGroup --location $Location

# Create storage account
Write-Host "💾 Creating storage account..." -ForegroundColor Yellow
az storage account create --name $StorageAccount --resource-group $ResourceGroup --location $Location --sku Standard_LRS

# Create Function App
Write-Host "⚡ Creating Function App..." -ForegroundColor Yellow
az functionapp create --resource-group $ResourceGroup --consumption-plan-location $Location --runtime python --runtime-version 3.11 --functions-version 4 --name $FunctionAppName --storage-account $StorageAccount

# Deploy the function
Write-Host "🚀 Deploying your monetized quantum function..." -ForegroundColor Yellow
func azure functionapp publish $FunctionAppName

# Get the function URL
$functionUrl = az functionapp show --name $FunctionAppName --resource-group $ResourceGroup --query "defaultHostName" -o tsv

Write-Host ""
Write-Host "🎉 DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "================================" -ForegroundColor Green
Write-Host ""
Write-Host "📍 Your ASTRO Quantum System (Alpha Pi Omega Corp) is live at:" -ForegroundColor Cyan
Write-Host "   https://$functionUrl" -ForegroundColor White
Write-Host ""
Write-Host "💰 Monetization Endpoints (Alpha Pi Omega Corp):" -ForegroundColor Yellow
Write-Host "   • Get API Keys: https://$functionUrl/api/getApiKey" -ForegroundColor White
Write-Host "   • User Dashboard: https://$functionUrl/api/dashboard" -ForegroundColor White
Write-Host "   • Quantum Operations: https://$functionUrl/api/runAria" -ForegroundColor White
Write-Host "   • Revenue Analytics: https://$functionUrl/api/revenue" -ForegroundColor White
Write-Host "   • Pricing Info: https://$functionUrl/api/pricing" -ForegroundColor White
Write-Host ""
Write-Host "🧪 Test Your API Now (Alpha Pi Omega Corp):" -ForegroundColor Yellow
Write-Host "   curl `\"https://$functionUrl/api/getApiKey`\"" -ForegroundColor White
Write-Host ""
Write-Host "💸 Start making money immediately! (Alpha Pi Omega Corp, Contact: paulm@alphapiomega.com)" -ForegroundColor Green
Write-Host "   1. Get API keys from the endpoint above" -ForegroundColor White
Write-Host "   2. Update pricing_dashboard.html with your URL" -ForegroundColor White
Write-Host "   3. Host the dashboard on Netlify/Vercel" -ForegroundColor White
Write-Host "   4. Share your quantum platform with the world!" -ForegroundColor White
Write-Host ""

# Test the deployment
Write-Host "🧪 Testing deployment..." -ForegroundColor Yellow
try {
    $response = Invoke-RestMethod -Uri "https://$functionUrl/api/getApiKey" -Method GET
    Write-Host "✅ API test successful! Your system is ready for monetization." -ForegroundColor Green
    
    # Display sample API keys
    Write-Host ""
    Write-Host "🔑 Sample API Keys Generated:" -ForegroundColor Cyan
    $response.demo_keys.PSObject.Properties | ForEach-Object {
        Write-Host "   $($_.Name): $($_.Value)" -ForegroundColor White
    }
    
} catch {
    Write-Host "⚠️  Deployment completed but API test failed. Check Azure portal for details." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "📊 Next Steps (Alpha Pi Omega Corp):" -ForegroundColor Magenta
Write-Host "   1. Open Azure portal to monitor your function" -ForegroundColor White
Write-Host "   2. Set up Azure Front Door CDN for global performance & security" -ForegroundColor White
Write-Host "   3. Set up custom domain and SSL" -ForegroundColor White  
Write-Host "   4. Configure Stripe for payment processing" -ForegroundColor White
Write-Host "   5. Launch marketing campaigns" -ForegroundColor White
Write-Host ""
Write-Host "� To enable Azure Front Door, see the script section below or use the Azure Portal." -ForegroundColor Yellow
Write-Host ""
Write-Host "�💰 Target: $10K MRR in 90 days! Start selling now! (Alpha Pi Omega Corp, Contact: paulm@alphapiomega.com)" -ForegroundColor Green

# ================= Azure Front Door Integration (Manual Step) =================
Write-Host "" -ForegroundColor DarkGray
Write-Host "# To set up Azure Front Door for your Function App, run these commands after deployment:" -ForegroundColor Cyan
Write-Host "# (Replace names as needed. See Azure Portal for more options.)" -ForegroundColor Cyan
Write-Host "" -ForegroundColor DarkGray
Write-Host "# az network front-door profile create --name astro-frontdoor --resource-group $ResourceGroup --sku Standard_AzureFrontDoor --location $Location" -ForegroundColor Gray
Write-Host "# az network front-door endpoint create --resource-group $ResourceGroup --profile-name astro-frontdoor --name astro-endpoint" -ForegroundColor Gray
Write-Host "# az network front-door origin-group create --resource-group $ResourceGroup --profile-name astro-frontdoor --name astro-origingroup" -ForegroundColor Gray
Write-Host "# az network front-door origin create --resource-group $ResourceGroup --profile-name astro-frontdoor --origin-group-name astro-origingroup --name astro-function-origin --host-name $functionUrl --priority 1 --weight 1000 --enabled-state Enabled" -ForegroundColor Gray
Write-Host "# az network front-door route create --resource-group $ResourceGroup --profile-name astro-frontdoor --endpoint-name astro-endpoint --name astro-route --origin-group astro-origingroup --route-type Forward --https-redirect Enabled --patterns-to-match /*" -ForegroundColor Gray
Write-Host "" -ForegroundColor DarkGray
Write-Host "# After setup, update your DNS to point your custom domain to the Front Door endpoint." -ForegroundColor Cyan
Write-Host "# Enable HTTPS in the Azure Portal for your custom domain (Azure-managed certificate recommended)." -ForegroundColor Cyan
Write-Host "" -ForegroundColor DarkGray
