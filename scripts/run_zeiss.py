import os

dataset_dir = "C:/Users/ZODNGUY1/datasets/zeiss"
scenes = ["brain-transparent"]

poisson_depth = 10

out_dir = "C:/Users/ZODNGUY1/OneDrive - Carl Zeiss AG/gaussian/repos/gaussian-surfels/output/zeiss"

for scene in scenes:
    print(f"======= Processing scene {scene} =======")

    cmd = f"python train.py -s {dataset_dir}/{scene} -m \"{out_dir}/{scene}\" -r 2 -i images --checkpoint_iterations 7000 30000"
    print("[>] " + cmd)
    os.system(cmd)
    
    # Out of memory due to high number of training views: IDR training path?
    cmd = f"python render.py -m \"{out_dir}/{scene}\" -s {dataset_dir}/{scene} -r 2 --skip_test --img --depth {poisson_depth}"
    print("[>] " + cmd)
    os.system(cmd)

    cmd = f"python metrics.py -m \"{out_dir}/{scene}\""
    print("[>] " + cmd)
    os.system(cmd)

    print(f"======= Done with scene {scene} =======\n")