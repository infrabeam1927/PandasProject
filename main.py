

import pandas as pd


sales = pd.DataFrame(
    {
        "product": ["Notebook", "Pen", "Notebook", "Pencil", "Pen"],
        "quantity": [3, 10, 2, 5, 4],
        "unit_price": [4.50, 1.25, 4.50, 0.75, 1.25],
    }
)
sales["total"] = sales["quantity"] * sales["unit_price"]

summary = sales.groupby("product", as_index=False)["total"].sum()
summary = summary.sort_values("total", ascending=False)

print("Sales data:")
print(sales.to_string(index=False))
print("\nRevenue by product:")
print(summary.to_string(index=False))

summary.to_excel("sales_summary.xlsx", index=False)
print("\nSaved summary to sales_summary.xlsx")
