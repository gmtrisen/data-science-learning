# Used to summarize data in a structured table format
import pandas as pd

data = {
        "Department": ["IT", "IT", "HR", "HR", "IT", "HR"],
    "Gender": ["M", "F", "F", "M", "M", "F"],
    "Salary": [50000, 60000, 45000, 48000, 70000, 52000]
}
df = pd.DataFrame(data)
print(df)

# BASIC PIVOT TABLE
# pivot = df.pivot_table(
#     values="Salary",
#     index="Department",
#     aggfunc="mean"
# )
# print(pivot)

# Pivot with rows and columns
pivot = df.pivot_table(
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean"
)
print(pivot)

pivot = df.pivot_table(
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc=["mean","sum"]
)
print(pivot)

# Add Totals(Margins)
pivot = df.pivot_table(
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean",
    margins=True
)
print(pivot)

# Handling missing values in pivot
pivot = df.pivot_table(
    values="Salary",
    index="Department",
    columns="Gender",
    aggfunc="mean",
    fill_value=0
)
print(pivot)

# What is reshapping
# Reshapping changes the shape of the DataFrame
# Wide format → Long format
# Long format → Wide format

# Stack - wide to long
# Unstack - long to wide

# Wide format → Long format(melt())
wide_df = pd.DataFrame({
    "Name":["Alice","Bob"],
    "Math":[80,90],
    "Science":[85,88]
})

long_df = pd.melt(
    wide_df,
    id_vars="Name",
    var_name="Subject",
    value_name="Score"
)
print(long_df)
