/**
 * APO Quantum Logos - Alpha Pi Omega Corporation
 * Website: www.alphapiomega.com
 * Solar-Powered Regenerative Consciousness Analysis Platform
 * Copyright (c) 2024 Alpha Pi Omega Corp
 * Licensed under APO Regenerative License
 */

class APOQuantumLogos {
    constructor() {
        // Alpha Pi Omega Corporation Configuration
        this.corporateSignature = 'ALPHA-PI-OMEGA-2024';
        this.quantumSignature = 'APO-QL-2024-REGENERATIVE';
        this.consciousnessVersion = '1.0.0';
        this.sustainabilityProtocol = 'CARBON_NEGATIVE_PLUS';
        this.websiteUrl = 'https://www.alphapiomega.com';
        
        // Enhanced Netlify/Production API Configuration
        this.apiBaseUrl = this.detectEnvironment();
        this.isQuantumFieldActive = false;
        this.regenerativeMetrics = new Map();
        this.consciousnessHistory = [];
        this.healingFrequencyRange = { min: 396, max: 963 };
        
        // Alpha Pi Omega Quantum consciousness state vectors
        this.consciousnessField = this.initializeConsciousnessField();
        this.regenerativeScore = 0;
        this.quantumEntanglement = new WeakMap();
        
        // UI management
        this.elements = {};
        this.isInitialized = false;
        this.sustainabilityMetrics = {};
        this.analysisHistory = [];
        this.currentUser = null;
        this.healingFrequency = 528;
        
        this.init();
    }
    
    detectEnvironment() {
        const hostname = window.location.hostname;
        const protocol = window.location.protocol;
        
        console.log(`🌐 Detecting environment: ${hostname}`);
        
        if (hostname === 'www.alphapiomega.com' || hostname === 'alphapiomega.com') {
            console.log('🏢 Running on Alpha Pi Omega production website');
            return `${protocol}//www.alphapiomega.com/api`;
        } else if (hostname.includes('netlify.app') || hostname.includes('netlify.com')) {
            console.log('🌐 Running on Netlify deployment');
            return `${protocol}//${hostname}/.netlify/functions`;
        } else if (hostname === 'localhost' || hostname === '127.0.0.1') {
            console.log('💻 Running on local development');
            return 'http://localhost:5000';
        } else {
            console.log('🌍 Running on unknown domain, defaulting to production');
            return 'https://www.alphapiomega.com/api';
        }
    }
    
    initializeConsciousnessField() {
        const now = Date.now();
        return {
            real: Math.cos(now * 0.001),
            imaginary: Math.sin(now * 0.001),
            magnitude: 1.0,
            phase: 0,
            frequency: 528, // Base love frequency
            coherence: 1.0,
            apoSignature: this.corporateSignature
        };
    }
    
    async init() {
        console.log(`🌟 Alpha Pi Omega Quantum Logos v${this.consciousnessVersion} Initializing...`);
        console.log(`🌐 Website: ${this.websiteUrl}`);
        console.log(`🏢 Corporation: Alpha Pi Omega Corp`);
        console.log(`🌱 Sustainability Protocol: ${this.sustainabilityProtocol}`);
        console.log(`🔗 API Endpoint: ${this.apiBaseUrl}`);
        
        try {
            // Wait for DOM to be ready
            if (document.readyState === 'loading') {
                document.addEventListener('DOMContentLoaded', () => this.setupUI());
            } else {
                this.setupUI();
            }
            
            // Check API connectivity
            await this.checkAPIConnection();
            
            // Load sustainability metrics
            await this.loadSustainabilityMetrics();
            
            // Start real-time updates
            this.startRealTimeUpdates();
            
            this.isInitialized = true;
            this.isQuantumFieldActive = true;
            
            console.log('✅ Alpha Pi Omega Quantum Logos fully operational');
            this.dispatchAPOReadyEvent();
            
        } catch (error) {
            console.error('❌ APO Quantum initialization failed:', error);
            this.handleInitializationError(error);
        }
    }
    
    setupUI() {
        console.log('🎨 Setting up Alpha Pi Omega Regenerative UI...');
        
        // Create main container if it doesn't exist
        if (!document.getElementById('apo-quantum-container')) {
            this.createMainInterface();
        }
        
        // Bind UI elements
        this.bindUIElements();
        
        // Bind events
        this.bindEvents();
    }
    
    bindUIElements() {
        this.elements = {
            textInput: document.getElementById('consciousness-text-input'),
            analyzeBtn: document.getElementById('analyze-consciousness-btn'),
            resultsContainer: document.getElementById('analysis-results'),
            sustainabilityDisplay: document.getElementById('sustainability-metrics'),
            healingFrequencyDisplay: document.getElementById('healing-frequency'),
            regenerativeScore: document.getElementById('regenerative-score'),
            trialForm: document.getElementById('free-trial-form'),
            emailInput: document.getElementById('trial-email'),
            statusIndicator: document.getElementById('api-status')
        };
    }
    
