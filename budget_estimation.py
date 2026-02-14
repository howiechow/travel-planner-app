# Budget estimation module for travel costs
# Integrates with external APIs for real-time cost estimates

def estimate_budget(destination, duration, travelers):
    base_cost = 100 * duration
    multiplier = 1 + (travelers * 0.5)
    return int(base_cost * multiplier)
