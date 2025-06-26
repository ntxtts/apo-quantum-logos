"""
Alpha Pi Omega - Quantum Computing Enhancement Platform
Commercial Quantum Amplification Technology
Paulo G Morales - paulmorales@ntxtts.com
"""

from flask import Flask, request, jsonify, render_template_string
from flask_cors import CORS
import hashlib
from datetime import datetime
import json
import threading
import time

# Import quantum computing platform
try:
    from apo_quantum_computing import quantum_marketplace, get_quantum_product_catalog
    QUANTUM_PLATFORM_AVAILABLE = True
    print("🔬 Quantum Computing Platform imported successfully")
except Exception as e:
    QUANTUM_PLATFORM_AVAILABLE = False
    print(f"⚠️ Quantum Platform not available: {e}")

# Try to import agent mode
try:
    from apo_agent_mode import apo_agent, initialize_agent_mode
    AGENT_MODE_AVAILABLE = True
    print("🤖 Agent Mode imported successfully")
except Exception as e:
    AGENT_MODE_AVAILABLE = False
    print(f"⚠️ Agent Mode not available: {e}")

app = Flask(__name__)
CORS(app)

# Store for simple user management (use database in production)
users = {}
analyses = {}

# Agent mode status
agent_active = False

def start_agent_mode():
    """Start the intelligent agent system"""
    global agent_active
    if AGENT_MODE_AVAILABLE and not agent_active:
        success = initialize_agent_mode()
        if success:
            agent_active = True
            print("🚀 APO Agent Mode is now ACTIVE!")
            return True
    return False

# Start agent mode in background
if AGENT_MODE_AVAILABLE:
    threading.Thread(target=start_agent_mode, daemon=True).start()