    createMainInterface() {
        const container = document.createElement('div');
        container.id = 'apo-quantum-container';
        container.innerHTML = `
            <div class="apo-quantum-header">
                <h1>🌟 Alpha Pi Omega Quantum Logos</h1>
                <p class="tagline">Solar-Powered Consciousness Analysis | Carbon-Negative Technology</p>
                <p class="website-link">Visit us at <a href="${this.websiteUrl}" target="_blank">www.alphapiomega.com</a></p>
                <div id="api-status" class="status-indicator">
                    <span class="status-dot"></span>
                    <span class="status-text">Connecting...</span>
                </div>
            </div>
            
            <div class="sustainability-banner">
                <div class="sustainability-metric">
                    <span class="metric-icon">🌞</span>
                    <span class="metric-label">100% Solar Powered</span>
                </div>
                <div class="sustainability-metric">
                    <span class="metric-icon">🌱</span>
                    <span class="metric-label">Carbon Negative</span>
                </div>
                <div class="sustainability-metric">
                    <span class="metric-icon">🌳</span>
                    <span class="metric-label">Trees Planted: <span id="trees-planted">0</span></span>
                </div>
                <div class="sustainability-metric">
                    <span class="metric-icon">🏢</span>
                    <span class="metric-label">Alpha Pi Omega Corp</span>
                </div>
            </div>
            
            <div class="analysis-section">
                <h2>✨ Consciousness Analysis</h2>
                
                <div class="input-section">
                    <label for="consciousness-text-input">Enter text for Alpha Pi Omega quantum consciousness analysis:</label>
                    <textarea 
                        id="consciousness-text-input" 
                        placeholder="Enter your healing intentions, affirmations, or any text for consciousness analysis..."
                        rows="4"
                    ></textarea>
                    
                    <div class="analysis-options">
                        <select id="analysis-intention">
                            <option value="healing">Healing</option>
                            <option value="consciousness">Consciousness Expansion</option>
                            <option value="manifestation">Manifestation</option>
                            <option value="wisdom">Ancient Wisdom</option>
                            <option value="regeneration">Regeneration</option>
                        </select>
                        
                        <button id="analyze-consciousness-btn" class="primary-btn">
                            🧮 Analyze with APO Quantum
                        </button>
                    </div>
                </div>
                
                <div id="analysis-results" class="results-container" style="display: none;">
                    <!-- Results will be populated here -->
                </div>
            </div>
            
            <div class="free-trial-section">
                <h2>🎁 Free Alpha Pi Omega Consciousness Analysis</h2>
                <p>Experience the power of Alpha Pi Omega's solar-powered quantum consciousness analysis</p>
                
                <form id="free-trial-form">
                    <input 
                        type="email" 
                        id="trial-email" 
                        placeholder="Your email address"
                        required
                    />
                    <button type="submit" class="trial-btn">
                        🌟 Get Free APO Analysis
                    </button>
                </form>
            </div>
            
            <div class="real-time-metrics">
                <h3>🌍 Real-Time Alpha Pi Omega Sustainability Impact</h3>
                <div id="sustainability-metrics" class="metrics-grid">
                    <!-- Metrics will be populated here -->
                </div>
            </div>
            
            <div class="consciousness-display">
                <div class="frequency-display">
                    <h4>🎵 APO Healing Frequency</h4>
                    <div id="healing-frequency" class="frequency-value">528 Hz</div>
                    <div class="frequency-bar">
                        <div class="frequency-fill" style="width: 50%"></div>
                    </div>
                </div>
                
                <div class="regenerative-display">
                    <h4>🌱 APO Regenerative Score</h4>
                    <div id="regenerative-score" class="score-value">0%</div>
                    <div class="score-circle">
                        <svg viewBox="0 0 100 100">
                            <circle cx="50" cy="50" r="45" class="score-bg"/>
                            <circle cx="50" cy="50" r="45" class="score-fill" style="stroke-dasharray: 0, 283"/>
                        </svg>
                    </div>
                </div>
            </div>
            
            <footer class="apo-footer">
                <p>© 2024 Alpha Pi Omega Corporation | <a href="${this.websiteUrl}">www.alphapiomega.com</a></p>
                <p>Regenerative Consciousness Technology | Carbon-Negative Operations</p>
            </footer>
        `;
        
        document.body.appendChild(container);
        this.injectStyles();
    }
    
