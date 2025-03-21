import os

dataset_dir = "C:/Users/ZODNGUY1/datasets/dtu-surfels"
dataset_gt_dir = "C:/Users/ZODNGUY1/datasets/dtu/Official_DTU_Dataset"
scenes = [24, 37, 40, 55, 63, 65, 69, 83, 97, 105, 106, 110, 114, 118, 122]

poisson_depth = 10

out_dir = "C:/Users/ZODNGUY1/OneDrive - Carl Zeiss AG/gaussian/repos/gaussian-surfels/output/dtu"

for scene in scenes:
    print(f"======= Processing scene scan{scene} =======")

    cmd = f"python train.py -s {dataset_dir}/scan{scene} -m \"{out_dir}/scan{scene}\" -r 2 --checkpoint_iterations 7000 30000"
    print("[>] " + cmd)
    os.system(cmd)
    
    cmd = f"python render.py -m \"{out_dir}/scan{scene}\" -s {dataset_dir}/scan{scene} -r 2 --skip_test --img --depth {poisson_depth}"
    print("[>] " + cmd)
    os.system(cmd)

    cmd = f"python eval.py --dataset dtu --source_path {dataset_dir}/scan{scene} --mesh_path \"{out_dir}/scan{scene}/poisson_mesh_{poisson_depth}_plain.ply\" --dtu_gt_path {dataset_gt_dir} --dtu_scanId {scene}"
    print("[>] " + cmd)
    os.system(cmd)

    cmd = f"python eval.py --dataset dtu --source_path {dataset_dir}/scan{scene} --mesh_path \"{out_dir}/scan{scene}/poisson_mesh_{poisson_depth}_pruned.ply\" --dtu_gt_path {dataset_gt_dir} --dtu_scanId {scene}"
    print("[>] " + cmd)
    os.system(cmd)

    print(f"======= Done with scene scan{scene} =======\n")