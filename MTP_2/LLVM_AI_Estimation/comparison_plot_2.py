import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Step 1: Read a CSV file
def read_csv_file(file_path):
    data = pd.read_csv(file_path)
    return data

# Step 3: Define a function to create the desired plots
def create_combined_plot(data, x_col, y_cols, annotation_col):
    # Check if columns exist in the DataFrame
    for col in [x_col] + y_cols + [annotation_col]:
        if col not in data.columns:
            print(f"Column '{col}' does not exist in the data.")
            return

    # Extract necessary data
    x = data[x_col]
    y1 = data[y_cols[0]]
    y2 = data[y_cols[1]]
    annotations = data[annotation_col]

    # Define the positions for the bars
    bar_width = 0.35
    r1 = np.arange(len(x))
    r2 = [r + bar_width for r in r1]

    # Create the plot
    fig, ax1 = plt.subplots(figsize=(25,13))

    # Plot grouped bars
    bars1 = ax1.bar(r1, y1, color='b', width=bar_width, edgecolor='grey', label=y_cols[0])
    bars2 = ax1.bar(r2, y2, color='r', width=bar_width, edgecolor='grey', label=y_cols[1])

    # Log scaling on y-axis
    ax1.set_yscale('log')
    ax1.set_xlabel(x_col, fontsize='x-large', fontweight='bold')
    ax1.set_ylabel('FLOPS \n(Log Scale)', fontsize='x-large', fontweight='bold',rotation=0,labelpad=20)
    ax1.tick_params(axis='y', labelsize='xx-large')
    #ax1.set_yticklabels(ax1.get_ytickslables(),fontweight='bold')
    ax1.set_title(f'PAPI vs LLVM Pass Estimation ', fontsize='x-large', fontweight='bold')
    ax1.set_xticks([r + bar_width/2 for r in range(len(x))])
    ax1.set_xticklabels(x, rotation=45, fontsize=13, fontweight='bold')
    #ax1.legend(fontsize='large')

    # Annotate each x label with the "Ratio" value
    for i, txt in enumerate(annotations):
        if not (1.0 <= txt <= 1.5):
            # Annotation text in a box
            ax1.annotate(
                f'{txt}',
                (r1[i] + bar_width, max(y1[i], y2[i]) * 1.05),
                textcoords="offset points",
                xytext=(0,5),
                ha='center',
                fontsize='large',
                fontweight='bold',
                color='green',
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.5')
            )

    # Create a custom legend to include the "LLVM vs PAPI Ratio"
    handles, labels = ax1.get_legend_handles_labels()
    handles.append(plt.Line2D([0], [0], color='green', lw=4))
    labels.append('LLVM vs PAPI Ratio(>1.5)')
    ax1.legend(handles, labels, fontsize='large')

    
    plt.savefig("LLVMPassvsPAPI_POLYBENCH.pdf",dpi=300)

# Example usage:
# 1. Read CSV file
file_path = '/home/shikhar_jain/MTP-2/LLVM_AI_Estimation/Comparison.csv'
data = read_csv_file(file_path)

# 2. Create the combined plot
x_col = 'Kernels'
y_cols = ['PAPI', 'LLVM PASS']
annotation_col = 'Ratio'
create_combined_plot(data, x_col, y_cols, annotation_col)