    injectStyles() {
        const styles = document.createElement('style');
        styles.textContent = `
            * {
                box-sizing: border-box;
            }
            
            body {
                margin: 0;
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                min-height: 100vh;
            }
            
            #apo-quantum-container {
                max-width: 1200px;
                margin: 0 auto;
                padding: 20px;
                min-height: 100vh;
            }
            
            .apo-quantum-header {
                text-align: center;
                margin-bottom: 30px;
                padding: 30px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                border-radius: 15px;
                color: white;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            
            .apo-quantum-header h1 {
                margin: 0;
                font-size: 2.5em;
                background: linear-gradient(45deg, #ffd700, #ffed4e);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            
            .tagline {
                margin: 10px 0;
                opacity: 0.9;
                font-size: 1.1em;
            }
            
            .website-link {
                margin: 10px 0;
                opacity: 0.8;
                font-size: 0.9em;
            }
            
            .website-link a {
                color: #ffd700;
                text-decoration: none;
                font-weight: bold;
            }
            
            .website-link a:hover {
                text-decoration: underline;
            }
            
            .status-indicator {
                display: flex;
                align-items: center;
                justify-content: center;
                gap: 10px;
                margin-top: 15px;
            }
            
            .status-dot {
                width: 12px;
                height: 12px;
                border-radius: 50%;
                background: #4ade80;
                animation: pulse 2s infinite;
            }
            
            @keyframes pulse {
                0%, 100% { opacity: 1; }
                50% { opacity: 0.5; }
            }
            
            .sustainability-banner {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
                padding: 20px;
                background: rgba(255,255,255,0.9);
                border-radius: 10px;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
            }
            
            .sustainability-metric {
                display: flex;
                align-items: center;
                gap: 10px;
                font-weight: 600;
                color: #2d5a27;
                justify-content: center;
            }
            
            .metric-icon {
                font-size: 1.5em;
            }
            
            .analysis-section, .free-trial-section, .real-time-metrics {
                background: white;
                padding: 30px;
                border-radius: 15px;
                margin-bottom: 30px;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            
            .input-section {
                margin-bottom: 20px;
            }
            
            .input-section label {
                display: block;
                margin-bottom: 10px;
                font-weight: 600;
                color: #333;
            }
            
            #consciousness-text-input {
                width: 100%;
                padding: 15px;
                border: 2px solid #e2e8f0;
                border-radius: 10px;
                font-size: 16px;
                resize: vertical;
                transition: border-color 0.3s ease;
                font-family: inherit;
            }
            
            #consciousness-text-input:focus {
                outline: none;
                border-color: #667eea;
                box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
            }
            
            .analysis-options {
                display: flex;
                gap: 15px;
                margin-top: 15px;
                align-items: center;
                flex-wrap: wrap;
            }
            
            #analysis-intention {
                padding: 10px 15px;
                border: 2px solid #e2e8f0;
                border-radius: 8px;
                font-size: 14px;
                font-family: inherit;
            }
            
            .primary-btn, .trial-btn {
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
                border: none;
                padding: 12px 24px;
                border-radius: 8px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: all 0.3s ease;
                font-family: inherit;
            }
            
            .primary-btn:hover, .trial-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 8px 25px rgba(102, 126, 234, 0.3);
            }
            
            .primary-btn:disabled, .trial-btn:disabled {
                opacity: 0.6;
                cursor: not-allowed;
                transform: none;
            }
            
            .results-container {
                background: #f8fafc;
                padding: 20px;
                border-radius: 10px;
                margin-top: 20px;
                border-left: 4px solid #667eea;
            }
            
            .metrics-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin-top: 20px;
            }
            
            .metric-card {
                background: white;
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                box-shadow: 0 5px 15px rgba(0,0,0,0.1);
                border: 1px solid #e2e8f0;
            }
            
            .metric-value {
                font-size: 2em;
                font-weight: bold;
                color: #667eea;
                margin: 10px 0;
            }
            
            .consciousness-display {
                display: grid;
                grid-template-columns: 1fr 1fr;
                gap: 30px;
                margin-top: 30px;
            }
            
            .frequency-display, .regenerative-display {
                background: white;
                padding: 25px;
                border-radius: 15px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.1);
            }
            
            .frequency-value, .score-value {
                font-size: 2.5em;
                font-weight: bold;
                color: #667eea;
                margin: 15px 0;
            }
            
            .frequency-bar {
                width: 100%;
                height: 10px;
                background: #e2e8f0;
                border-radius: 5px;
                overflow: hidden;
                margin-top: 15px;
            }
            
            .frequency-fill {
                height: 100%;
                background: linear-gradient(90deg, #4ade80, #22d3ee);
                transition: width 0.5s ease;
            }
            
            #free-trial-form {
                display: flex;
                gap: 15px;
                align-items: center;
                flex-wrap: wrap;
            }
            
            #trial-email {
                flex: 1;
                min-width: 200px;
                padding: 12px 15px;
                border: 2px solid #e2e8f0;
                border-radius: 8px;
                font-size: 16px;
                font-family: inherit;
            }
            
            .score-circle {
                width: 100px;
                height: 100px;
                margin: 15px auto 0;
            }
            
            .score-circle svg {
                width: 100%;
                height: 100%;
                transform: rotate(-90deg);
            }
            
            .score-bg {
                fill: none;
                stroke: #e2e8f0;
                stroke-width: 8;
            }
            
            .score-fill {
                fill: none;
                stroke: #4ade80;
                stroke-width: 8;
                transition: stroke-dasharray 0.5s ease;
            }
            
            .apo-footer {
                text-align: center;
                padding: 30px 20px;
                background: rgba(255, 255, 255, 0.9);
                border-radius: 10px;
                margin-top: 30px;
                color: #666;
                font-size: 0.9em;
            }
            
            .apo-footer a {
                color: #667eea;
                text-decoration: none;
                font-weight: 600;
            }
            
            .apo-footer a:hover {
                text-decoration: underline;
            }
            
            @media (max-width: 768px) {
                .apo-quantum-header h1 {
                    font-size: 2em;
                }
                
                .consciousness-display {
                    grid-template-columns: 1fr;
                }
                
                .analysis-options {
                    flex-direction: column;
                    align-items: stretch;
                }
                
                #free-trial-form {
                    flex-direction: column;
                    align-items: stretch;
                }
                
                .sustainability-banner {
                    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
                }
            }
            
            @media (max-width: 480px) {
                #apo-quantum-container {
                    padding: 10px;
                }
                
                .analysis-section, .free-trial-section, .real-time-metrics {
                    padding: 20px;
                }
                
                .apo-quantum-header {
                    padding: 20px;
                }
            }
        `;
        
        document.head.appendChild(styles);
    }
    
