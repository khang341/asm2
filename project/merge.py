import argparse
import os
import pandas as pd

def merge_csv(input_files, output_file):
    dfs = []

    for file in input_files:
        df = pd.read_csv(file)
        dfs.append(df)

    merged_df = pd.concat(dfs, ignore_index=True)
    merged_df = merged_df.drop_duplicates(subset=["text"]).reset_index(drop=True)

    out_dir = os.path.dirname(output_file)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    merged_df.to_csv(output_file, index=False)
    print(f"Merged CSV saved as {output_file}")
    print(f"Total rows: {len(merged_df)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Merge multiple CSV files into one CSV file.")
    parser.add_argument("input_files", nargs="+", help="Input CSV files")
    parser.add_argument("--output", required=True, help="Output CSV file")
    args = parser.parse_args()

    merge_csv(args.input_files, args.output)