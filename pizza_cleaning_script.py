# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 16:08:13 2024

@author: REMLEX
"""

import pandas as pd
from datetime import datetime
import seaborn as sns
import matplotlib.pyplot as plt

#Read the Excel files
pizza_sales_df = pd.read_excel('pizza_sales.xlsx')
pizza_sizes_df = pd.read_csv('pizza_size.csv')
pizza_categories_df = pd.read_csv('pizza_category.csv')


# Viewing top and bottom rows in a DataFrame
pizza_sales_df.head()  # Display first five rows
pizza_sales_df.head(10)  # Display first ten rows

pizza_sales_df.tail()  # Display last five rows
pizza_sales_df.tail(10)  # Display last ten rows


# Display the statistics of the details, by display summary
# Describing the data
pizza_sales_df.describe()  # Display for each numerical value
pizza_description = pizza_sales_df.describe()

# Have a look at non-null counts per column
pizza_sales_df.info()


# Count the number of null values in each column
null_count = pizza_sales_df.isnull().sum()

# Check for duplicated rows
duplicated_rows = pizza_sales_df.duplicated().sum()
print(duplicated_rows)

# To select a column
quantity_column = pizza_sales_df['quantity']
selected_columns = pizza_sales_df[['order_id','quantity','unit_price']]

# =============================================================================
# Select a specific rows and column by using LOC
# =============================================================================
# Get the row with index label 3
row = pizza_sales_df.loc[3]

# Get two rows, index label 3 and 5
rows = pizza_sales_df.loc[[3,5]]

# Get rows between, index label 3 and 5
subset = pizza_sales_df.loc[3:6]

# Get rows between, index label 3 and 5 and specifics columns
subset = pizza_sales_df.loc[3:6, ['quantity','unit_price']]

# Set an index as a column in a DataFrame
pizza_sales_df.set_index('order_details_id', inplace=True)

# Resetting an index
pizza_sales_df.reset_index(inplace=True)

# Truncate DataFrame before index 3
truncates_before = pizza_sales_df.truncate(before=3)

# Truncate DataFrame after index 5
truncates_after = pizza_sales_df.truncate(after=5)

# Truncate column
quantity_series = pizza_sales_df['quantity']

# Truncate series before index 3
truncated_series_before = quantity_series.truncate(before=3)

# Truncate series after index 5
truncated_series_after = quantity_series.truncate(after=3)

#  Basic Filtering
filtered_rows = pizza_sales_df[pizza_sales_df['unit_price'] > 20]

# Filtering on date
pizza_sales_df['order_date'] = pizza_sales_df['order_date'].dt.date

# change it to date format
date_target = datetime.strptime('2015-12-15', '%Y-%m-%d').date()
filtered_rows_by_date = pizza_sales_df[pizza_sales_df['order_date'] > date_target]

# Filtering on multiple conditions
# Using the and condition
bbq_chicken_rows = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) & 
                                  (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]


# Using the or condition (| symbol)
bbq_chicken_rows_or = pizza_sales_df[(pizza_sales_df['unit_price'] > 20) | 
                                  (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]

# Filtering a specific range
high_sales = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) & 
                            (pizza_sales_df['unit_price'] <= 20)]

high_sales2 = pizza_sales_df[(pizza_sales_df['unit_price'] > 15) & 
                            (pizza_sales_df['unit_price'] <= 20) &
                            (pizza_sales_df['pizza_name'] == 'The Barbecue Chicken Pizza')]

# =============================================================================
# Dropping null value
# =============================================================================

# pizza_sales_df is dataframe
pizza_sales_null_values_dropped = pizza_sales_df.dropna()
null_count = pizza_sales_null_values_dropped.isnull().sum()

# Replace null with a value
date_na_fill = datetime.strptime('2000-01-01', '%Y-%m-%d').date()
pizza_sales_null_replaced = pizza_sales_df.fillna(date_na_fill)

# Delete specific rows and columns in a DataFrame
filtered_rows_2 = pizza_sales_df.drop(2, axis=0) # axis =0 is rows and axis=1 is columns

# Deleting rows 5,7,9
filtered_rows_5_7_9 = pizza_sales_df.drop([5,7,9], axis=0) # axis =0 is rows and axis=1 is columns

# Delete a column by a column name
filtered_unit_price = pizza_sales_df.drop('unit_price', axis=1) # axis =0 is rows and axis=1 is columns

# Delete a multiple columns
filtered_unit_price_and_order_id = pizza_sales_df.drop(['unit_price','order_id'], axis=1) # axis =0 is rows and axis=1 is columns

# =============================================================================
#  Sorting a dataframe in pandas
# =============================================================================

# Sorting in ascending order
sorted_df = pizza_sales_df.sort_values('total_price')

# Sorting in descenring order
sorted_df = pizza_sales_df.sort_values('total_price', ascending=False)

# Sorting by multiple columns
sorted_df = pizza_sales_df.sort_values(['pizza_category_id','total_price'], ascending=[True, False])

# =============================================================================
# Group by dataframe in pandas aggregation
# =============================================================================
# Group by pizza size id and get the count of sales (row count)
grouped_df_pizza_size = pizza_sales_df.groupby(['pizza_size_id']).count()

# Group by pizza size id and get the sum
# Note: Python can not sum text or date
grouped_df_pizza_size_by_sum = pizza_sales_df.groupby(['pizza_size_id'])['total_price'].sum()

# Additional aggregation
# Group by pizza size id and sum total_price and quantity
# If you use more that one column use multiple square bracket
grouped_df_pizza_size_sales_quantity = pizza_sales_df.groupby(['pizza_size_id'])[['total_price','quantity']].sum()



# Looking at different aggregation functions
# count(): Counts the number of non-NA/null values in each group
# sum(): Sums the values in each group
# mean(): Calculates the mean of values in each group
# std(): Compute the standard deviation in each group
# var(): Compute the standard variance in each group
# min(): Find the minimum values in each group
# max(): Find the maximum values in each group
# prod(): Computer the product of values in each group
# first(), last(): Get the fisrt and last values in each group
# size(): Returns the size of each group (including NaN/NA values)
# nunique(): Counts the number of unique values in each group

grouped_df_agg = pizza_sales_df.groupby(['pizza_size_id'])[['total_price','quantity']].sum()


# =============================================================================
# Using Aggregation Function
# =============================================================================

# Using agg to perform different aggregations on different columns
aggregated_data = pizza_sales_df.groupby(['pizza_size_id']).agg({'quantity':'sum', 'total_price': 'mean'})

# Merging pizza sales df and pizza size df
merged_df = pd.merge(pizza_sales_df, pizza_sizes_df, on='pizza_size_id')

# Add category iformation
merged_df = pd.merge(merged_df, pizza_categories_df, on='pizza_category_id')

# =============================================================================
# Concantenate two DataFrame
# =============================================================================
# Concantenate two DataFrame - appending rows to a dataframe - vertically
another_pizza_sales_df = pd.read_excel('another_pizza_sales.xlsx')
concatenate_vertically = pd.concat([pizza_sales_df, another_pizza_sales_df])
concatenate_vertically = concatenate_vertically.reset_index()

# Concantenate two DataFrame - appending columns to a dataframe - horizontally
pizza_sales_voucher_df = pd.read_excel('pizza_sales_voucher.xlsx')
concatenate_horizontally = pd.concat([pizza_sales_df, pizza_sales_voucher_df], axis=1)

# Converting to lower case
lower_text = pizza_sales_df['pizza_ingredients'].str.lower()
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.lower()

# Converting to uppercase
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.upper()

# Converting to title case
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.title()


# =============================================================================
# Replacing Text Value
# =============================================================================
# Replacing Text Value
replaced_text = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', 'Mozzarella')
pizza_sales_df['pizza_ingredients'] = pizza_sales_df['pizza_ingredients'].str.replace('Feta Cheese', 'Mozzarella')

# =============================================================================
# Removing extra white spacing
# =============================================================================
pizza_sales_df['pizza_name'] = pizza_sales_df['pizza_name'].str.strip()


# =============================================================================
# Generating a Box Plot
# =============================================================================
#  Use the merged_df dataframe
sns.boxplot(x='category', y='total_price', data=merged_df)
plt.xlabel('Pizza Category')
plt.ylabel('Total Sales')
plt.title('Boxplot showing distribution of sales by category')
plt.show()



# Creating a plot
# Note: X-axis is month_year while Y-axis payment_value
# plt.plot(x, y)
"""
plt.plot(merged_df['category'], merged_df['total_price'], color='red', marker='o')
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xlabel('Pizza Category')
plt.ylabel('Total Sales')
plt.title('Boxplot showing distribution of sales by category')
plt.xticks(rotation = 90, fontsize=8)
plt.yticks(fontsize=8)

pivot_data = merged_df.pivot(index='pizza_name', columns='total_price', values='quantity')
pivot_data.plot(kind='bar', stacked='True')
plt.ticklabel_format(useOffset=False, style='plain', axis='y')
plt.xlabel('Pizza Category')
plt.ylabel('Total Sales')
plt.title('Boxplot showing distribution of sales by category')
"""

# plt.savefig('my_plot.png')


# =============================================================================
# Exporting Data
# =============================================================================
# Exporting Data
merged_df.to_excel('pizza_sales_merged_data.xlsx', index=False)
merged_df.to_json('pizza_sales_merged_data.json')



