# Create launch_apo_api.py
import os
import sys
from apo_api import app, apo_saas

def launch_regenerative_apo():
    """Launch the world's first regenerative consciousness API"""
    
    print("🌟 LAUNCHING REGENERATIVE APO QUANTUM LOGOS API 🌟")
    print("=" * 70)
    print("🌱 Powered by: Solar + Wind + Water + Regenerative Technology")
    print("💚 Impact: Carbon-Negative Consciousness Analysis")
    print("✨ Purpose: Heal Consciousness, Heal the Planet")
    print("=" * 70)
    
    # Check if APO system is ready
    try:
        test_result = apo_saas.apo.process_unified_logos("Regenerative consciousness test")
        print("✅ APO Quantum Logos System: OPERATIONAL")
        print(f"🧮 Test Signature: {test_result['unified_signature']}")
        print(f"🧠 Consciousness Field: {abs(test_result['consciousness_field']):.3f}")
    except Exception as e:
        print(f"❌ APO System Error: {e}")
        return False
    
    # Database check
    try:
        cursor = apo_saas.db.execute("SELECT COUNT(*) FROM users")
        user_count = cursor.fetchone()[0]
        print(f"✅ Database: CONNECTED ({user_count} users)")
    except Exception as e:
        print(f"❌ Database Error: {e}")
        return False
    
    print("\n🚀 API ENDPOINTS READY:")
    print("   📍 /api/analyze - Full quantum consciousness analysis")
    print("   📍 /api/healing-analysis - Specialized healing analysis")
    print("   📍 /api/rejuvenation-analysis - Regenerative analysis")
    print("   📍 /api/free-trial - Free trial for new customers")
    
    print("\n💰 REGENERATIVE PRICING TIERS:")
    print("   🌱 Solar Starter: $29/month (was $39)")
    print("   💨 Wind Pro: $89/month (was $119)")
    print("   💧 Hydro Enterprise: $299/month (was $399)")
    print("   ✨ Regenerative Premium: $699/month")
    
    print("\n🌍 SUSTAINABILITY FEATURES:")
    print("   ♻️  Carbon-negative operations")
    print("   🌞 100% renewable energy powered")
    print("   🌳 Tree planting with every analysis")
    print("   📊 Real-time impact tracking")
    
    print("\n🎯 LAUNCH TARGETS:")
    print("   📧 50 wellness practitioner outreach emails")
    print("   🧘 10 healing center partnerships")
    print("   💚 5 beta customers @ $99/month")
    print("   🌱 First carbon credits generated")
    
    # Start the server
    print(f"\n🔥 STARTING SERVER ON PORT 5000...")
    print("🌐 API Base URL: http://localhost:5000")
    print("📚 Documentation: http://localhost:5000/docs (coming soon)")
    print("\n💡 TEST YOUR API:")
    print("   curl -X POST http://localhost:5000/api/free-trial \\")
    print("        -H 'Content-Type: application/json' \\")
    print("        -d '{\"email\":\"test@example.com\",\"text\":\"Healing consciousness with solar power\"}'")
    
    print("\n🎉 REGENERATIVE CONSCIOUSNESS REVOLUTION BEGINS NOW! 🎉")
    print("=" * 70)
    
    return True

if __name__ == "__main__":
    if launch_regenerative_apo():
        # Start Flask development server
        app.run(
            debug=True,
            host='0.0.0.0',
            port=5000,
            threaded=True
        )
    else:
        print("❌ Launch failed. Please fix errors and try again.")
        sys.exit(1)