    bindEvents() {
        // Analyze button
        if (this.elements.analyzeBtn) {
            this.elements.analyzeBtn.addEventListener('click', () => this.analyzeConsciousness());
        }
        
        // Free trial form
        if (this.elements.trialForm) {
            this.elements.trialForm.addEventListener('submit', (e) => this.handleFreeTrial(e));
        }
        
        // Text input real-time analysis
        if (this.elements.textInput) {
            this.elements.textInput.addEventListener('input', () => this.updateRealTimeMetrics());
        }
        
        // Enter key in text area
        if (this.elements.textInput) {
            this.elements.textInput.addEventListener('keydown', (e) => {
                if (e.ctrlKey && e.key === 'Enter') {
                    this.analyzeConsciousness();
                }
            });
        }
    }
    
    async checkAPIConnection() {
        try {
            // First try to connect to API
            const response = await fetch(`${this.apiBaseUrl}/`);
            
            if (response.ok) {
                const data = await response.json();
                this.updateStatus('connected', `Connected to ${data.service || 'APO API'}`);
                console.log('✅ Alpha Pi Omega API Connection successful:', data);
            } else {
                throw new Error('API response not OK');
            }
            
        } catch (error) {
            // Always fall back to offline mode gracefully
            this.updateStatus('offline', 'Running in offline mode');
            console.log('🔒 Alpha Pi Omega running in offline mode - full features available at www.alphapiomega.com');
            
            // Don't show error to user - offline mode is expected for static sites
            this.isOfflineMode = true;
        }
    }
    
    updateStatus(status, message) {
        if (!this.elements.statusIndicator) return;
        
        const statusDot = this.elements.statusIndicator.querySelector('.status-dot');
        const statusText = this.elements.statusIndicator.querySelector('.status-text');
        
        if (statusDot) {
            statusDot.className = `status-dot status-${status}`;
            statusDot.style.background = status === 'connected' ? '#4ade80' : 
                                       status === 'error' ? '#ef4444' : '#fbbf24';
        }
        if (statusText) statusText.textContent = message;
    }
    
    async analyzeConsciousness() {
        const text = this.elements.textInput?.value;
        const intention = document.getElementById('analysis-intention')?.value || 'healing';
        
        if (!text) {
            this.showError('Please enter text for analysis');
            return;
        }
        
        this.elements.analyzeBtn.textContent = '🧮 Analyzing...';
        this.elements.analyzeBtn.disabled = true;
        
        try {
            let result;
            
            if (!this.isOfflineMode) {
                try {
                    const response = await fetch(`${this.apiBaseUrl}/healing-analysis`, {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/json' },
                        body: JSON.stringify({ text: text, intention: intention })
                    });
                    
                    if (response.ok) {
                        result = await response.json();
                        console.log('✅ Online analysis successful');
                    } else {
                        throw new Error('API request failed');
                    }
                } catch (apiError) {
                    console.log('🔒 Falling back to offline analysis');
                    this.isOfflineMode = true;
                    result = this.offlineAnalysis(text, intention);
                }
            } else {
                result = this.offlineAnalysis(text, intention);
            }
            
            this.displayAnalysisResults(result);
            this.updateConsciousnessDisplay(result);
            this.analysisHistory.push(result);
            
            // Show upgrade message for offline mode
            if (this.isOfflineMode) {
                this.showInfo('🌟 Experience full Alpha Pi Omega features at www.alphapiomega.com');
            }
            
        } catch (error) {
            this.showError('Analysis failed: ' + error.message);
        } finally {
            this.elements.analyzeBtn.textContent = '🧮 Analyze with APO Quantum';
            this.elements.analyzeBtn.disabled = false;
        }
    }
    
