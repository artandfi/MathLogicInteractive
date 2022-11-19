import dearpygui.dearpygui as dpg
from constants import MAIN_WND


def module_btn_click(sender, app_data, user_data):
    module = user_data["module"]

    with dpg.window(tag=module.name, label=module.name):
        module.render()
        dpg.add_text()
        dpg.add_button(label="Submit", callback=submit_btn_click, user_data=module)
        dpg.add_button(label="Back", callback=back_btn_click, user_data=[module.name])
    
    dpg.set_primary_window(module.name, True)
    dpg.hide_item(dpg.get_active_window())


def submit_btn_click(sender, app_data, user_data):
    module = user_data
    module.save_progress()
    
    with dpg.window(label="Result", modal=True, show=True, tag="modal_id", no_title_bar=True):
        dpg.add_text(f"Your score: {sum(task.score for task in module.exam.tasks)}/{module.max_score}")
        dpg.add_separator()
        dpg.add_button(label="OK", width=75, callback=back_btn_click, user_data=["modal_id", module.name])


def back_btn_click(sender, app_data, user_data):
    dpg.set_primary_window(MAIN_WND, True)
    for wnd in user_data:
        dpg.delete_item(wnd)
    dpg.show_item(MAIN_WND)
