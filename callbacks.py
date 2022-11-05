import dearpygui.dearpygui as dpg
from constants import MAIN_WND


def module_btn_click(sender, app_data, user_data):
    with dpg.window(tag=user_data, label=user_data):
        # load module data from its file here
        dpg.add_text("Module contents...", wrap=dpg.get_viewport_client_width()*0.95)
        dpg.add_text("Training test contents...")
        dpg.add_text("Test contents...")
        dpg.add_button(label="Back", callback=back_btn_click, user_data=user_data)
    
    dpg.set_primary_window(user_data, True)
    dpg.hide_item(dpg.get_active_window())
    

def back_btn_click(sender, app_data, user_data):
    dpg.set_primary_window(MAIN_WND, True)
    dpg.delete_item(user_data)
    dpg.show_item(MAIN_WND)
