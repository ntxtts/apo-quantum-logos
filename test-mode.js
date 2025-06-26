// Enhanced APO Quantum Logos Test
console.log('🧪 Testing APO Quantum Logos Node.js Environment...');
console.log('Node version:', process.version);
console.log('Current directory:', process.cwd());
console.log('='.repeat(60));

const { exec } = require('child_process');
const fs = require('fs');
const path = require('path');

// Test results
let testResults = {
  nodeJs: true,
  python: false,
  apoScript: false,
  packages: false
};

// Test Python execution
console.log('🐍 Testing Python...');
exec('python --version', (error, stdout, stderr) => {
  if (error) {
    console.error('❌ Python test failed:', error.message);
    testResults.python = false;
  } else {
    console.log('✅ Python test:', stdout.trim());
    testResults.python = true;
  }
  
  // Test Python packages
  exec('python -c "import numpy, scipy, matplotlib; print(\'Python packages OK\')"', (pkgError, pkgStdout, pkgStderr) => {
    if (pkgError) {
      console.log('❌ Python packages missing. Run: pip install numpy scipy matplotlib pandas sympy');
      testResults.packages = false;
    } else {
      console.log('✅ Python packages:', pkgStdout.trim());
      testResults.packages = true;
    }
    
    printFinalResults();
  });
});

// Test if APO files exist
console.log('📄 Checking APO files...');
const requiredFiles = [
  'apo_quantum_logos.py',
  'package.json',
  'node.js'
];

requiredFiles.forEach(file => {
  if (fs.existsSync(file)) {
    console.log(`✅ ${file} found`);
    if (file === 'apo_quantum_logos.py') {
      testResults.apoScript = true;
      
      // Check file size
      const stats = fs.statSync(file);
      const fileSizeInKB = (stats.size / 1024).toFixed(2);
      console.log(`   📊 Size: ${fileSizeInKB} KB`);
      
      // Quick content check
      const content = fs.readFileSync(file, 'utf-8');
      const lineCount = content.split('\n').length;
      console.log(`   📝 Lines: ${lineCount}`);
      
      // Check for main classes
      if (content.includes('UnifiedAPOQuantumLogos')) {
        console.log('   ✅ UnifiedAPOQuantumLogos class found');
      }
      if (content.includes('MathematicalTheoryProcessor')) {
        console.log('   ✅ MathematicalTheoryProcessor class found');
      }
    }
  } else {
    console.log(`❌ ${file} not found`);
  }
});

// Test Node.js modules
console.log('\n📦 Testing Node.js modules...');
try {
  const readline = require('readline');
  const child_process = require('child_process');
  console.log('✅ Required Node.js modules available');
} catch (moduleError) {
  console.error('❌ Node.js module error:', moduleError.message);
}

// Function to print final results
function printFinalResults() {
  console.log('\n' + '='.repeat(60));
  console.log('🎯 TEST RESULTS SUMMARY');
  console.log('='.repeat(60));
  
  console.log(`Node.js: ${testResults.nodeJs ? '✅' : '❌'}`);
  console.log(`Python: ${testResults.python ? '✅' : '❌'}`);
  console.log(`APO Script: ${testResults.apoScript ? '✅' : '❌'}`);
  console.log(`Python Packages: ${testResults.packages ? '✅' : '❌'}`);
  
  const allGood = Object.values(testResults).every(result => result === true);
  
  if (allGood) {
    console.log('\n🎉 ALL SYSTEMS GO! 🚀');
    console.log('Your APO Quantum Logos system is ready!');
    console.log('\nNext steps:');
    console.log('  node node.js           - Start Node.js bridge');
    console.log('  python apo_quantum_logos.py - Run Python directly');
  } else {
    console.log('\n⚠️  SETUP NEEDED');
    
    if (!testResults.python) {
      console.log('🔧 Install Python 3.9+ from python.org');
    }
    if (!testResults.packages) {
      console.log('🔧 Install packages: pip install numpy scipy matplotlib pandas sympy');
    }
    if (!testResults.apoScript) {
      console.log('🔧 Ensure apo_quantum_logos.py is in current directory');
    }
  }
  
  console.log('\n🌟 APO Quantum Logos Test Complete! 🌟');
}

// Test direct Python execution
console.log('\n🚀 Testing direct Python execution...');
exec('python -c "print(\'Python execution test successful\')"', (pyError, pyStdout, pyStderr) => {
  if (pyError) {
    console.error('❌ Direct Python execution failed:', pyError.message);
  } else {
    console.log('✅ Direct Python execution:', pyStdout.trim());
  }
});