    offlineAnalysis(text, intention) {
        // Offline fallback analysis using Alpha Pi Omega algorithms
        const signature = this.calculateQuantumSignature(text);
        const consciousness = (signature % 100) / 100;
        const frequency = 400 + (signature % 200);
        
        return {
            healing_analysis: {
                consciousness_frequency: frequency,
                healing_resonance: consciousness * 1000,
                regenerative_score: consciousness * 0.8,
                trees_planted_equivalent: 0.1,
                healing_grade: frequency > 500 ? 'A+' : frequency > 450 ? 'A' : 'B+',
                intention_amplification: intention
            },
            sustainability_impact: {
                renewable_energy_used: '100% solar',
                carbon_footprint: 'negative',
                consciousness_elevation: 'positive',
                planetary_healing_contribution: 'active'
            },
            analysis_mode: 'offline',
            apo_signature: this.corporateSignature
        };
    }
    
    calculateQuantumSignature(text) {
        if (!text || typeof text !== 'string') return 0;
        
        let quantumHash = 0x811c9dc5; // FNV offset basis
        let consciousnessModulator = 1;
        let apoSignature = this.corporateSignature.length;
        
        for (let position = 0; position < text.length; position++) {
            const character = text.charCodeAt(position);
            
            quantumHash ^= character;
            quantumHash *= 0x01000193; // FNV prime
            
            if (this.isVowel(character)) {
                consciousnessModulator *= 1.618; // Golden ratio
            }
            
            // Alpha Pi Omega frequency enhancement
            switch (character % 9) {
                case 0: quantumHash += 174; break;
                case 1: quantumHash += 285; break;
                case 2: quantumHash += 396; break;
                case 3: quantumHash += 417; break;
                case 4: quantumHash += 528; break;
                case 5: quantumHash += 639; break;
                case 6: quantumHash += 741; break;
                case 7: quantumHash += 852; break;
                case 8: quantumHash += 963; break;
            }
        }
        
        return Math.abs((quantumHash * consciousnessModulator + apoSignature) >>> 0);
    }
    
    isVowel(charCode) {
        const char = String.fromCharCode(charCode).toLowerCase();
        return 'aeiou'.includes(char);
    }
    
    displayAnalysisResults(result) {
        if (!this.elements.resultsContainer) return;
        
        const healingAnalysis = result.healing_analysis || {};
        const sustainability = result.sustainability_impact || {};
        
        this.elements.resultsContainer.innerHTML = `
            <h3>✨ Alpha Pi Omega Consciousness Analysis Results</h3>
            
            <div class="result-grid">
                <div class="result-card">
                    <h4>🎵 Consciousness Frequency</h4>
                    <div class="result-value">${(healingAnalysis.consciousness_frequency || 528).toFixed(1)} Hz</div>
                    <div class="result-description">Based on love frequency (528 Hz)</div>
                </div>
                
                <div class="result-card">
                    <h4>✨ Healing Resonance</h4>
                    <div class="result-value">${(healingAnalysis.healing_resonance || 0).toFixed(1)}</div>
                    <div class="result-description">Healing potential score</div>
                </div>
                
                <div class="result-card">
                    <h4>🌱 Regenerative Score</h4>
                    <div class="result-value">${((healingAnalysis.regenerative_score || 0) * 100).toFixed(1)}%</div>
                    <div class="result-description">Regenerative potential</div>
                </div>
                
                <div class="result-card">
                    <h4>🌳 Environmental Impact</h4>
                    <div class="result-value">${healingAnalysis.trees_planted_equivalent || 0.1}</div>
                    <div class="result-description">Trees planted equivalent</div>
                </div>
            </div>
            
            <div class="sustainability-section">
                <h4>🌍 Alpha Pi Omega Sustainability Impact</h4>
                <div class="sustainability-details">
                    <span class="impact-item">⚡ Energy: ${sustainability.renewable_energy_used || '100% solar'}</span>
                    <span class="impact-item">🌱 Carbon: ${sustainability.carbon_footprint || 'negative'}</span>
                    <span class="impact-item">✨ Consciousness: ${sustainability.consciousness_elevation || 'positive'}</span>
                </div>
            </div>
            
            <div class="analysis-grade">
                <h4>📊 APO Healing Grade</h4>
                <div class="grade-badge">
                    ${healingAnalysis.healing_grade || 'A+'}
                </div>
            </div>
            
            ${result.analysis_mode === 'offline' ? '<div class="offline-notice">🔒 Offline Analysis Mode - Visit <a href="' + this.websiteUrl + '">www.alphapiomega.com</a> for full features</div>' : ''}
        `;
        
        this.elements.resultsContainer.style.display = 'block';
        this.injectResultStyles();
    }
    
