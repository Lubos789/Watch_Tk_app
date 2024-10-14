import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
import os
from obj_window import ObjWindow
from vs_fce import VsFce
from Stat_pod_fce import StatPodFce
from vvi import VviFce
from setup import Setup


class MainClass:

    def __init__(self, root):
        self.initialize()

    def initialize(self):
        self.root = root
        width = 1350
        height = 1000
        self.root.geometry(f"{width}x{height}")
        self.root.title("Control_App")
        # root.grid_columnconfigure(2, weight=1)
        # root.grid_columnconfigure(1, weight=1)
        # root.grid_rowconfigure(1, weight=1)

        # for i in range(3):
        #     self.columnconfigure(i, weight=1)
        # self.rowconfigure(0, weight=1)

        self.obj_window = ObjWindow()
        self.obj_window.add_widgets(self.root)

        self.vs_fce = VsFce(self.obj_window.scrolledtext, self.obj_window.label_last_run_vs)
        self.stat_pod_fce = StatPodFce(self.obj_window.scrolledtext, 1, self.obj_window.label_last_run_podniky, "or_fce")
        self.stat_pod_likvidace = StatPodFce(self.obj_window.scrolledtext, 0, self.obj_window.label_last_run_likvidace, "podniky_v_likvidaci_fce")
        self.vvi = VviFce(self.obj_window.scrolledtext, self.obj_window.label_last_run_vvi, "vvi_fce")
        self.setup = Setup(self.obj_window.scrolledtext)

        self.binds_event()

    def binds_event(self):
        # self.obj_window.button1.config(command=lambda: self.obj_window.label1.config(text=self.vs_fce.play()))
        self.obj_window.button1.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.vs_fce.run_main_fce(self.obj_window.progrsess_meter, self.obj_window.frame0)))
        self.obj_window.button2.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.vs_fce.date_fce()))
        self.obj_window.button_statni_podniky.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.stat_pod_fce.run_main_fce(self.obj_window.progrsess_meter, self.obj_window.frame0)))
        self.obj_window.button_statni_podniky_date.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.stat_pod_fce.date_fce(self.obj_window.progrsess_meter, self.obj_window.frame0)))
        self.obj_window.button_show.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.setup.show(self.obj_window.entry_sub_name)))
        self.obj_window.button_up.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.setup.up(self.obj_window.entry_sub_name)))
        self.obj_window.button_down.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.setup.down(self.obj_window.entry_sub_name)))
        self.obj_window.button_podiky_v_likvidaci.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.stat_pod_likvidace.run_main_fce(self.obj_window.progrsess_meter, self.obj_window.frame0)))
        self.obj_window.button_podiky_v_likvidaci_date.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.stat_pod_likvidace.date_fce(self.obj_window.progrsess_meter, self.obj_window.frame0)))
        self.obj_window.button_vvi.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.vvi.vvi_main(self.obj_window.progrsess_meter, self.obj_window.frame0)))
        self.obj_window.button_vvi_date.config(command=lambda: self.obj_window.scrolledtext.insert(END, self.vvi.date_fce(self.obj_window.progrsess_meter, self.obj_window.frame0)))

if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = MainClass(root)
    root.mainloop()
