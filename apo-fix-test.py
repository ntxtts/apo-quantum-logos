# Quick fix test for APO
print("🧪 Testing APO with Quick Fix")
print("=" * 50)

try:
    from apo_quantum_logos import (
        UnifiedAPOQuantumLogos, 
        MathematicalTheoryProcessor,
        AncientAstronomyProcessor,
        LogogramGlyphProcessor
    )
    print("✅ All imports successful")
    
    # Test individual processors first
    print("\n🧮 Testing Mathematical Processor...")
    math_proc = MathematicalTheoryProcessor()
    math_result = math_proc.analyze_mathematical_content("The Schrödinger equation")
    print(f"✅ Math analysis: {math_result.get('total_mathematical_content', 0)}")
    
    print("\n🌌 Testing Astronomy Processor...")
    astro_proc = AncientAstronomyProcessor()
    astro_result = astro_proc.calculate_ancient_astronomical_resonance("Venus cycles")
    print(f"✅ Astro analysis: {astro_result.get('total_resonance', 0)}")
    
    print("\n📜 Testing Logogram Processor...")
    logo_proc = LogogramGlyphProcessor()
    logo_result = logo_proc.detect_logograms_and_glyphs("天地人")
    print(f"✅ Logo analysis: {logo_result.get('total_logographic_content', 0)}")
    
    # Now test the unified system
    print("\n🌟 Testing Unified System...")
    apo = UnifiedAPOQuantumLogos()
    
    # Check if processors are initialized
    if hasattr(apo, 'math_theory_processor'):
        print("✅ Math processor initialized")
    else:
        print("❌ Math processor missing")
        # Add it manually
        apo.math_theory_processor = math_proc
        print("🔧 Math processor added manually")
    
    if hasattr(apo, 'ancient_astronomy_processor'):
        print("✅ Astro processor initialized")
    else:
        print("❌ Astro processor missing")
        apo.ancient_astronomy_processor = astro_proc
        print("🔧 Astro processor added manually")
    
    if hasattr(apo, 'logogram_processor'):
        print("✅ Logo processor initialized")
    else:
        print("❌ Logo processor missing")
        apo.logogram_processor = logo_proc
        print("🔧 Logo processor added manually")
    
    # Test unified analysis
    test_text = "The Schrödinger equation describes quantum evolution"
    print(f"\n📝 Testing unified analysis: {test_text}")
    
    result = apo.process_unified_logos(test_text)
    print("✅ Unified analysis complete!")
    print(f"🧮 Unified signature: {result['unified_signature']}")
    print(f"🧠 Consciousness field: {abs(result['consciousness_field']):.3f}")
    
except ImportError as e:
    print(f"❌ Import error: {e}")
except AttributeError as e:
    print(f"❌ Attribute error: {e}")
    print("💡 The UnifiedAPOQuantumLogos class needs processor initialization")
except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("🎉 APO fix test complete!")