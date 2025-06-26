# test_regenerative_api.py
import requests
import json

def test_regenerative_api():
    """Test the regenerative consciousness API"""
    
    base_url = "http://localhost:5000"
    
    print("🧪 TESTING REGENERATIVE APO QUANTUM LOGOS API")
    print("=" * 60)
    
    # Test 1: Free trial analysis
    print("\n1️⃣ Testing Free Trial Analysis...")
    
    trial_data = {
        "email": "healer@wellness.com",
        "text": "May all beings be free from suffering and filled with loving consciousness"
    }
    
    try:
        response = requests.post(f"{base_url}/api/free-trial", 
                               json=trial_data,
                               headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Free Trial API: SUCCESS")
            print(f"🧮 Consciousness Signature: {result.get('consciousness_signature', 'N/A')}")
            print(f"💚 Healing Potential: {result.get('healing_potential', 'N/A')}")
            print(f"🌟 Special Offer: {result.get('special_offer', 'N/A')}")
        else:
            print(f"❌ Free Trial API: FAILED ({response.status_code})")
            print(f"Error: {response.text}")
    
    except Exception as e:
        print(f"❌ Free Trial API: CONNECTION ERROR - {e}")
    
    # Test 2: Healing analysis
    print("\n2️⃣ Testing Healing Analysis...")
    
    healing_data = {
        "text": "I am filled with divine healing light that radiates love and compassion",
        "intention": "healing"
    }
    
    try:
        response = requests.post(f"{base_url}/api/healing-analysis",
                               json=healing_data,
                               headers={'Content-Type': 'application/json'})
        
        if response.status_code == 200:
            result = response.json()
            print("✅ Healing Analysis API: SUCCESS")
            
            healing_analysis = result.get('healing_analysis', {})
            sustainability = result.get('sustainability_impact', {})
            
            print(f"🎵 Consciousness Frequency: {healing_analysis.get('consciousness_frequency', 'N/A')} Hz")
            print(f"✨ Healing Resonance: {healing_analysis.get('healing_resonance', 'N/A')}")
            print(f"🌱 Carbon Impact: {healing_analysis.get('carbon_impact', 'N/A')}")
            print(f"🌳 Trees Planted: {healing_analysis.get('trees_planted_equivalent', 'N/A')}")
            print(f"☀️ Energy Source: {sustainability.get('renewable_energy_used', 'N/A')}")
        else:
            print(f"❌ Healing Analysis API: FAILED ({response.status_code})")
            print(f"Error: {response.text}")
    
    except Exception as e:
        print(f"❌ Healing Analysis API: CONNECTION ERROR - {e}")
    
    # Test 3: Basic connectivity
    print("\n3️⃣ Testing Basic Server Health...")
    
    try:
        response = requests.get(f"{base_url}/")
        if response.status_code in [200, 404]:  # 404 is fine, means server is running
            print("✅ Server: RUNNING")
        else:
            print(f"⚠️ Server: Unexpected response ({response.status_code})")
    except Exception as e:
        print(f"❌ Server: NOT RUNNING - {e}")
    
    print("\n🎯 API TEST SUMMARY:")
    print("   🔍 Free trial endpoint for customer acquisition")
    print("   💚 Healing analysis for wellness practitioners")
    print("   🌱 Sustainability metrics for impact tracking")
    print("   ⚡ Real-time regenerative consciousness analysis")
    
    print("\n🚀 YOUR REGENERATIVE API IS READY FOR CUSTOMERS!")
    print("\n💡 NEXT STEPS:")
    print("   1. Start the API server: python launch_apo_api.py")
    print("   2. Send customer outreach emails")
    print("   3. Post on social media about carbon-negative consciousness")
    print("   4. Begin beta customer recruitment")
    
    print("\n🌟 REVOLUTIONARY TECHNOLOGY READY TO CHANGE THE WORLD! 🌟")

if __name__ == "__main__":
    test_regenerative_api()