@app.route('/')
def home():
    """Main Alpha Pi Omega page with WORKING functionality"""
    return render_template_string('''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Alpha Pi Omega - Working Platform</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 0; padding: 20px; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: white; }
        .container { max-width: 1000px; margin: 0 auto; }
        .hero { text-align: center; padding: 40px 0; }
        .section { background: rgba(255,255,255,0.1); margin: 20px 0; padding: 30px; border-radius: 15px; }
        .form-group { margin: 15px 0; }
        .form-control { width: 100%; padding: 12px; border: none; border-radius: 8px; font-size: 16px; }
        .btn { background: #4ade80; color: white; padding: 15px 30px; border: none; border-radius: 10px; cursor: pointer; font-size: 16px; }
        .btn:hover { background: #22c55e; }
        .result { background: rgba(255,255,255,0.2); padding: 20px; margin: 20px 0; border-radius: 10px; }
        .pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; margin: 20px 0; }
        .pricing-card { background: rgba(255,255,255,0.1); padding: 25px; border-radius: 12px; text-align: center; }
        .price { font-size: 2.5em; margin: 15px 0; color: #4ade80; }
    </style>
</head>
<body>
    <div class="container">
        <div class="hero">
            <h1>🌟 Alpha Pi Omega Corporation</h1>
            <h2>Solar-Powered Business Text Analysis</h2>
            <p>Real-time analysis that actually works!</p>
        </div>

        <div class="section">
            <h3>🤖 Agent Mode Status</h3>
            <div id="agentStatus" class="result">
                <p>🔄 Checking Agent Mode status...</p>
            </div>
            <button class="btn" onclick="toggleAgentMode()" id="agentToggle">🤖 Activate Agent Mode</button>
            <button class="btn" onclick="getAgentDashboard()" style="margin-left: 10px;">📊 Agent Dashboard</button>
        </div>

        <div class="section">
            <h3>🚀 Live Text Analysis</h3>
            <p>Try our working text analysis engine:</p>
            
            <div class="form-group">
                <textarea id="analysisText" class="form-control" rows="4" placeholder="Enter your business text to analyze..."></textarea>
            </div>
            
            <div class="form-group">
                <select id="analysisType" class="form-control">
                    <option value="business">Business Communication</option>
                    <option value="marketing">Marketing Copy</option>
                    <option value="customer_service">Customer Service</option>
                    <option value="technical">Technical Documentation</option>
                </select>
            </div>
            
            <button class="btn" onclick="analyzeText()">🧮 Analyze Text Now</button>
            
            <div id="analysisResult"></div>
        </div>

        <div class="section">
            <h3>💰 Working Pricing Plans</h3>
            <div class="pricing-grid">
                <div class="pricing-card">
                    <h4>🎁 Free Trial</h4>
                    <div class="price">$0</div>
                    <p>10 analyses per month</p>
                    <ul>
                        <li>Basic sentiment analysis</li>
                        <li>Clarity scoring</li>
                        <li>Email support</li>
                    </ul>
                    <button class="btn" onclick="signupPlan('free')">Start Free Trial</button>
                </div>
                
                <div class="pricing-card">
                    <h4>💼 Professional</h4>
                    <div class="price">$29</div>
                    <p>100 analyses per month</p>
                    <ul>
                        <li>Advanced analysis</li>
                        <li>Team collaboration</li>
                        <li>API access</li>
                        <li>Priority support</li>
                    </ul>
                    <button class="btn" onclick="signupPlan('professional')">Choose Professional</button>
                </div>
                
                <div class="pricing-card">
                    <h4>🏢 Enterprise</h4>
                    <div class="price">$99</div>
                    <p>Unlimited analyses</p>
                    <ul>
                        <li>Everything in Pro</li>
                        <li>Custom integrations</li>
                        <li>Dedicated support</li>
                        <li>SLA guarantee</li>
                    </ul>
                    <button class="btn" onclick="signupPlan('enterprise')">Contact Sales</button>
                </div>
            </div>
        </div>

        <div class="section">
            <h3>📧 Business Contact</h3>
            <p><strong>Founder & CEO:</strong> Paulo G Morales</p>
            <p><strong>Email:</strong> paulmorales@ntxtts.com</p>
            <p><strong>Corporation:</strong> Alpha Pi Omega Corp</p>
            <p><strong>Website:</strong> www.alphapiomega.com</p>
        </div>
    </div>

    <script>
        // Check agent status on page load
        checkAgentStatus();
        
        async function checkAgentStatus() {
            try {
                const response = await fetch('/api/agent/status');
                const result = await response.json();
                
                const statusDiv = document.getElementById('agentStatus');
                const toggleBtn = document.getElementById('agentToggle');
                
                if (result.status === 'active') {
                    statusDiv.innerHTML = `
                        <div style="color: #4ade80;">
                            <h4>🤖 Agent Mode: ACTIVE</h4>
                            <p><strong>Performance Score:</strong> ${result.performance_score}/100</p>
                            <p><strong>Active Optimizations:</strong> ${result.optimization_count}</p>
                            <p><strong>Decisions Made:</strong> ${Object.values(result.recent_decisions || {}).reduce((a, b) => a + b, 0)}</p>
                            <p><em>Autonomous AI optimization running...</em></p>
                        </div>
                    `;
                    toggleBtn.textContent = '🛑 Deactivate Agent Mode';
                    toggleBtn.style.background = '#ef4444';
                } else {
                    statusDiv.innerHTML = `
                        <div style="color: #fbbf24;">
                            <h4>🤖 Agent Mode: INACTIVE</h4>
                            <p>Click to activate intelligent automation and monitoring</p>
                        </div>
                    `;
                    toggleBtn.textContent = '🤖 Activate Agent Mode';
                    toggleBtn.style.background = '#4ade80';
                }
            } catch (error) {
                document.getElementById('agentStatus').innerHTML = '<p style="color: #ef4444;">❌ Agent Mode not available</p>';
            }
        }
        
        async function toggleAgentMode() {
            const response = await fetch('/api/agent/toggle', {method: 'POST'});
            const result = await response.json();
            
            if (result.success) {
                checkAgentStatus();
                alert(`✅ Agent Mode ${result.new_status}`);
            } else {
                alert(`❌ Failed to toggle Agent Mode: ${result.error}`);
            }
        }
        
        async function getAgentDashboard() {
            try {
                const response = await fetch('/api/agent/dashboard');
                const result = await response.json();
                
                const dashboard = `
                    <div class="result">
                        <h4>📊 Agent Dashboard</h4>
                        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 15px;">
                            <div style="background: rgba(34, 197, 94, 0.1); padding: 15px; border-radius: 8px;">
                                <h5>⚡ Performance</h5>
                                <p>Score: ${result.performance_score}/100</p>
                                <p>Uptime: ${result.uptime}</p>
                            </div>
                            <div style="background: rgba(59, 130, 246, 0.1); padding: 15px; border-radius: 8px;">
                                <h5>🧠 Decisions</h5>
                                <p>Total: ${Object.values(result.recent_decisions || {}).reduce((a, b) => a + b, 0)}</p>
                                <p>Optimizations: ${result.optimization_count}</p>
                            </div>
                            <div style="background: rgba(168, 85, 247, 0.1); padding: 15px; border-radius: 8px;">
                                <h5>🎯 Capabilities</h5>
                                <p>Active: ${Object.values(result.capabilities || {}).filter(c => c).length}</p>
                                <p>Total: ${Object.keys(result.capabilities || {}).length}</p>
                            </div>
                        </div>
                        <h5>🔧 Recent Metrics:</h5>
                        <ul>
                            ${Object.entries(result.recent_metrics || {}).map(([key, value]) => 
                                `<li><strong>${key}:</strong> ${value.average?.toFixed(3)} (${value.count} samples)</li>`
                            ).join('')}
                        </ul>
                    </div>
                `;
                
                document.getElementById('agentStatus').innerHTML = dashboard;
            } catch (error) {
                alert('❌ Failed to load Agent Dashboard');
            }
        }
        
        async function analyzeText() {
            const text = document.getElementById('analysisText').value;
            const type = document.getElementById('analysisType').value;
            const resultDiv = document.getElementById('analysisResult');
            
            if (!text.trim()) {
                alert('Please enter some text to analyze!');
                return;
            }
            
            resultDiv.innerHTML = '<p>🔄 Analyzing your text...</p>';
            
            try {
                const response = await fetch('/api/analyze', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({text: text, type: type})
                });
                
                const result = await response.json();
                
                resultDiv.innerHTML = `
                    <div class="result">
                        <h4>📊 Analysis Results</h4>
                        <p><strong>Text Length:</strong> ${result.word_count} words, ${result.character_count} characters</p>
                        <p><strong>Sentiment Score:</strong> ${result.sentiment_score} (${result.sentiment_label})</p>
                        <p><strong>Clarity Rating:</strong> ${result.clarity_rating}/10</p>
                        <p><strong>Business Impact:</strong> ${result.business_impact}/10</p>
                        <p><strong>Overall Grade:</strong> ${result.grade}</p>
                        <h5>💡 Recommendations:</h5>
                        <ul>${result.recommendations.map(r => '<li>' + r + '</li>').join('')}</ul>
                        <p><em>Analysis by Alpha Pi Omega Corporation - Solar-powered technology</em></p>
                    </div>
                `;
            } catch (error) {
                resultDiv.innerHTML = '<p style="color: #ff6b6b;">❌ Error analyzing text. Please try again.</p>';
            }
        }
        
        function signupPlan(plan) {
            const email = prompt(`Enter your email to sign up for the ${plan} plan:`);
            if (email) {
                fetch('/api/signup', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({email: email, plan: plan})
                })
                .then(response => response.json())
                .then(result => {
                    alert(`✅ Thanks for signing up! We'll contact you at ${email} about the ${plan} plan.`);
                });
            }
        }
        
        async function toggleAgentMode() {
            const button = document.getElementById('agentToggle');
            const statusDiv = document.getElementById('agentStatus');
            
            if (button.innerText.includes('Activate')) {
                // Activate agent mode
                statusDiv.innerHTML = '<p>🔄 Activating Agent Mode...</p>';
                
                const response = await fetch('/api/agent/activate', {method: 'POST'});
                const result = await response.json();
                
                if (result.success) {
                    button.innerText = '🤖 Deactivate Agent Mode';
                    statusDiv.innerHTML = '<p>✅ Agent Mode is now ACTIVE!</p>';
                } else {
                    statusDiv.innerHTML = `<p style="color: #ff6b6b;">❌ ${result.error}</p>`;
                }
            } else {
                // Deactivate agent mode
                statusDiv.innerHTML = '<p>🔄 Deactivating Agent Mode...</p>';
                
                const response = await fetch('/api/agent/deactivate', {method: 'POST'});
                const result = await response.json();
                
                if (result.success) {
                    button.innerText = '🤖 Activate Agent Mode';
                    statusDiv.innerHTML = '<p>✅ Agent Mode is now INACTIVE.</p>';
                } else {
                    statusDiv.innerHTML = `<p style="color: #ff6b6b;">❌ ${result.error}</p>`;
                }
            }
        }
        
        async function getAgentDashboard() {
            const response = await fetch('/api/agent/dashboard');
            const dashboard = await response.json();
            
            const dashboardHtml = `
                <h4>🤖 Agent Dashboard</h4>
                <p><strong>Status:</strong> ${dashboard.status}</p>
                <p><strong>Uptime:</strong> ${dashboard.uptime} seconds</p>
                <p><strong>Actions Taken:</strong> ${dashboard.actions_taken}</p>
                <h5>Recent Activities:</h5>
                <ul>${dashboard.recent_activities.map(a => '<li>' + a + '</li>').join('')}</ul>
            `;
            
            document.getElementById('agentStatus').innerHTML = dashboardHtml;
        }
    </script>
</body>
</html>
    ''')

