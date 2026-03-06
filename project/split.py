import argparse
import os
import pandas as pd
from sklearn.model_selection import train_test_split

def split_dataset(input_csv, out_dir, train_ratio=0.8, seed=42):
    df = pd.read_csv(input_csv)

    # Shuffle + split
    train_df, temp_df = train_test_split(
        df,
        test_size=(1 - train_ratio),
        random_state=seed,
        stratify=df["label"]
    )

    val_df, test_df = train_test_split(
        temp_df,
        test_size=0.5,
        random_state=seed,
        stratify=temp_df["label"]
    )

    # Create output folder
    os.makedirs(out_dir, exist_ok=True)

    train_path = os.path.join(out_dir, "train.csv")
    val_path = os.path.join(out_dir, "val.csv")
    test_path = os.path.join(out_dir, "test.csv")

    train_df.to_csv(train_path, index=False)
    val_df.to_csv(val_path, index=False)
    test_df.to_csv(test_path, index=False)

    print("Split completed successfully.")
    print(f"Train: {train_path} ({len(train_df)} rows)")
    print(f"Validation: {val_path} ({len(val_df)} rows)")
    print(f"Test: {test_path} ({len(test_df)} rows)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split dataset into train/val/test")
    parser.add_argument("--input", required=True, help="Path to merged CSV")
    parser.add_argument("--outdir", required=True, help="Output directory")
    parser.add_argument("--train-ratio", type=float, default=0.8, help="Training ratio")
    parser.add_argument("--seed", type=int, default=42, help="Random seed")

    args = parser.parse_args()

    split_dataset(args.input, args.outdir, args.train_ratio, args.seed)