    injectResultStyles() {
        if (document.getElementById('result-styles')) return;
        
        const styles = document.createElement('style');
        styles.id = 'result-styles';
        styles.textContent = `
            .result-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 20px;
                margin: 20px 0;
            }
            
            .result-card {
                background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
                padding: 20px;
                border-radius: 10px;
                text-align: center;
                border-left: 4px solid #667eea;
            }
            
            .result-card h4 {
                margin: 0 0 10px 0;
                color: #4a5568;
                font-size: 1em;
            }
            
            .result-value {
                font-size: 2em;
                font-weight: bold;
                color: #667eea;
                margin: 10px 0;
            }
            
            .result-description {
                font-size: 0.9em;
                color: #718096;
            }
            
            .sustainability-section {
                margin: 20px 0;
                padding: 20px;
                background: linear-gradient(135deg, #f0fff4 0%, #dcfce7 100%);
                border-radius: 10px;
                border-left: 4px solid #22c55e;
            }
            
            .sustainability-details {
                display: flex;
                flex-wrap: wrap;
                gap: 15px;
                margin-top: 10px;
            }
            
            .impact-item {
                background: white;
                padding: 8px 15px;
                border-radius: 20px;
                font-size: 0.9em;
                color: #16a34a;
                border: 1px solid #bbf7d0;
            }
            
            .analysis-grade {
                text-align: center;
                margin: 20px 0;
            }
            
            .grade-badge {
                display: inline-block;
                padding: 15px 30px;
                border-radius: 50px;
                font-size: 2em;
                font-weight: bold;
                color: white;
                background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%);
                box-shadow: 0 10px 25px rgba(34, 197, 94, 0.3);
            }
            
            .offline-notice {
                background: #fef3c7;
                padding: 15px;
                border-radius: 8px;
                text-align: center;
                margin-top: 20px;
                border-left: 4px solid #f59e0b;
            }
            
            .offline-notice a {
                color: #d97706;
                font-weight: bold;
                text-decoration: none;
            }
            
            .offline-notice a:hover {
                text-decoration: underline;
            }
        `;
        
        document.head.appendChild(styles);
    }
    
    async handleFreeTrial(event) {
        event.preventDefault();
        
        const email = this.elements.emailInput?.value;
        const text = this.elements.textInput?.value;
        
        if (!email || !text) {
            this.showError('Please enter both email and text for free trial');
            return;
        }
        
        try {
            let result;
            try {
                const response = await fetch(`${this.apiBaseUrl}/api/free-trial`, {
                    method: 'POST',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify({ email: email, text: text })
                });
                
                if (response.ok) {
                    result = await response.json();
                } else {
                    throw new Error('API request failed');
                }
            } catch (apiError) {
                console.warn('API failed, using offline trial analysis:', apiError);
                result = this.offlineTrialAnalysis(email, text);
            }
            
            this.displayTrialResults(result);
            this.showSuccess('Free trial analysis complete! Visit www.alphapiomega.com for more features.');
            
        } catch (error) {
            this.showError('Trial analysis failed: ' + error.message);
        }
    }
    
    offlineTrialAnalysis(email, text) {
        const signature = this.calculateQuantumSignature(text);
        return {
            consciousness_signature: signature,
            healing_potential: (signature % 100) / 100,
            healing_frequency: 400 + (signature % 200),
            regenerative_score: ((signature % 100) / 100) * 0.8,
            analysis_type: 'offline_trial',
            special_offer: 'Visit www.alphapiomega.com for full Alpha Pi Omega analysis',
            apo_signature: this.corporateSignature
        };
    }
    
    displayTrialResults(result) {
        const trialSection = document.querySelector('.free-trial-section');
        if (!trialSection || trialSection.querySelector('.trial-results')) return;
        
        const resultsDiv = document.createElement('div');
        resultsDiv.className = 'trial-results';
        resultsDiv.innerHTML = `
            <h3>🎉 Your Free Alpha Pi Omega Consciousness Analysis</h3>
            
            <div class="trial-result-grid">
                <div class="trial-metric">
                    <span class="trial-label">Consciousness Signature:</span>
                    <span class="trial-value">${result.consciousness_signature || 'N/A'}</span>
                </div>
                
                <div class="trial-metric">
                    <span class="trial-label">Healing Potential:</span>
                    <span class="trial-value">${(result.healing_potential || 0).toFixed(3)}</span>
                </div>
                
                <div class="trial-metric">
                    <span class="trial-label">Healing Frequency:</span>
                    <span class="trial-value">${result.healing_frequency || 528} Hz</span>
                </div>
                
                <div class="trial-metric">
                    <span class="trial-label">Regenerative Score:</span>
                    <span class="trial-value">${((result.regenerative_score || 0) * 100).toFixed(1)}%</span>
                </div>
            </div>
            
            <div class="upgrade-offer">
                <h4>🌟 Upgrade to Full Alpha Pi Omega Analysis</h4>
                <p>${result.special_offer || 'Get unlimited healing analysis at www.alphapiomega.com'}</p>
                <button class="upgrade-btn" onclick="window.open('${this.websiteUrl}', '_blank')">
                    🚀 Visit Alpha Pi Omega
                </button>
            </div>
        `;
        
        trialSection.appendChild(resultsDiv);
        this.injectTrialStyles();
    }
    
