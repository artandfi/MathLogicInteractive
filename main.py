import dearpygui.dearpygui as dpg
from constants import DATA_PATH, DEFAULT_FONT_PATH, MAIN_WND
from callbacks import module_btn_click
from dearpygui_ext.themes import create_theme_imgui_light


modules = ['Propositional Logic', 'Predicate Calculus', 'Sequent Calculus', 'Resolution Method']


def setup():
    dpg.create_viewport(title="MathLogic Interactive by (c) artandfi")
    dpg.setup_dearpygui()

    with dpg.font_registry():
        default_font = dpg.add_font(DEFAULT_FONT_PATH, 20)

    with dpg.window(tag=MAIN_WND):
        dpg.bind_font(default_font)
        dpg.add_text("Modules")
    
        for i, module in enumerate(modules):
            user_data = {
                "label": module,
                "path": f"{DATA_PATH}/module{i+1}"
            }
            dpg.add_button(label=module, callback=module_btn_click, user_data=user_data)
        
        dpg.add_text(f"Score: 67/100 (D)")
        dpg.add_progress_bar(overlay="Progress: 52%", default_value=0.52)

    dpg.set_primary_window(MAIN_WND, True)
    dpg.maximize_viewport()

    theme = create_theme_imgui_light()
    dpg.bind_theme(theme)
    dpg.show_viewport()


def main():
    dpg.create_context()
    setup()
    dpg.start_dearpygui()
    dpg.destroy_context()


if __name__ == "__main__":
    main()
