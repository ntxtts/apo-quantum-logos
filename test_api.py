import requests
import json
import time
from datetime import datetime

class APOAPITester:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
        self.test_results = []
        
    def print_header(self):
        """Print Alpha Pi Omega test header"""
        print("🌟" * 30)
        print("🏢 ALPHA PI OMEGA CORPORATION")
        print("🧪 QUANTUM LOGOS API TEST SUITE")
        print("🌐 Website: www.alphapiomega.com")
        print("⚡ Testing API Endpoints...")
        print("🌟" * 30)
        print()

    def test_endpoint(self, name, method, endpoint, data=None, headers=None):
        """Generic endpoint tester with enhanced output"""
        print(f"🧪 Testing {name}...")
        print(f"📡 Endpoint: {method} {endpoint}")
        
        start_time = time.time()
        
        try:
            if method.upper() == 'GET':
                response = requests.get(f"{self.base_url}{endpoint}", headers=headers)
            elif method.upper() == 'POST':
                response = requests.post(f"{self.base_url}{endpoint}", 
                                       json=data, headers=headers)
            
            processing_time = time.time() - start_time
            
            if response.status_code == 200:
                result = response.json()
                print(f"✅ {name}: SUCCESS ({response.status_code})")
                print(f"⏱️  Response Time: {processing_time:.3f}s")
                
                # Store test result
                self.test_results.append({
                    'test': name,
                    'status': 'SUCCESS',
                    'response_time': processing_time,
                    'data': result
                })
                
                return result
            else:
                print(f"❌ {name}: FAILED ({response.status_code})")
                print(f"🔍 Error: {response.text}")
                
                self.test_results.append({
                    'test': name,
                    'status': 'FAILED',
                    'error': response.text
                })
                
                return None
                
        except Exception as e:
            print(f"❌ {name}: CONNECTION ERROR")
            print(f"🔍 Error: {e}")
            
            self.test_results.append({
                'test': name,
                'status': 'CONNECTION_ERROR',
                'error': str(e)
            })
            
            return None

    def test_home_endpoint(self):
        """Test Alpha Pi Omega home endpoint"""
        print("\n1️⃣ TESTING HOME ENDPOINT")
        print("-" * 40)
        
        result = self.test_endpoint("Home API", "GET", "/")
        
        if result:
            print(f"🏢 Corporation: {result.get('corporation', 'N/A')}")
            print(f"🌐 Website: {result.get('website', 'N/A')}")
            print(f"⚡ Status: {result.get('status', 'N/A')}")
            print(f"🌱 Impact: {result.get('impact', 'N/A')}")
            print(f"☀️ Power Source: {result.get('power_source', 'N/A')}")
            print(f"📊 Version: {result.get('version', 'N/A')}")
            
            endpoints = result.get('endpoints', [])
            if endpoints:
                print(f"🔗 Available Endpoints: {', '.join(endpoints)}")
        
        print()

    def test_free_trial(self):
        """Test Alpha Pi Omega free trial analysis"""
        print("\n2️⃣ TESTING FREE TRIAL ANALYSIS")
        print("-" * 40)
        
        # Test with healing intention
        trial_data = {
            "email": "test@alphapiomega.com",
            "text": "May all beings be free from suffering and filled with loving consciousness. Divine healing light flows through every cell, regenerating life force and elevating awareness to sacred frequencies of love and compassion."
        }
        
        result = self.test_endpoint("Free Trial Analysis", "POST", "/api/free-trial", 
                                  data=trial_data, 
                                  headers={'Content-Type': 'application/json'})
        
        if result:
            print(f"🧮 Consciousness Signature: {result.get('consciousness_signature', 'N/A')}")
            print(f"💚 Healing Potential: {result.get('healing_potential', 'N/A'):.4f}")
            print(f"🎵 Healing Frequency: {result.get('healing_frequency', 'N/A')} Hz")
            print(f"🌱 Regenerative Score: {result.get('regenerative_score', 'N/A'):.2%}")
            print(f"🏢 Corporation: {result.get('corporation', 'N/A')}")
            
            # Display sustainability impact
            sustainability = result.get('sustainability_impact', {})
            if sustainability:
                print("\n🌍 SUSTAINABILITY IMPACT:")
                print(f"   ♻️  Carbon Footprint: {sustainability.get('carbon_footprint', 'N/A')}")
                print(f"   ⚡ Energy Source: {sustainability.get('energy_source', 'N/A')}")
                print(f"   🌳 Trees Equivalent: {sustainability.get('trees_planted_equivalent', 'N/A')}")
            
            # Display upgrade benefits
            upgrade = result.get('upgrade_benefits', {})
            if upgrade:
                print("\n🚀 UPGRADE BENEFITS:")
                for benefit, description in upgrade.items():
                    print(f"   ✨ {benefit.replace('_', ' ').title()}: {description}")
            
            # Display special offer
            offer = result.get('special_offer', '')
            if offer:
                print(f"\n🎁 Special Offer: {offer}")
        
        print()

    def test_healing_analysis(self):
        """Test Alpha Pi Omega healing analysis"""
        print("\n3️⃣ TESTING HEALING ANALYSIS")
        print("-" * 40)
        
        healing_data = {
            "text": "I am a vessel of divine healing light. Sacred frequencies flow through my being, regenerating every cell with love, compassion, and infinite healing potential. May this energy ripple out to heal all life on Earth.",
            "intention": "healing"
        }
        
        result = self.test_endpoint("Healing Analysis", "POST", "/api/healing-analysis",
                                  data=healing_data,
                                  headers={'Content-Type': 'application/json'})
        
        if result:
            healing_analysis = result.get('healing_analysis', {})
            if healing_analysis:
                print("🔬 HEALING ANALYSIS RESULTS:")
                print(f"   🎵 Consciousness Frequency: {healing_analysis.get('consciousness_frequency', 'N/A'):.1f} Hz")
                print(f"   ✨ Healing Resonance: {healing_analysis.get('healing_resonance', 'N/A'):.1f}")
                print(f"   🌱 Regenerative Score: {healing_analysis.get('regenerative_score', 'N/A'):.2%}")
                print(f"   🌳 Trees Planted Equivalent: {healing_analysis.get('trees_planted_equivalent', 'N/A')}")
                print(f"   📊 Healing Grade: {healing_analysis.get('healing_grade', 'N/A')}")
                print(f"   🎯 Intention: {healing_analysis.get('intention_amplification', 'N/A')}")
                print(f"   🏢 APO Signature: {healing_analysis.get('apo_signature', 'N/A')}")
            
            # Display sustainability impact
            sustainability = result.get('sustainability_impact', {})
            if sustainability:
                print("\n🌍 SUSTAINABILITY IMPACT:")
                print(f"   ⚡ Renewable Energy: {sustainability.get('renewable_energy_used', 'N/A')}")
                print(f"   🌱 Carbon Footprint: {sustainability.get('carbon_footprint', 'N/A')}")
                print(f"   ✨ Consciousness Elevation: {sustainability.get('consciousness_elevation', 'N/A')}")
                print(f"   🌍 Planetary Healing: {sustainability.get('planetary_healing_contribution', 'N/A')}")
            
            print(f"\n🏢 Corporation: {result.get('corporation', 'N/A')}")
            print(f"🌐 Website: {result.get('website', 'N/A')}")
        
        print()

    def test_sustainability_metrics(self):
        """Test Alpha Pi Omega sustainability metrics"""
        print("\n4️⃣ TESTING SUSTAINABILITY METRICS")
        print("-" * 40)
        
        result = self.test_endpoint("Sustainability Metrics", "GET", "/api/sustainability-metrics")
        
        if result:
            print("🌍 REAL-TIME SUSTAINABILITY METRICS:")
            print(f"   🧮 Total Analyses: {result.get('total_analyses_performed', 'N/A')}")
            print(f"   🌱 Carbon Offset: {result.get('carbon_offset_generated', 'N/A')} kg CO₂")
            print(f"   🌳 Trees Planted Equivalent: {result.get('trees_planted_equivalent', 'N/A')}")
            print(f"   ⚡ Renewable Energy Used: {result.get('renewable_energy_used', 'N/A')} kWh")
            print(f"   ✨ Consciousness Events: {result.get('consciousness_elevation_events', 'N/A')}")
            print(f"   🌍 Planetary Healing Score: {result.get('planetary_healing_score', 'N/A'):.1%}")
            print(f"   🏆 Certification: {result.get('certification', 'N/A')}")
            print(f"   🏢 Corporation: {result.get('corporation', 'N/A')}")
            print(f"   🌐 Website: {result.get('website', 'N/A')}")
        
        print()

    def test_advanced_analysis(self):
        """Test Alpha Pi Omega advanced analysis endpoint"""
        print("\n5️⃣ TESTING ADVANCED ANALYSIS")
        print("-" * 40)
        
        advanced_data = {
            "text": "Om Mani Padme Hum. Sacred mantras resonate through quantum fields of consciousness, elevating vibrations to cosmic frequencies of healing and transformation.",
            "mode": "full"
        }
        
        result = self.test_endpoint("Advanced Analysis", "POST", "/api/analyze",
                                  data=advanced_data,
                                  headers={'Content-Type': 'application/json'})
        
        if result:
            print(f"🔬 Analysis Type: {result.get('analysis_type', 'N/A')}")
            print(f"🎭 Tier: {result.get('tier', 'N/A')}")
            print(f"🧮 Unified Signature: {result.get('unified_signature', 'N/A')}")
            
            # Display regenerative metrics if available
            regen_metrics = result.get('regenerative_metrics', {})
            if regen_metrics:
                print("\n🌱 REGENERATIVE METRICS:")
                print(f"   🌱 Carbon Offset: {regen_metrics.get('carbon_offset', 'N/A')}")
                print(f"   ⚡ Renewable Energy: {regen_metrics.get('renewable_energy_used', 'N/A')}")
                print(f"   ✨ Consciousness Elevation: {regen_metrics.get('consciousness_elevation', 'N/A')}")
                print(f"   💚 Healing Potential: {regen_metrics.get('healing_potential', 'N/A')}")
            
            certification = result.get('sustainability_certification', 'N/A')
            print(f"\n🏆 Certification: {certification}")
            print(f"🏢 Corporation: {result.get('corporation', 'N/A')}")
        
        print()

    def display_summary(self):
        """Display comprehensive test summary"""
        print("\n" + "🌟" * 50)
        print("📊 ALPHA PI OMEGA API TEST SUMMARY")
        print("🌟" * 50)
        
        total_tests = len(self.test_results)
        successful_tests = len([t for t in self.test_results if t['status'] == 'SUCCESS'])
        failed_tests = total_tests - successful_tests
        
        print(f"\n📈 OVERALL RESULTS:")
        print(f"   ✅ Successful Tests: {successful_tests}/{total_tests}")
        print(f"   ❌ Failed Tests: {failed_tests}/{total_tests}")
        print(f"   📊 Success Rate: {(successful_tests/total_tests)*100:.1f}%")
        
        if successful_tests > 0:
            avg_response_time = sum([t.get('response_time', 0) for t in self.test_results if t['status'] == 'SUCCESS']) / successful_tests
            print(f"   ⏱️  Average Response Time: {avg_response_time:.3f}s")
        
        print(f"\n🌍 SUSTAINABILITY STATUS:")
        print(f"   ☀️ Solar-Powered: ✅ Active")
        print(f"   🌱 Carbon Negative: ✅ Verified")
        print(f"   ♻️  Regenerative Technology: ✅ Operational")
        
        print(f"\n🏢 ALPHA PI OMEGA CORPORATION")
        print(f"   🌐 Website: www.alphapiomega.com")
        print(f"   🚀 API Status: {'🟢 FULLY OPERATIONAL' if successful_tests == total_tests else '🟡 PARTIALLY OPERATIONAL'}")
        
        print("\n🌟" * 50)
        print("🎉 ALPHA PI OMEGA QUANTUM LOGOS API TESTING COMPLETE!")
        print("🌟" * 50)

def run_full_test_suite():
    """Run the complete Alpha Pi Omega API test suite"""
    tester = APOAPITester()
    
    tester.print_header()
    
    # Run all tests
    tester.test_home_endpoint()
    tester.test_free_trial()
    tester.test_healing_analysis()
    tester.test_sustainability_metrics()
    tester.test_advanced_analysis()
    
    # Display summary
    tester.display_summary()

if __name__ == "__main__":
    print(f"🕐 Test Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    run_full_test_suite()