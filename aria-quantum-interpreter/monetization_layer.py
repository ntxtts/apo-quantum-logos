# 💰 ASTRO Quantum System - Monetization Layer
# Real-time usage tracking, billing, and subscription management

import json
import logging
from datetime import datetime, timedelta
from typing import Dict, Any, Optional, Tuple
import hashlib
import os

class MonetizationManager:
    """Handles subscription tiers, usage tracking, and billing"""
    
    # Subscription tiers and limits
    TIERS = {
        "free": {
            "monthly_limit": 100,
            "max_qubits": 4,
            "algorithms": ["basic", "hadamard", "bell_state"],
            "price": 0,
            "support": "community"
        },
        "starter": {
            "monthly_limit": 1000,
            "max_qubits": 8,
            "algorithms": ["basic", "hadamard", "bell_state", "grover", "deutsch_jozsa"],
            "price": 99,
            "support": "email"
        },
        "professional": {
            "monthly_limit": 10000,
            "max_qubits": 32,
            "algorithms": ["all"],
            "price": 499,
            "support": "priority"
        },
        "enterprise": {
            "monthly_limit": -1,  # unlimited
            "max_qubits": 128,
            "algorithms": ["all", "custom"],
            "price": 2499,
            "support": "dedicated"
        }
    }
    
    # Pay-per-use pricing (cents)
    PAY_PER_USE = {
        "basic_operation": 10,      # $0.10
        "complex_algorithm": 100,   # $1.00
        "circuit_simulation": 50,   # $0.50
        "state_analysis": 25,       # $0.25
        "custom_algorithm": 500     # $5.00
    }
    
    def __init__(self, storage_connection_string: str = None):
        self.storage_connection = storage_connection_string
        self.usage_cache = {}  # In-memory cache for current month
        
    def authenticate_user(self, api_key: str) -> Optional[Dict[str, Any]]:
        """Authenticate user and return subscription info"""
        # In production, this would query your user database
        # For demo, we'll use a simple hash-based system
        
        demo_users = {
            "demo_free": {
                "user_id": "user_001",
                "tier": "free",
                "api_key": "sk_test_free_" + hashlib.md5("demo_free".encode()).hexdigest()[:16],
                "monthly_usage": 25,  # Used 25 out of 100
                "last_reset": datetime.now().strftime("%Y-%m")
            },
            "demo_starter": {
                "user_id": "user_002", 
                "tier": "starter",
                "api_key": "sk_test_starter_" + hashlib.md5("demo_starter".encode()).hexdigest()[:16],
                "monthly_usage": 245,  # Used 245 out of 1000
                "last_reset": datetime.now().strftime("%Y-%m")
            },
            "demo_pro": {
                "user_id": "user_003",
                "tier": "professional",
                "api_key": "sk_test_pro_" + hashlib.md5("demo_pro".encode()).hexdigest()[:16],
                "monthly_usage": 1250,  # Used 1250 out of 10000
                "last_reset": datetime.now().strftime("%Y-%m")
            }
        }
        
        # Find user by API key
        for username, user_data in demo_users.items():
            if user_data["api_key"] == api_key:
                return user_data
                
        return None
    
    def check_usage_limits(self, user_data: Dict[str, Any], operation_type: str) -> Tuple[bool, str]:
        """Check if user can perform the requested operation"""
        tier = user_data["tier"]
        tier_config = self.TIERS[tier]
        
        # Check monthly limits
        if tier_config["monthly_limit"] != -1:  # Not unlimited
            if user_data["monthly_usage"] >= tier_config["monthly_limit"]:
                return False, f"Monthly limit of {tier_config['monthly_limit']} operations exceeded"
        
        # Check algorithm access
        if operation_type not in ["basic", "hadamard", "bell_state"] and "all" not in tier_config["algorithms"]:
            if operation_type not in tier_config["algorithms"]:
                return False, f"Algorithm '{operation_type}' not available in {tier} tier"
        
        return True, "OK"
    
    def calculate_usage_cost(self, operation_type: str, complexity: int = 1) -> int:
        """Calculate cost in cents for pay-per-use model"""
        base_cost = self.PAY_PER_USE.get(operation_type, self.PAY_PER_USE["basic_operation"])
        return base_cost * complexity
    
    def track_usage(self, user_id: str, operation_type: str, qubits_used: int = 1, success: bool = True) -> Dict[str, Any]:
        """Track usage and generate billing record"""
        timestamp = datetime.now()
        
        usage_record = {
            "user_id": user_id,
            "timestamp": timestamp.isoformat(),
            "operation_type": operation_type,
            "qubits_used": qubits_used,
            "success": success,
            "cost_cents": self.calculate_usage_cost(operation_type, qubits_used) if success else 0
        }
        
        # In production, save to Azure Table Storage or Cosmos DB
        logging.info(f"Usage tracked: {json.dumps(usage_record)}")
        
        return usage_record
    
    def get_user_dashboard_data(self, user_data: Dict[str, Any]) -> Dict[str, Any]:
        """Generate dashboard data for user"""
        tier = user_data["tier"]
        tier_config = self.TIERS[tier]
        
        # Calculate usage percentage
        if tier_config["monthly_limit"] == -1:
            usage_percentage = 0  # Unlimited
        else:
            usage_percentage = (user_data["monthly_usage"] / tier_config["monthly_limit"]) * 100
        
        return {
            "user_id": user_data["user_id"],
            "subscription_tier": tier,
            "monthly_usage": user_data["monthly_usage"],
            "monthly_limit": tier_config["monthly_limit"],
            "usage_percentage": min(usage_percentage, 100),
            "available_algorithms": tier_config["algorithms"],
            "max_qubits": tier_config["max_qubits"],
            "support_level": tier_config["support"],
            "monthly_cost": tier_config["price"],
            "next_billing_date": self._get_next_billing_date(),
            "upgrade_benefits": self._get_upgrade_benefits(tier)
        }
    
    def _get_next_billing_date(self) -> str:
        """Calculate next billing date"""
        now = datetime.now()
        next_month = now.replace(day=1) + timedelta(days=32)
        return next_month.replace(day=1).strftime("%Y-%m-%d")
    
    def _get_upgrade_benefits(self, current_tier: str) -> Dict[str, Any]:
        """Show benefits of upgrading to next tier"""
        tier_order = ["free", "starter", "professional", "enterprise"]
        
        if current_tier == "enterprise":
            return {"message": "You're on our highest tier!"}
        
        current_index = tier_order.index(current_tier)
        next_tier = tier_order[current_index + 1]
        next_config = self.TIERS[next_tier]
        
        return {
            "next_tier": next_tier,
            "additional_operations": next_config["monthly_limit"] - self.TIERS[current_tier]["monthly_limit"] if next_config["monthly_limit"] != -1 else "unlimited",
            "additional_qubits": next_config["max_qubits"] - self.TIERS[current_tier]["max_qubits"],
            "new_algorithms": list(set(next_config["algorithms"]) - set(self.TIERS[current_tier]["algorithms"])),
            "monthly_cost": next_config["price"],
            "upgrade_link": f"/upgrade?to={next_tier}"
        }

