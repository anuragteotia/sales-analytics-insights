import pandas as pd

try:
    df = pd.read_excel('SQL_Sales_Dataset_200_Rows.xlsx')
except FileNotFoundError:
    data = {
        'order_id': [101, 102, 103, 104, 105],
        'customer_name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
        'total_price': [500, 300, 700, 200, 400]
    }
    df = pd.DataFrame(data)
    print("--- Using sample data (File not found) ---")

# 2. Analyze: Top Customers (by total spend)
top_customers = df.groupby('customer_name')[
    'total_price'].sum().sort_values(ascending=False).head(5)

# 3. Analyze: Average Order Value (AOV)
total_revenue = df['total_price'].sum()
total_unique_orders = df['order_id'].nunique()
aov = total_revenue / total_unique_orders

# 4. Display Results
print("\n--- TOP CUSTOMERS ---")
print(top_customers)

print(f"\n--- AVERAGE ORDER VALUE ---")
print(f"Total Revenue: {total_revenue}")
print(f"Total Unique Orders: {total_unique_orders}")
print(f"AOV: {aov:.2f}")

# 5. Export to Excel (Optional: Good for showing your manager)
top_customers.to_excel('top_customers.xlsx')
print("\nResults saved to 'top_customers.xlsx'")
