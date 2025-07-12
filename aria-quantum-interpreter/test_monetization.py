#!/usr/bin/env python3
"""
Test script for ASTRO Quantum System monetization
Alpha Pi Omega Corp - Paul M. (paulm@alphapiomega.com)
"""

import requests
import json
import time

class ASTROMonetizationTester:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip('/')
        self.api_keys = {}
    
    def test_get_api_key(self, tier: str = "free"):
        """Test API key generation"""
        print(f"🔑 Testing API key generation for {tier} tier...")
        
        response = requests.get(f"{self.base_url}/api/getApiKey?tier={tier}")
        
        if response.status_code == 200:
            data = response.json()
            api_key = data["api_key"]
            self.api_keys[tier] = api_key
            print(f"✅ Got API key: {api_key[:20]}...")
            return api_key
        else:
            print(f"❌ Failed to get API key: {response.status_code}")
            return None
    
    def test_pricing_endpoint(self):
        """Test public pricing endpoint"""
        print("💰 Testing pricing endpoint...")
        
        response = requests.get(f"{self.base_url}/api/pricing")
        
        if response.status_code == 200:
            data = response.json()
            company = data.get("company", {})
            if company.get("company") == "Alpha Pi Omega Corp":
                print("✅ Pricing endpoint working - Alpha Pi Omega Corp verified")
                return True
            else:
                print("❌ Company info not found")
        else:
            print(f"❌ Pricing endpoint failed: {response.status_code}")
        
        return False
    
    def test_quantum_operation(self, tier: str = "free"):
        """Test quantum operation with billing"""
        if tier not in self.api_keys:
            self.test_get_api_key(tier)
        
        api_key = self.api_keys.get(tier)
        if not api_key:
            print(f"❌ No API key for {tier} tier")
            return False
        
        print(f"⚛️ Testing quantum operation with {tier} tier...")
        
        headers = {"X-API-Key": api_key}
        params = {"command": "quantum entangle 2"}
        
        response = requests.get(f"{self.base_url}/api/runAria", headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            billing = data.get("billing", {})
            print(f"✅ Quantum operation successful - Cost: ${billing.get('cost', 0)}")
            return True
        else:
            print(f"❌ Quantum operation failed: {response.status_code}")
            if response.status_code == 401:
                print("   Authentication issue")
            elif response.status_code == 429:
                print("   Rate limit exceeded")
        
        return False
    
    def test_dashboard(self, tier: str = "free"):
        """Test user dashboard"""
        if tier not in self.api_keys:
            self.test_get_api_key(tier)
        
        api_key = self.api_keys.get(tier)
        if not api_key:
            return False
        
        print(f"📊 Testing dashboard for {tier} tier...")
        
        headers = {"X-API-Key": api_key}
        response = requests.get(f"{self.base_url}/api/dashboard", headers=headers)
        
        if response.status_code == 200:
            data = response.json()
            usage = data.get("usage", {})
            print(f"✅ Dashboard working - Operations used: {usage.get('operations_used', 0)}")
            return True
        else:
            print(f"❌ Dashboard failed: {response.status_code}")
        
        return False
    
    def run_full_test(self):
        """Run complete monetization test suite"""
        print("🚀 Starting ASTRO Quantum System Monetization Tests")
        print("=" * 60)
        
        results = {
            "pricing": self.test_pricing_endpoint(),
            "api_key_free": self.test_get_api_key("free"),
            "api_key_starter": self.test_get_api_key("starter"),
            "quantum_operation": self.test_quantum_operation("free"),
            "dashboard": self.test_dashboard("free"),
        }
        
        print("\n" + "=" * 60)
        print("📋 Test Results Summary:")
        
        for test_name, result in results.items():
            status = "✅ PASS" if result else "❌ FAIL"
            print(f"  {test_name}: {status}")
        
        all_passed = all(results.values())
        
        if all_passed:
            print("\n🎉 All tests passed! Monetization system is ready for production.")
            print("💰 Start marketing and selling immediately!")
        else:
            print("\n⚠️ Some tests failed. Check configuration and try again.")
        
        print(f"\nAlpha Pi Omega Corp - Contact: paulm@alphapiomega.com")
        
        return all_passed

if __name__ == "__main__":
    # Replace with your actual Azure Function URL
    BASE_URL = "https://your-function-app-name.azurewebsites.net"
    
    print("ASTRO Quantum System - Monetization Test Suite")
    print("Alpha Pi Omega Corp")
    print(f"Testing URL: {BASE_URL}")
    print()
    
    tester = ASTROMonetizationTester(BASE_URL)
    tester.run_full_test()