class RevenueAnalytics:
    """Analytics for revenue tracking and forecasting"""
    
    def __init__(self):
        self.demo_data = self._generate_demo_analytics()
    
    def _generate_demo_analytics(self) -> Dict[str, Any]:
        """Generate realistic demo analytics data"""
        return {
            "monthly_revenue": {
                "current_month": 12750,  # $127.50
                "last_month": 8920,     # $89.20
                "growth_rate": 42.9     # 42.9% growth
            },
            "user_metrics": {
                "total_users": 47,
                "active_users": 34,
                "free_tier": 28,
                "starter_tier": 12,
                "professional_tier": 6,
                "enterprise_tier": 1
            },
            "usage_metrics": {
                "total_operations": 15420,
                "successful_operations": 14891,
                "success_rate": 96.6,
                "avg_qubits_per_operation": 3.2
            },
            "top_algorithms": [
                {"name": "hadamard", "usage": 4521, "revenue": 2260},
                {"name": "grover", "usage": 3210, "revenue": 6420},
                {"name": "bell_state", "usage": 2890, "revenue": 1445},
                {"name": "deutsch_jozsa", "usage": 1654, "revenue": 3308}
            ]
        }
    
    def get_revenue_dashboard(self) -> Dict[str, Any]:
        """Get comprehensive revenue dashboard data"""
        return {
            "summary": self.demo_data,
            "projections": {
                "next_month_revenue": 18050,  # 42% growth continued
                "quarterly_target": 45000,
                "annual_projection": 180000
            },
            "conversion_opportunities": [
                {"tier": "free_to_starter", "potential_users": 15, "potential_revenue": 1485},
                {"tier": "starter_to_pro", "potential_users": 4, "potential_revenue": 1600},
                {"tier": "pro_to_enterprise", "potential_users": 2, "potential_revenue": 4000}
            ]
        }

# API Key Generator for Demo
def generate_demo_api_keys() -> Dict[str, str]:
    """Generate demo API keys for testing"""
    return {
        "free_tier": "sk_test_free_" + hashlib.md5("demo_free".encode()).hexdigest()[:16],
        "starter_tier": "sk_test_starter_" + hashlib.md5("demo_starter".encode()).hexdigest()[:16], 
        "professional_tier": "sk_test_pro_" + hashlib.md5("demo_pro".encode()).hexdigest()[:16]
    }

if __name__ == "__main__":
    # Demo usage
    print("🚀 ASTRO Quantum Monetization Demo")
    print("=" * 50)
    
    # Generate demo API keys
    api_keys = generate_demo_api_keys()
    print("\n📊 Demo API Keys:")
    for tier, key in api_keys.items():
        print(f"{tier}: {key}")
    
    # Test monetization manager
    monetization = MonetizationManager()
    
    # Test user authentication and dashboard
    test_key = api_keys["starter_tier"]
    user_data = monetization.authenticate_user(test_key)
    
    if user_data:
        print(f"\n✅ User authenticated: {user_data['tier']} tier")
        dashboard = monetization.get_user_dashboard_data(user_data)
        print(f"📈 Usage: {dashboard['usage_percentage']:.1f}% of monthly limit")
        print(f"💰 Monthly cost: ${dashboard['monthly_cost']}")
    
    # Test revenue analytics
    analytics = RevenueAnalytics()
    revenue_data = analytics.get_revenue_dashboard()
    print(f"\n💵 Current Monthly Revenue: ${revenue_data['summary']['monthly_revenue']['current_month']:,}")
    print(f"📊 Growth Rate: {revenue_data['summary']['monthly_revenue']['growth_rate']}%")
    print(f"🎯 Annual Projection: ${revenue_data['projections']['annual_projection']:,}")