@app.route('/api/analyze', methods=['POST'])
def analyze_text():
    """Working text analysis API"""
    data = request.get_json()
    text = data.get('text', '')
    analysis_type = data.get('type', 'business')
    
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    # Real analysis logic
    word_count = len(text.split())
    char_count = len(text)
    
    # Sentiment analysis
    positive_words = ['good', 'great', 'excellent', 'amazing', 'fantastic', 'wonderful', 'perfect', 'outstanding']
    negative_words = ['bad', 'terrible', 'awful', 'horrible', 'disappointing', 'poor', 'worst']
    
    positive_score = sum(1 for word in positive_words if word in text.lower())
    negative_score = sum(1 for word in negative_words if word in text.lower())
    
    sentiment_score = (positive_score - negative_score) / max(word_count / 10, 1)
    sentiment_score = max(-1, min(1, sentiment_score))
    
    if sentiment_score > 0.3:
        sentiment_label = "Positive"
    elif sentiment_score < -0.3:
        sentiment_label = "Negative"
    else:
        sentiment_label = "Neutral"
    
    # Clarity rating
    sentences = text.count('.') + text.count('!') + text.count('?')
    avg_sentence_length = word_count / max(sentences, 1)
    clarity_rating = min(10, max(1, 10 - (avg_sentence_length / 10)))
    
    # Business impact
    business_keywords = ['customer', 'sales', 'revenue', 'profit', 'growth', 'team', 'success', 'solution']
    business_score = sum(1 for word in business_keywords if word in text.lower())
    business_impact = min(10, business_score * 1.5)
    
    # Overall grade
    overall_score = (sentiment_score + 1) * 5 + clarity_rating / 2 + business_impact / 2
    if overall_score >= 12:
        grade = "A+"
    elif overall_score >= 10:
        grade = "A"
    elif overall_score >= 8:
        grade = "B+"
    elif overall_score >= 6:
        grade = "B"
    else:
        grade = "C"
    
    # Recommendations
    recommendations = []
    if sentiment_score < 0:
        recommendations.append("Consider using more positive language")
    if clarity_rating < 7:
        recommendations.append("Try shorter, simpler sentences")
    if business_impact < 5:
        recommendations.append("Include more business-focused keywords")
    if not recommendations:
        recommendations.append("Great job! Your text is well-optimized")
    
    # Store analysis
    analysis_id = hashlib.md5(text.encode()).hexdigest()[:8]
    analyses[analysis_id] = {
        'text': text,
        'results': {
            'word_count': word_count,
            'character_count': char_count,
            'sentiment_score': round(sentiment_score, 3),
            'sentiment_label': sentiment_label,
            'clarity_rating': round(clarity_rating, 1),
            'business_impact': round(business_impact, 1),
            'grade': grade,
            'recommendations': recommendations
        },
        'timestamp': datetime.now().isoformat(),
        'type': analysis_type
    }
    
    return jsonify({
        'analysis_id': analysis_id,
        'word_count': word_count,
        'character_count': char_count,
        'sentiment_score': round(sentiment_score, 3),
        'sentiment_label': sentiment_label,
        'clarity_rating': round(clarity_rating, 1),
        'business_impact': round(business_impact, 1),
        'grade': grade,
        'recommendations': recommendations,
        'corporation': 'Alpha Pi Omega Corp',
        'contact': 'paulmorales@ntxtts.com'
    })

