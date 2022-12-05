import json


def reset_progress(modules, progress_file_path):
    """
        Resets the progress for the entire course.
        
        Args:
            modules (Iterable[Module]): List of course modules.
            progress_file_path (PathLike): Path to the progress file.
        Returns:
            None
    """
    with open(progress_file_path, "r") as f:
        data = json.load(f)
    
    for module in modules:
        scores_len = len(data[module.name]["scores"])
        data[module.name]["scores"] = [0 for _ in range(scores_len)]
        data[module.name]["completed"] = False
        module.refresh()
        
    with open(progress_file_path, "w") as f:
        json.dump(data, f, indent=4)


def score_letter(score):
    """
        A grade in the ABCDF system based on 0-100 score.

        Args:
            score (float): The score from 0 to 100.
        Returns:
            Literal['F', 'D', 'C', 'B', 'A']
    """
    if 0 <= score <= 59:
        return 'F'
    if 60 <= score <= 69:
        return 'D'
    if 70 <= score <= 79:
        return 'C'
    if 80 <= score <= 89:
        return 'B'
    if 90 <= score <= 100:
        return 'A'
    
    raise ValueError