# Discover what methods are actually available
print("🔍 Discovering APO Class Methods")
print("=" * 50)

try:
    from apo_quantum_logos import (
        UnifiedAPOQuantumLogos,
        MathematicalTheoryProcessor,
        AncientAstronomyProcessor,
        LogogramGlyphProcessor
    )
    
    print("✅ All imports successful")
    
    # Check MathematicalTheoryProcessor methods
    print("\n🧮 MathematicalTheoryProcessor methods:")
    math_proc = MathematicalTheoryProcessor()
    math_methods = [method for method in dir(math_proc) if not method.startswith('_')]
    for method in math_methods:
        print(f"  • {method}")
    
    # Check AncientAstronomyProcessor methods
    print("\n🌌 AncientAstronomyProcessor methods:")
    astro_proc = AncientAstronomyProcessor()
    astro_methods = [method for method in dir(astro_proc) if not method.startswith('_')]
    for method in astro_methods:
        print(f"  • {method}")
    
    # Check LogogramGlyphProcessor methods
    print("\n📜 LogogramGlyphProcessor methods:")
    logo_proc = LogogramGlyphProcessor()
    logo_methods = [method for method in dir(logo_proc) if not method.startswith('_')]
    for method in logo_methods:
        print(f"  • {method}")
    
    # Check UnifiedAPOQuantumLogos methods
    print("\n🌟 UnifiedAPOQuantumLogos methods:")
    apo = UnifiedAPOQuantumLogos()
    apo_methods = [method for method in dir(apo) if not method.startswith('_')]
    for method in apo_methods:
        print(f"  • {method}")
    
    # Check UnifiedAPOQuantumLogos attributes
    print("\n🔧 UnifiedAPOQuantumLogos attributes:")
    apo_attrs = [attr for attr in dir(apo) if not attr.startswith('_') and not callable(getattr(apo, attr))]
    for attr in apo_attrs:
        print(f"  • {attr}")

except Exception as e:
    print(f"❌ Error: {e}")
    import traceback
    traceback.print_exc()

print("🎉 Method discovery complete!")