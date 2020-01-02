from infi.systray import SysTrayIcon
import os

this_dir = os.getcwd()
icons = f"{this_dir}/icons"

def conf_watch(systray):
    systray.update(hover_text="Configuration in Progress", icon=f"{icons}/gear_32x32.ico")
    os.system(f'python {this_dir}/watch_config_gui.py')
    systray.update(hover_text="Waiting to begin Watch", icon=f"{icons}/question_32x32.ico")

def start_watch(systray):
    systray.update(hover_text="Watch has begun", icon=f"{icons}/check_32x32.ico")

def end_watch(systray):
    systray.update(hover_text="Watch has ended", icon=f"{icons}/red_cross_32x32.ico")

menu_options = (("Configure Watch", f"{icons}/gear_32x32.ico", conf_watch),
                ("Begin Watch", f"{icons}/check_32x32.ico", start_watch),
                ("End Watch", f"{icons}/red_cross_32x32.ico", end_watch))
systray = SysTrayIcon(f"{icons}/question_32x32.ico", "Waiting to begin Watch", menu_options)
systray.start()
