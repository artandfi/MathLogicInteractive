import dearpygui.dearpygui as dpg
from constants import DEFAULT_FONT_PATH, MAIN_WND, SCORE_TEXT, PROGRESS_BAR
from callbacks import module_btn_click, reset_progress_btn_click
from dearpygui_ext.themes import create_theme_imgui_light
from models.propositional_logic.module import PropositionalLogicModule
from models.propositional_calculus.module import PropositionalCalculusModule
from models.sequent_calculus.module import SequentCalculusModule


modules = [
    PropositionalLogicModule(),
    PropositionalCalculusModule(),
    SequentCalculusModule(),
    #'Resolution Method'
]


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
                "module_index": i,
                "modules": modules
            }
            dpg.add_button(label=module.name, callback=module_btn_click, user_data=user_data)
        
        dpg.add_text(f"Score: {sum(m.score for m in modules)}/{sum(m.max_score for m in modules)}", tag=SCORE_TEXT)
        dpg.add_progress_bar(overlay="Course progress", default_value=sum([m.completed for m in modules])/len(modules), tag=PROGRESS_BAR)
        dpg.add_text()
        dpg.add_button(label="Reset progress", callback=reset_progress_btn_click, user_data=modules)

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
