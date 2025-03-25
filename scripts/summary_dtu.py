import argparse
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Process chamfer.json files in subdirectories.")
    parser.add_argument("--parent_dir", "-d", type=str, required=True, help="Parent directory containing subdirectories.")
    parser.add_argument("--depth", type=int, default=10, help="Depth value to extract from chamfer.json.")
    args = parser.parse_args()

    parent_dir = Path(args.parent_dir)

    if not parent_dir.is_dir():
        print(f"Error: {parent_dir} is not a valid directory.")
        return

    plain_values = []
    pruned_values = []

    for sub_dir in parent_dir.iterdir():
        if not sub_dir.is_dir():
            continue

        chamfer_file = sub_dir / "chamfer.json"
        if not chamfer_file.exists():
            print(f"Warning: chamfer.json not found in {sub_dir}")
        
        with chamfer_file.open("r") as f:
            data = json.load(f)
            plain_value = data[f"plain_{args.depth}"]
            pruned_value = data[f"pruned_{args.depth}"]
            print(f"{sub_dir}: plain_{args.depth}={plain_value:.2f}, pruned_{args.depth}={pruned_value:.2f}")
            plain_values.append(plain_value)
            pruned_values.append(pruned_value)

    if plain_values and pruned_values:
        avg_plain = round(sum(plain_values) / len(plain_values), 2)
        avg_pruned = round(sum(pruned_values) / len(pruned_values), 2)
        print(f"Average: plain_{args.depth}={avg_plain}, pruned_{args.depth}={avg_pruned}")
    else:
        print("No valid chamfer.json data found.")

if __name__ == "__main__":
    main()