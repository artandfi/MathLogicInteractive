import dearpygui.dearpygui as dpg
from constants import MAIN_WND


def module_btn_click(sender, app_data, user_data):
    module = user_data["module"]

    with dpg.window(tag=module.name, label=module.name):
        module.render()
        dpg.add_button(label="Back", callback=back_btn_click, user_data=module.name)
    
    dpg.set_primary_window(module.name, True)
    dpg.hide_item(dpg.get_active_window())
    

def back_btn_click(sender, app_data, user_data):
    dpg.set_primary_window(MAIN_WND, True)
    dpg.delete_item(user_data)
    dpg.show_item(MAIN_WND)
