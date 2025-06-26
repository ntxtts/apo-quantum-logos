console.log('🧪 Minimal Node.js Test');
console.log('Node version:', process.version);

// Just test if Node.js works
const testData = {
  timestamp: new Date().toISOString(),
  message: 'Node.js is working!',
  ready: true
};

console.log('✅ Test data:', JSON.stringify(testData, null, 2));
console.log('🎉 Minimal test complete!');