import json
import dearpygui.dearpygui as dpg
from constants import MAIN_WND, PROGRESS_FILE, SCORE_TEXT, PROGRESS_BAR


def module_btn_click(sender, app_data, user_data):
    modules = user_data["modules"]
    module = modules[user_data["module_index"]]

    with dpg.window(tag=module.name, label=module.name):
        module.render()
        dpg.add_text()
        dpg.add_button(label="Submit", callback=submit_btn_click, user_data=user_data, show=not module.completed)
        dpg.add_button(label="Back", callback=back_btn_click, user_data=[module.name])
    
    dpg.set_primary_window(module.name, True)
    dpg.hide_item(dpg.get_active_window())


def submit_btn_click(sender, app_data, user_data):
    modules = user_data["modules"]
    module = modules[user_data["module_index"]]
    module.completed = True
    module.save_progress()

    dpg.set_value(SCORE_TEXT, f"Score: {sum(m.score for m in modules)}/{sum(m.max_score for m in modules)}")
    dpg.set_value(PROGRESS_BAR, sum([m.completed for m in modules])/len(modules))
    
    with dpg.window(label="Result", modal=True, show=True, tag="modal_id", no_title_bar=True):
        dpg.add_text(f"Your score: {sum(task.score for task in module.exam.tasks)}/{module.max_score}")
        dpg.add_separator()
        dpg.add_button(label="OK", width=75, callback=back_btn_click, user_data=["modal_id", module.name])


def back_btn_click(sender, app_data, user_data):
    dpg.set_primary_window(MAIN_WND, True)
    for wnd in user_data:
        dpg.delete_item(wnd)
    dpg.show_item(MAIN_WND)


def reset_progress_btn_click(sender, app_data, user_data):
    modules = user_data
    
    dpg.set_value(SCORE_TEXT, f"Score: 0/{sum(m.max_score for m in modules)}")
    dpg.set_value(PROGRESS_BAR, 0)

    with open(PROGRESS_FILE, "r") as f:
        data = json.load(f)
    
    for module in modules:
        scores_len = len(data[module.name]["scores"])
        data[module.name]["scores"] = [0 for _ in range(scores_len)]
        data[module.name]["completed"] = False
        module.refresh()
        
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=4)