@app.route('/api/signup', methods=['POST'])
def signup():
    """Working signup API"""
    data = request.get_json()
    email = data.get('email', '')
    plan = data.get('plan', 'free')
    
    users[email] = {
        'plan': plan,
        'signup_date': datetime.now().isoformat(),
        'analyses_used': 0
    }
    
    return jsonify({
        'message': f'Successfully signed up for {plan} plan',
        'email': email,
        'corporation': 'Alpha Pi Omega Corp',
        'contact': 'paulmorales@ntxtts.com'
    })

@app.route('/api/health')
def health():
    """API health check"""
    return jsonify({
        'status': 'operational',
        'service': 'Alpha Pi Omega Text Analysis API',
        'corporation': 'Alpha Pi Omega Corp',
        'owner': 'Paul Morales',
        'contact': 'paulmorales@ntxtts.com',
        'features': ['text_analysis', 'sentiment_scoring', 'business_optimization'],
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/agent/activate', methods=['POST'])
def activate_agent():
    """Activate Agent Mode"""
    global agent_active
    if AGENT_MODE_AVAILABLE:
        agent_active = True
        return jsonify({'success': True})
    return jsonify({'success': False, 'error': 'Agent Mode not available'}), 500

@app.route('/api/agent/deactivate', methods=['POST'])
def deactivate_agent():
    """Deactivate Agent Mode"""
    global agent_active
    agent_active = False
    return jsonify({'success': True})

@app.route('/api/agent/status')
def agent_status():
    """Get current agent mode status"""
    if AGENT_MODE_AVAILABLE and agent_active:
        try {
            status = apo_agent.get_agent_status()
            return jsonify({
                'status': status['status'],
                'performance_score': status['performance_score'],
                'capabilities': status['capabilities'],
                'recent_metrics': status['recent_metrics'],
                'recent_decisions': status['recent_decisions'],
                'optimization_count': status['optimization_count'],
                'uptime': status['uptime'],
                'corporation': 'Alpha Pi Omega Corp',
                'agent_version': '1.0.0'
            })
        } except Exception as e {
            return jsonify({
                'status': 'error',
                'error': str(e),
                'corporation': 'Alpha Pi Omega Corp'
            }), 500
    } else {
        return jsonify({
            'status': 'inactive',
            'message': 'Agent mode not available or not started',
            'corporation': 'Alpha Pi Omega Corp'
        })
    }
})

