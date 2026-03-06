import argparse
import pandas as pd
import matplotlib.pyplot as plt

def visualize_distribution(csv_file, title):

    # Load dataset
    df = pd.read_csv(csv_file)

    # Count labels
    class_counts = df["label"].value_counts()

    # Plot
    plt.figure(figsize=(8,5))
    class_counts.plot(kind="bar")

    plt.title(title)
    plt.xlabel("Class")
    plt.ylabel("Count")

    plt.xticks(rotation=0)
    plt.tight_layout()

    # Show graph
    plt.show()

    # Also save the figure (useful for reports)
    plt.savefig("output/class_distribution.png")

    print("Graph saved as output/class_distribution.png")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Visualize class distribution")

    parser.add_argument("--input", required=True, help="Path to CSV file")
    parser.add_argument("--title", default="Dataset Class Distribution")

    args = parser.parse_args()

    visualize_distribution(args.input, args.title)
