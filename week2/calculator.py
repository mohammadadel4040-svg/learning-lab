"""
Business Profit Calculator!
This program calculates profit and profit margin
based on revenue and cost entered by the user.
"""

# Get revenue input from user
revenue = float(input("Enter total revenue: $"))

# Get cost input from user
costs = float(input("Enter total costs: $"))

# Calculate profit
profit = revenue - costs

# Calculate profit margin percentage
margin = (profit / revenue) * 100

# Display results
print("\n--- Financial Summary ---")
print(f"Revenue: ${revenue:.2f}")
print(f"Costs: ${costs:.2f}")
print(f"Profit: ${profit:.2f}")
print(f"Profit Margin: {margin:.1f}%")
