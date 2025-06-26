# Simple APO test
print("🧪 Testing APO Quantum Logos Python System")
print("=" * 50)

try:
    from apo_quantum_logos import UnifiedAPOQuantumLogos
    print("✅ APO import successful")
    
    # Test the system
    apo = UnifiedAPOQuantumLogos()
    print("✅ APO system initialized")
    
    # Test analysis
    test_text = "The Schrödinger equation describes quantum evolution"
    print(f"📝 Testing with: {test_text}")
    
    result = apo.process_unified_logos(test_text)
    print("✅ Analysis complete!")
    print(f"🧮 Unified signature: {result['unified_signature']}")
    print(f"🧠 Consciousness field: {abs(result['consciousness_field']):.3f}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("🎉 APO test complete!")