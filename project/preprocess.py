import argparse
import os
import pandas as pd

def preprocess(input_path: str, output_path: str, label_col: str, text_col: str):
    df = pd.read_csv(input_path, encoding="latin-1")

    # Validate columns early (so you get a clear error)
    missing = [c for c in [label_col, text_col] if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns {missing}. Available columns: {list(df.columns)}")

    df = df[[label_col, text_col]].copy()
    df.columns = ["label", "text"]

    # Clean
    df["label"] = df["label"].astype(str).str.strip().str.lower()
    df["text"] = df["text"].astype(str)
    df["text"] = df["text"].str.replace("\r", " ", regex=False).str.replace("\n", " ", regex=False).str.strip()

    # Drop empty text
    df = df[df["text"].str.len() > 0]

    # Keep only spam/ham
    df = df[df["label"].isin(["spam", "ham"])]

    
    out_dir = os.path.dirname(output_path)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    df.to_csv(output_path, index=False)
    print(f"Saved: {output_path} (rows={len(df)})")

    df["text"] = df["text"].str.encode("latin1", errors="ignore").str.decode("utf-8", errors="ignore")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)
    parser.add_argument("--label-col", required=True)
    parser.add_argument("--text-col", required=True)
    args = parser.parse_args()

    preprocess(args.input, args.output, args.label_col, args.text_col)