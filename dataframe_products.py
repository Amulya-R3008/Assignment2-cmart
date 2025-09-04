import pandas as pd

# Create DataFrame of products
data = {
    "Product Name": ["Laptop", "Mobile", "Headphones", "Tablet", "Keyboard"],
    "Price": [60000, 15000, 2000, 25000, 500],
    "Category": ["Electronics", "Electronics", "Accessories", "Electronics", "Accessories"]
}

df = pd.DataFrame(data)

print("Original Products DataFrame:")
print(df)

# Add a new column - Discounted Price (90% of Price)
df["Discounted Price"] = df["Price"] * 0.9

print("\nDataFrame with Discounted Price:")
print(df)

# Filter products cheaper than 500
cheap_products = df[df["Discounted Price"] < 500]

print("\nProducts cheaper than 500 after discount:")
print(cheap_products)