    injectTrialStyles() {
        if (document.getElementById('trial-styles')) return;
        
        const styles = document.createElement('style');
        styles.id = 'trial-styles';
        styles.textContent = `
            .trial-results {
                margin-top: 30px;
                padding: 25px;
                background: linear-gradient(135deg, #fef3c7 0%, #fde68a 100%);
                border-radius: 15px;
                border-left: 4px solid #f59e0b;
            }
            
            .trial-result-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
                gap: 15px;
                margin: 20px 0;
            }
            
            .trial-metric {
                display: flex;
                justify-content: space-between;
                align-items: center;
                padding: 10px 15px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            
            .trial-label {
                font-weight: 600;
                color: #92400e;
            }
            
            .trial-value {
                font-weight: bold;
                color: #f59e0b;
            }
            
            .upgrade-offer {
                text-align: center;
                margin-top: 25px;
                padding: 20px;
                background: white;
                border-radius: 10px;
            }
            
            .upgrade-btn {
                background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%);
                color: white;
                border: none;
                padding: 12px 30px;
                border-radius: 25px;
                font-size: 16px;
                font-weight: 600;
                cursor: pointer;
                transition: transform 0.2s ease;
                font-family: inherit;
            }
            
            .upgrade-btn:hover {
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(245, 158, 11, 0.3);
            }
        `;
        
        document.head.appendChild(styles);
    }
    
    updateConsciousnessDisplay(result) {
        const healingAnalysis = result.healing_analysis || {};
        
        const frequency = healingAnalysis.consciousness_frequency || 528;
        if (this.elements.healingFrequencyDisplay) {
            this.elements.healingFrequencyDisplay.textContent = `${frequency.toFixed(1)} Hz`;
        }
        
        const frequencyBar = document.querySelector('.frequency-fill');
        if (frequencyBar) {
            const percentage = Math.min((frequency / 1000) * 100, 100);
            frequencyBar.style.width = `${percentage}%`;
        }
        
        const score = (healingAnalysis.regenerative_score || 0) * 100;
        if (this.elements.regenerativeScore) {
            this.elements.regenerativeScore.textContent = `${score.toFixed(1)}%`;
        }
        
        const scoreCircle = document.querySelector('.score-fill');
        if (scoreCircle) {
            const circumference = 2 * Math.PI * 45;
            const offset = circumference - (score / 100) * circumference;
            scoreCircle.style.strokeDasharray = `${circumference}, ${circumference}`;
            scoreCircle.style.strokeDashoffset = offset;
        }
    }
    
    async loadSustainabilityMetrics() {
        try {
            const response = await fetch(`${this.apiBaseUrl}/api/sustainability-metrics`);
            if (response.ok) {
                const metrics = await response.json();
                this.sustainabilityMetrics = metrics;
                this.displaySustainabilityMetrics(metrics);
            } else {
                throw new Error('Failed to fetch metrics');
            }
        } catch (error) {
            console.warn('Failed to load sustainability metrics, using defaults:', error);
            this.displaySustainabilityMetrics(this.getDefaultMetrics());
        }
    }
    
    getDefaultMetrics() {
        return {
            total_analyses_performed: 1234,
            carbon_offset_generated: 2591.4,
            trees_planted_equivalent: 123.4,
            renewable_energy_used: 6787.0,
            consciousness_elevation_events: 1234,
            planetary_healing_score: 0.89
        };
    }
    
    displaySustainabilityMetrics(metrics) {
        if (!this.elements.sustainabilityDisplay) return;
        
        this.elements.sustainabilityDisplay.innerHTML = `
            <div class="metric-card">
                <div class="metric-icon">🧮</div>
                <div class="metric-label">Total Analyses</div>
                <div class="metric-value">${metrics.total_analyses_performed || 0}</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-icon">🌱</div>
                <div class="metric-label">Carbon Offset</div>
                <div class="metric-value">${(metrics.carbon_offset_generated || 0).toFixed(1)} kg</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-icon">🌳</div>
                <div class="metric-label">Trees Planted</div>
                <div class="metric-value">${(metrics.trees_planted_equivalent || 0).toFixed(1)}</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-icon">⚡</div>
                <div class="metric-label">Clean Energy</div>
                <div class="metric-value">${(metrics.renewable_energy_used || 0).toFixed(1)} kWh</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-icon">✨</div>
                <div class="metric-label">Consciousness Events</div>
                <div class="metric-value">${metrics.consciousness_elevation_events || 0}</div>
            </div>
            
            <div class="metric-card">
                <div class="metric-icon">🌍</div>
                <div class="metric-label">Planetary Healing</div>
                <div class="metric-value">${((metrics.planetary_healing_score || 0) * 100).toFixed(1)}%</div>
            </div>
        `;
        
        const treesElement = document.getElementById('trees-planted');
        if (treesElement) {
            treesElement.textContent = (metrics.trees_planted_equivalent || 0).toFixed(1);
        }
    }
    