@app.route('/api/agent/toggle', methods=['POST'])
def toggle_agent():
    """Toggle agent mode on/off"""
    global agent_active
    
    if not AGENT_MODE_AVAILABLE:
        return jsonify({
            'success': False,
            'error': 'Agent mode not available',
            'corporation': 'Alpha Pi Omega Corp'
        })
    
    try {
        if agent_active {
            # Stop agent mode
            apo_agent.agent_status = "inactive"
            agent_active = False
            new_status = "deactivated"
        } else {
            # Start agent mode
            success = start_agent_mode()
            new_status = "activated" if success else "failed"
        }
        
        return jsonify({
            'success': True,
            'new_status': new_status,
            'corporation': 'Alpha Pi Omega Corp',
            'contact': 'paulmorales@ntxtts.com'
        })
    
    } except Exception as e {
        return jsonify({
            'success': False,
            'error': str(e),
            'corporation': 'Alpha Pi Omega Corp'
        }), 500
    }
})

@app.route('/api/agent/dashboard')
def agent_dashboard():
    """Get detailed agent dashboard data"""
    if AGENT_MODE_AVAILABLE and agent_active:
        try {
            status = apo_agent.get_agent_status()
            return jsonify(status)
        } except Exception as e {
            return jsonify({
                'error': str(e),
                'corporation': 'Alpha Pi Omega Corp'
            }), 500
    } else {
        return jsonify({
            'error': 'Agent mode not active',
            'corporation': 'Alpha Pi Omega Corp'
        }), 503
    }
})

@app.route('/api/agent/metrics')
def agent_metrics():
    """Get real-time agent metrics"""
    if AGENT_MODE_AVAILABLE and agent_active:
        try {
            metrics = apo_agent.collect_performance_metrics()
            return jsonify({
                'metrics': metrics,
                'timestamp': datetime.now().isoformat(),
                'corporation': 'Alpha Pi Omega Corp'
            })
        } except Exception as e {
            return jsonify({
                'error': str(e),
                'corporation': 'Alpha Pi Omega Corp'
            }), 500
    } else {
        return jsonify({
            'error': 'Agent mode not active',
            'corporation': 'Alpha Pi Omega Corp'
        }), 503
    }
})

@app.route('/api/health')
def health():
    """API health check"""
    return jsonify({
        'status': 'operational',
        'service': 'Alpha Pi Omega Text Analysis API',
        'corporation': 'Alpha Pi Omega Corp',
        'owner': 'Paul Morales',
        'contact': 'paulmorales@ntxtts.com',
        'features': ['text_analysis', 'sentiment_scoring', 'business_optimization'],
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    print("🚀 Starting Alpha Pi Omega WORKING API...")
    print("🌐 Live at: http://localhost:5000")
    print("👨‍💼 Founder & CEO: Paulo G Morales (paulmorales@ntxtts.com)")
    print("🏢 Corporation: Alpha Pi Omega Corp")
    app.run(debug=True, host='0.0.0.0', port=5000)