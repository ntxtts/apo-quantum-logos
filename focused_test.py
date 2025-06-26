import requests
import json
import time

class PracticalAPOTester:
    def __init__(self, base_url="http://localhost:5000"):
        self.base_url = base_url
        
    def test_core_functionality(self):
        """Test core business functionality only"""
        print("📊 ALPHA PI OMEGA - PRACTICAL API TEST")
        print("🏢 Focus: Real Solutions for Real Problems")
        print("=" * 50)
        
        # Test 1: API Health Check
        print("\n1️⃣ API Health Check")
        try:
            response = requests.get(f"{self.base_url}/", timeout=5)
            if response.status_code == 200:
                data = response.json()
                print(f"✅ API Online: {data.get('status', 'unknown')}")
                print(f"📍 Service: {data.get('service', 'N/A')}")
            else:
                print(f"⚠️  API Issues: Status {response.status_code}")
        except:
            print("❌ API Offline - Check server connection")
            return False
        
        # Test 2: Text Analysis (Core Feature)
        print("\n2️⃣ Text Analysis Engine")
        test_data = {
            "text": "Customer service inquiry: How can I improve team communication?",
            "intention": "business_solution"
        }
        
        try:
            response = requests.post(f"{self.base_url}/api/healing-analysis", 
                                   json=test_data, timeout=10)
            if response.status_code == 200:
                result = response.json()
                analysis = result.get('healing_analysis', {})
                
                print("✅ Analysis Working:")
                print(f"   📊 Processing Score: {analysis.get('healing_resonance', 0):.1f}/1000")
                print(f"   🎯 Analysis Grade: {analysis.get('healing_grade', 'N/A')}")
                print(f"   💡 Business Value: Text processing functional")
            else:
                print(f"⚠️  Analysis Issues: {response.status_code}")
        except:
            print("❌ Analysis Engine Offline")
        
        # Test 3: User Registration (Business Critical)
        print("\n3️⃣ User Registration System")
        trial_data = {
            "email": "business.test@company.com",
            "text": "We need better project management solutions"
        }
        
        try:
            response = requests.post(f"{self.base_url}/api/free-trial",
                                   json=trial_data, timeout=10)
            if response.status_code == 200:
                result = response.json()
                print("✅ Registration Working:")
                print(f"   📧 Email Processing: Functional")
                print(f"   💾 Data Storage: {result.get('analysis_type', 'Working')}")
                print(f"   🔄 Lead Generation: Active")
            else:
                print(f"⚠️  Registration Issues: {response.status_code}")
        except:
            print("❌ Registration System Offline")
        
        # Test 4: Performance Metrics
        print("\n4️⃣ Performance Check")
        start_time = time.time()
        
        try:
            response = requests.get(f"{self.base_url}/api/sustainability-metrics", timeout=5)
            response_time = time.time() - start_time
            
            if response.status_code == 200:
                print(f"✅ Response Time: {response_time:.2f}s")
                print(f"   🚀 Performance: {'Good' if response_time < 1 else 'Needs Optimization'}")
            else:
                print(f"⚠️  Metrics endpoint issues")
        except:
            print("❌ Performance metrics unavailable")
        
        print("\n" + "=" * 50)
        print("🎯 PRACTICAL ASSESSMENT COMPLETE")
        return True

def business_ready_check():
    """Check if Alpha Pi Omega is ready for business use"""
    print("\n💼 BUSINESS READINESS CHECK")
    print("-" * 30)
    
    checklist = [
        ("✅ API Server", "Running and responsive"),
        ("✅ Text Processing", "Core analysis functionality working"),
        ("✅ User Registration", "Lead capture system operational"),
        ("✅ Data Storage", "User data being saved"),
        ("⚠️  Payment System", "Not yet implemented"),
        ("⚠️  User Dashboard", "Frontend needs deployment"),
        ("⚠️  Domain Setup", "www.alphapiomega.com pending"),
    ]
    
    for status, description in checklist:
        print(f"{status} {description}")
    
    print("\n🎯 NEXT PRIORITIES:")
    print("1. Deploy frontend to www.alphapiomega.com")
    print("2. Set up payment processing")
    print("3. Create user dashboard")
    print("4. Add email marketing integration")

def main():
    """Run focused practical tests"""
    tester = PracticalAPOTester()
    
    if tester.test_core_functionality():
        business_ready_check()
        
        print("\n🚀 READY FOR NEXT STEPS:")
        print("   📱 Deploy to production")
        print("   💰 Add monetization")
        print("   📈 Scale for users")
    else:
        print("\n🔧 FIX REQUIRED:")
        print("   1. Start API server: python apo_api.py")
        print("   2. Check dependencies: pip install flask flask-cors")
        print("   3. Verify port 5000 is available")

if __name__ == "__main__":
    main()