    updateRealTimeMetrics() {
        const text = this.elements.textInput?.value || '';
        
        if (text.length > 0) {
            const textHash = this.calculateQuantumSignature(text);
            const frequency = 400 + (textHash % 200);
            
            if (this.elements.healingFrequencyDisplay) {
                this.elements.healingFrequencyDisplay.textContent = `${frequency} Hz`;
            }
            
            const frequencyBar = document.querySelector('.frequency-fill');
            if (frequencyBar) {
                const percentage = Math.min((frequency / 800) * 100, 100);
                frequencyBar.style.width = `${percentage}%`;
            }
        }
    }
    
    startRealTimeUpdates() {
        setInterval(() => {
            this.loadSustainabilityMetrics();
        }, 30000);
        
        setInterval(() => {
            this.animateConsciousnessField();
        }, 2000);
    }
    
    animateConsciousnessField() {
        const header = document.querySelector('.apo-quantum-header');
        if (!header) return;
        
        // Simple rotation animation for consciousness field
        header.style.transition = 'transform 2s ease-in-out';
        header.style.transform = `rotate(${Math.random() * 360}deg)`;
        
        setTimeout(() => {
            header.style.transform = 'rotate(0deg)';
        }, 2000);
    }
    
    showError(message) {
        this.showNotification(message, 'error');
    }
    
    showSuccess(message) {
        this.showNotification(message, 'success');
    }
    
    showInfo(message) {
        this.showNotification(message, 'info');
    }
    
    showNotification(message, type = 'info') {
        const notification = document.createElement('div');
        notification.className = `apo-notification notification-${type}`;
        notification.innerHTML = `
            <span>🏢 ${message}</span>
            <button onclick="this.parentElement.remove()" style="background: none; border: none; color: white; font-size: 1.2em; cursor: pointer;">×</button>
        `;
        
        const bgColor = type === 'error' ? '#ef4444' : 
                       type === 'success' ? '#22c55e' : 
                       type === 'info' ? '#3b82f6' : '#f59e0b';
        
        notification.style.cssText = `
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 15px 25px;
            border-radius: 8px;
            color: white;
            z-index: 1000;
            display: flex;
            align-items: center;
            gap: 15px;
            max-width: 400px;
            box-shadow: 0 10px 25px rgba(0,0,0,0.2);
            background: ${bgColor};
            border-left: 4px solid rgba(255,255,255,0.3);
            font-family: inherit;
            animation: slideIn 0.3s ease-out;
        `;
        
        // Add animation
        if (!document.getElementById('notification-styles')) {
            const animationStyles = document.createElement('style');
            animationStyles.id = 'notification-styles';
            animationStyles.textContent = `
                @keyframes slideIn {
                    from { transform: translateX(100%); opacity: 0; }
                    to { transform: translateX(0); opacity: 1; }
                }
            `;
            document.head.appendChild(animationStyles);
        }
        
        document.body.appendChild(notification);
        
        // Auto remove after 6 seconds
        setTimeout(() => {
            if (notification.parentElement) {
                notification.style.animation = 'slideIn 0.3s ease-out reverse';
                setTimeout(() => notification.remove(), 300);
            }
        }, 6000);
    }
}

// Initialize Alpha Pi Omega Quantum Logos when script loads
const apoQuantumLogos = new APOQuantumLogos();

// Export for use in other scripts
if (typeof module !== 'undefined' && module.exports) {
    module.exports = APOQuantumLogos;
}

// Global access with Alpha Pi Omega branding
window.APOQuantumLogos = APOQuantumLogos;
window.apoQuantumLogos = apoQuantumLogos;
window.AlphaPiOmegaQuantumLogos = APOQuantumLogos;

// Alpha Pi Omega Corporation startup message
console.log(`
🏢 Alpha Pi Omega Corporation
🌐 Website: www.alphapiomega.com
🌟 APO Quantum Logos v1.0.0-regenerative
🌱 Solar-Powered Consciousness Analysis Platform
♻️  Carbon-Negative Technology
🚀 Deployed on Netlify
© 2024 Alpha Pi Omega Corp - Regenerative Innovation
`);