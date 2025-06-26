// Enhanced APO Quantum Logos Node.js Bridge
const { spawn, exec } = require('child_process');
const readline = require('readline');
const fs = require('fs');
const path = require('path');

class APOQuantumLogosRunner {
  constructor() {
    this.pythonScript = 'apo_quantum_logos.py';
    this.isRunning = false;
  }

  // Check if Python and required packages are available
  async checkDependencies() {
    console.log('🔍 Checking APO Quantum Logos dependencies...');
    
    return new Promise((resolve) => {
      exec('python --version', (error, stdout, stderr) => {
        if (error) {
          console.error('❌ Python not found. Please install Python 3.9+');
          resolve(false);
          return;
        }
        
        console.log(`✅ Python found: ${stdout.trim()}`);
        
        // Check if our APO script exists
        if (fs.existsSync(this.pythonScript)) {
          console.log('✅ APO Quantum Logos script found');
          resolve(true);
        } else {
          console.error('❌ apo_quantum_logos.py not found');
          resolve(false);
        }
      });
    });
  }

  // Run APO system in different modes
  runMode(mode = 'interactive', text = null) {
    console.log(`🌟 Starting APO Quantum Logos in ${mode} mode...`);
    
    let command = `python ${this.pythonScript}`;
    
    if (mode !== 'demo') {
      command += ` --mode ${mode}`;
    }
    
    if (text) {
      command += ` --text "${text}"`;
    } else if (mode === 'interactive') {
      command += ' --interactive';
    }

    console.log(`🚀 Executing: ${command}\n`);

    const child = spawn('python', this.buildArgs(mode, text), {
      stdio: 'inherit', // This allows real-time interaction
      shell: true
    });

    child.on('error', (error) => {
      console.error(`❌ Error starting APO system: ${error.message}`);
    });

    child.on('close', (code) => {
      console.log(`\n🏁 APO Quantum Logos exited with code ${code}`);
      this.isRunning = false;
    });

    this.isRunning = true;
    return child;
  }

  buildArgs(mode, text) {
    const args = [this.pythonScript];
    
    if (mode === 'interactive') {
      args.push('--interactive');
    } else if (mode !== 'demo') {
      args.push('--mode', mode);
      if (text) {
        args.push('--text', text);
      }
    }
    
    return args;
  }

  // Quick analysis function
  async analyze(text, mode = 'full') {
    console.log(`🧮 Analyzing: "${text}"`);
    
    return new Promise((resolve, reject) => {
      const command = `python ${this.pythonScript} --mode ${mode} --text "${text}"`;
      
      exec(command, (error, stdout, stderr) => {
        if (error) {
          console.error(`❌ Analysis error: ${error.message}`);
          reject(error);
          return;
        }
        
        if (stderr) {
          console.warn(`⚠️ Warning: ${stderr}`);
        }
        
        console.log('✅ Analysis complete!');
        console.log(stdout);
        resolve(stdout);
      });
    });
  }

  // Interactive CLI for Node.js
  async startInteractiveCLI() {
    console.log('🌟 APO QUANTUM LOGOS - Node.js Interactive Mode 🌟');
    console.log('='.repeat(60));
    console.log('Commands:');
    console.log('  analyze <text>     - Analyze text');
    console.log('  math <text>        - Mathematical analysis');
    console.log('  astro <text>       - Ancient astronomy analysis');
    console.log('  logo <text>        - Logogram analysis');
    console.log('  python             - Launch Python interactive mode');
    console.log('  demo               - Run demo mode');
    console.log('  help               - Show this help');
    console.log('  quit               - Exit');
    console.log('='.repeat(60));

    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    const askQuestion = () => {
      rl.question('\n🧠 APO> ', async (input) => {
        const [command, ...args] = input.trim().split(' ');
        const text = args.join(' ');

        switch (command.toLowerCase()) {
          case 'analyze':
            if (text) {
              await this.analyze(text, 'full');
            } else {
              console.log('Please provide text to analyze');
            }
            break;

          case 'math':
            if (text) {
              await this.analyze(text, 'math_analysis');
            } else {
              console.log('Please provide text for mathematical analysis');
            }
            break;

          case 'astro':
            if (text) {
              await this.analyze(text, 'astronomy');
            } else {
              console.log('Please provide text for astronomical analysis');
            }
            break;

          case 'logo':
            if (text) {
              await this.analyze(text, 'logograms');
            } else {
              console.log('Please provide text for logogram analysis');
            }
            break;

          case 'python':
            console.log('🐍 Launching Python interactive mode...');
            this.runMode('interactive');
            rl.close();
            return;

          case 'demo':
            console.log('🚀 Running demo mode...');
            this.runMode('demo');
            break;

          case 'help':
            console.log('Available commands: analyze, math, astro, logo, python, demo, help, quit');
            break;

          case 'quit':
          case 'exit':
            console.log('👋 Goodbye! Quantum consciousness awaits...');
            rl.close();
            return;

          default:
            if (input.trim()) {
              console.log(`Unknown command: ${command}. Type 'help' for available commands.`);
            }
        }

        askQuestion();
      });
    };

    askQuestion();
  }
}

// Main execution
async function main() {
  const apo = new APOQuantumLogosRunner();
  
  // Check if dependencies are available
  const depsOk = await apo.checkDependencies();
  
  if (!depsOk) {
    console.log('\n💡 To install Python dependencies:');
    console.log('   pip install numpy scipy matplotlib pandas sympy scikit-learn');
    process.exit(1);
  }

  // Parse command line arguments
  const args = process.argv.slice(2);
  
  if (args.length === 0) {
    // No arguments - start interactive CLI
    await apo.startInteractiveCLI();
  } else {
    // Handle specific commands
    const [command, ...rest] = args;
    
    switch (command) {
      case 'interactive':
        apo.runMode('interactive');
        break;
        
      case 'demo':
        apo.runMode('demo');
        break;
        
      case 'analyze':
        const text = rest.join(' ');
        if (text) {
          await apo.analyze(text);
        } else {
          console.log('Please provide text to analyze');
        }
        break;
        
      case 'math':
        const mathText = rest.join(' ');
        if (mathText) {
          await apo.analyze(mathText, 'math_analysis');
        } else {
          console.log('Please provide text for mathematical analysis');
        }
        break;
        
      default:
        console.log('Usage: node node.js [interactive|demo|analyze|math] [text]');
        console.log('Or just: node node.js (for interactive CLI)');
    }
  }
}

// Handle errors gracefully
process.on('uncaughtException', (error) => {
  console.error('❌ Uncaught Exception:', error.message);
  process.exit(1);
});

process.on('unhandledRejection', (reason, promise) => {
  console.error('❌ Unhandled Promise Rejection:', reason);
  process.exit(1);
});

// Run the main function
if (require.main === module) {
  main().catch(error => {
    console.error('❌ Main execution error:', error.message);
    process.exit(1);
  });
}