import random

# Simulation Parameters
days = 7  # Simulate for 7 days
min_demand = 5  # Minimum daily customer demand
max_demand = 20  # Maximum daily customer demand
production_margin = 1.2  # Produce 20% more than predicted demand
price_per_cheesecake = 600  # Selling price per cheesecake
cost_per_cheesecake = 400  # Cost to produce each cheesecake

# Data Storage
daily_demand = []
daily_production = []
daily_sales = []
daily_inventory = []
daily_waste = []

# Simulation Loop
for day in range(days):
    # Step 1: Demand Forecasting
    demand = random.randint(min_demand, max_demand)
    daily_demand.append(demand)
    
    # Step 2: Production Planning
    production = int(demand * production_margin)
    daily_production.append(production)
    
    # Step 3: Inventory and Sales
    inventory = production
    sales = min(demand, inventory)
    inventory -= sales
    waste = inventory  # Unsold items are considered waste
    
    daily_sales.append(sales)
    daily_inventory.append(inventory)
    daily_waste.append(waste)
    
    # Output for each day
    print(f"Day {day+1}:")
    print(f"  Demand: {demand}")
    print(f"  Production: {production}")
    print(f"  Sales: {sales}")
    print(f"  Waste: {waste}")
    print(f"  Inventory End of Day: {inventory}\n")

# Performance Metrics
total_sales = sum(daily_sales)
total_waste = sum(daily_waste)
revenue = total_sales * price_per_cheesecake
costs = sum(daily_production) * cost_per_cheesecake
profit = revenue - costs

print("\n--- Performance Summary ---")
print(f"Total Sales: {total_sales} cheesecakes")
print(f"Total Waste: {total_waste} cheesecakes")
print(f"Total Revenue: PHP {revenue}")
print(f"Total Costs: PHP {costs}")
print(f"Net Profit: PHP {profit}")
