import json


def reset_progress(modules, progress_file_path):
    with open(progress_file_path, "r") as f:
        data = json.load(f)
    
    print(data)
    for module in modules:
        scores_len = len(data[module.name]["scores"])
        data[module.name]["scores"] = [0 for _ in range(scores_len)]
        data[module.name]["completed"] = False
        module.refresh()
        
    with open(progress_file_path, "w") as f:
        json.dump(data, f, indent=4)
