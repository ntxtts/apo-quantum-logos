# Working test with correct method names
print("🧪 ΑΠΩ Working Test with Correct Methods")
print("=" * 50)

try:
    from apo_quantum_logos import UnifiedAPOQuantumLogos
    print("✅ UnifiedAPOQuantumLogos import successful")
    
    # Test the main class directly
    apo = UnifiedAPOQuantumLogos()
    print("✅ ΑΠΩ system initialized")
    
    # Check what methods are available
    methods = [m for m in dir(apo) if not m.startswith('_') and callable(getattr(apo, m))]
    print(f"📋 Available methods: {len(methods)}")
    
    # Look for the main processing method
    if hasattr(apo, 'process_unified_logos'):
        print("✅ Found process_unified_logos method")
        
        # Test it
        test_text = "The Schrödinger equation describes quantum evolution"
        print(f"\n📝 Testing: {test_text}")
        
        result = apo.process_unified_logos(test_text)
        print("✅ Analysis successful!")
        
        # Display results safely
        print(f"🧮 Result type: {type(result)}")
        
        if isinstance(result, dict):
            print("📊 Result keys:")
            for key in result.keys():
                print(f"  • {key}")
            
            # Try to display main results
            if 'unified_signature' in result:
                print(f"🧮 Unified signature: {result['unified_signature']}")
            
            if 'consciousness_field' in result:
                consciousness = result['consciousness_field']
                if isinstance(consciousness, complex):
                    print(f"🧠 Consciousness field: {abs(consciousness):.3f}")
                else:
                    print(f"🧠 Consciousness field: {consciousness}")
        else:
            print(f"📄 Result: {result}")
    
    elif hasattr(apo, 'analyze'):
        print("✅ Found analyze method")
        result = apo.analyze("test")
        print(f"Result: {result}")
    
    elif hasattr(apo, 'process'):
        print("✅ Found process method")
        result = apo.process("test")
        print(f"Result: {result}")
    
    else:
        print("❌ No obvious processing method found")
        print("Available methods:")
        for method in methods:
            print(f"  • {method}")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("🎉 Working test complete!")