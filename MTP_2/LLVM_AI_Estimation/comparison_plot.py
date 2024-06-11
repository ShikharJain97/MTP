import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Read a CSV file
def read_csv_file(file_path):
    data = pd.read_csv(file_path)
    return data

# Step 2: Ask for pairs of columns to be used as the x-axis and y-axis
def get_column_pairs(data):
    print("Available columns:", list(data.columns))
    x_col = input("Enter the column name for the x-axis: ")
    y_col = input("Enter the column name for the y-axis: ")
    return x_col, y_col

# Step 3: Define a function to create a plot of a specified type
def create_plot(data, x_col, y_col, plot_type):
    plt.figure()
    if plot_type == 'scatter':
        plt.scatter(data[x_col], data[y_col])
    elif plot_type == 'bar':
        plt.bar(data[x_col], data[y_col])
    elif plot_type == 'line':
        plt.plot(data[x_col], data[y_col])
    else:
        print("Unsupported plot type!")
        return
    plt.xlabel(x_col)
    plt.ylabel(y_col)
    plt.title(f'{plot_type.capitalize()} plot of {y_col} vs {x_col}')
    plt.show()

# Step 4: Define a function to create a plot with multiple y-axes and one x-axis
def create_multiple_y_plots(data, x_col, y_cols, plot_types):
    if len(y_cols) != len(plot_types):
        print("Number of y columns must match the number of plot types.")
        return

    plt.figure()
    for y_col, plot_type in zip(y_cols, plot_types):
        if plot_type == 'scatter':
            plt.scatter(data[x_col], data[y_col], label=f'{y_col} (scatter)')
        elif plot_type == 'bar':
            plt.bar(data[x_col], data[y_col], label=f'{y_col} (bar)')
        elif plot_type == 'line':
            plt.plot(data[x_col], data[y_col], label=f'{y_col} (line)')
        else:
            print(f"Unsupported plot type for {y_col}!")
            return
    plt.xlabel(x_col)
    plt.ylabel("Values")
    plt.title(f'Multiple plots with x-axis {x_col}')
    plt.legend()
    plt.show()

# Example usage:
# 1. Read CSV file
file_path = '/home/shikhar_jain/MTP-2/LLVM_AI_Estimation/Comparison.csv'
data = read_csv_file(file_path)

# 2. Get column pairs for individual plots
x_col, y_col = get_column_pairs(data)
plot_type = input("Enter the plot type (scatter, bar, line): ")
create_plot(data, x_col, y_col, plot_type)

# 3. Get multiple y columns for combined plot
y_cols = input("Enter the y columns separated by commas: ").split(',')
plot_types = input("Enter the plot types separated by commas (same order as y columns): ").split(',')
create_multiple_y_plots(data, x_col, y_cols, plot_types)

