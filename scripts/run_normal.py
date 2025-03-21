import os
import argparse

if __name__ == "__main__":
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run normal estimation on all subfolders of a dataset root directory.")
    parser.add_argument('--dataset_root', '-r', type=str, help="Path to the dataset root directory.")
    args = parser.parse_args()

    # Change directory to the script's location
    script_dir  = os.path.join(os.path.dirname(os.path.abspath(__file__)), '../submodules/omnidata')
    os.chdir(script_dir)

    # Loop through all subfolders in the dataset root
    for subfolder in os.listdir(args.dataset_root):
        print(f"Processing scene: {subfolder}")
        subfolder_path = os.path.join(args.dataset_root, subfolder)
        if os.path.isdir(subfolder_path):
            # Construct and execute the command
            image_path = os.path.join(subfolder_path, 'image')
            command = f'python estimate_normal.py --img_path "{image_path}"'
            os.system(command)