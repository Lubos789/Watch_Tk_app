import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk
from ttkbootstrap.scrolled import ScrolledText
# from tkinter.scrolledtext import ScrolledText
from datetime import date
from pathlib import Path

class ObjWindow:

    def add_widgets(self, root):
        self.aad_frame(root)
        self.add_buttons()
        self.add_labels()
        self.add_entry()
        self.add_text_box()
        self.add_progress_meter()

    def aad_frame(self, root):
        # self.frame1 = ttk.Frame(root)
        # self.frame1.pack(side=TOP)

        self.frame = ttk.Frame(root)
        self.frame.pack(side=LEFT)

        img_path = Path(__file__).parent / 'image/pngegg (1).png'
        self.demo_media = ttk.PhotoImage(file=img_path)
        self.media = ttk.Label(self.frame, image=self.demo_media)
        self.media.pack(side=TOP)
        # self.media.grid(row=0, column=0, columnspan=2, pady=(0, 30))

        self.frame0 = ttk.Frame(self.frame)
        self.frame0.pack(side=LEFT)

        self.my_notebook = ttk.Notebook(self.frame0, bootstyle="dark")
        self.my_notebook.pack(padx=20, pady=(20, 0))

        self.tab1 = ttk.Frame(self.my_notebook)
        self.tab2 = ttk.Frame(self.my_notebook)

        self.my_notebook.add(self.tab1, text="Menu")
        self.my_notebook.add(self.tab2, text="Setup VS")

        self.frame2 = ttk.Frame(root)
        self.frame2.pack(side=RIGHT)


    def add_buttons(self):
        # Style
        my_style = ttk.Style()
        my_style.configure('success.Outline.TButton', font=("Helvetica", 10, "bold"))
        my_style.configure('danger.Outline.TButton', font=("Helvetica", 20, "bold"))

        self.button1 = ttk.Button(self.tab1, width=21, text="Vysoké školy", bootstyle="success-outline", style="success.Outline.TButton")
        self.button1.grid(row=1, column=0, padx=(10, 5), pady=(30, 0), sticky="nw")

        self.button2 = ttk.Button(self.tab1, width=21, text="Query by date (db)", bootstyle="success-outline")
        self.button2.grid(row=1, column=1, padx=(5, 10), pady=(30, 0), sticky="nw")

        self.button_vvi = ttk.Button(self.tab1, width=21, text="V.V.I", bootstyle="success-outline")
        self.button_vvi.grid(row=3, column=0, padx=(10, 5), pady=1, sticky="nw")

        self.button_vvi_date = ttk.Button(self.tab1, width=21, text="Query by date (web)", bootstyle="success-outline")
        self.button_vvi_date.grid(row=3, column=1, padx=(5, 10), pady=1, sticky="nw")

        self.button_statni_podniky = ttk.Button(self.tab1, width=21, text="Státní podniky", bootstyle="success-outline")
        self.button_statni_podniky.grid(row=5, column=0, padx=(10, 5), pady=1, sticky="nw")

        self.button_statni_podniky_date = ttk.Button(self.tab1, width=21, text="Query by date (web)", bootstyle="success-outline")
        self.button_statni_podniky_date.grid(row=5, column=1, padx=(5, 10), pady=1, sticky="nw")

        self.button_podiky_v_likvidaci = ttk.Button(self.tab1, width=21, text="Podniky v likvidaci", bootstyle="success-outline")
        self.button_podiky_v_likvidaci.grid(row=7, column=0, padx=(10, 5), pady=1, sticky="nw")

        self.button_podiky_v_likvidaci_date = ttk.Button(self.tab1, width=21, text="Query by date (web)", bootstyle="success-outline")
        self.button_podiky_v_likvidaci_date.grid(row=7, column=1, padx=(5, 10), pady=1, sticky="nw")
    #   ------------ tab 2 ---------------------------------------------------------------------------------------------
        self.button_show = ttk.Button(self.tab2, width=21, text="Show", bootstyle="success-outline")
        self.button_show.grid(row=2, column=1, padx=(1, 5), pady=(3, 50), sticky="ne")

        self.button_up = ttk.Button(self.tab2, width=21, text="UP", bootstyle="success-outline")
        self.button_up.grid(row=3, column=1, padx=(1, 5), pady=3, sticky="ne")

        self.button_down = ttk.Button(self.tab2, width=21, text="DOWN", bootstyle="success-outline")
        self.button_down.grid(row=4, column=1, padx=(1, 5), sticky="ne")

        # self.button_set = ttk.Button(self.tab2, width=21, text="SET", bootstyle="success-outline")
        # self.button_set.grid(row=4, column=1, padx=(10, 5))
    def add_labels(self):

        # self.label2 = ttk.Label(self.frame1, text="Hello World Test 1")
        # self.label2.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        # self.label2 = ttk.Label(self.frame2, text="Hello World Test 2")
        # self.label2.grid(row=0, column=0, padx=5, pady=5, sticky="n")

        self.label_last_run_vs = ttk.Label(self.tab1, text="Last run VS", bootstyle="light")
        self.label_last_run_vs.grid(row=2, column=0, padx=5, pady=(5, 30), sticky="nw")

        self.label_last_run_vvi = ttk.Label(self.tab1, text="Last run VVI", bootstyle="light")
        self.label_last_run_vvi.grid(row=4, column=0, padx=5, pady=(5, 30), sticky="nw")

        self.label_last_run_podniky = ttk.Label(self.tab1, text="Last run Statní podniky", bootstyle="light")
        self.label_last_run_podniky.grid(row=6, column=0, padx=5, pady=(5, 30), sticky="nw")

        self.label_last_run_likvidace = ttk.Label(self.tab1, text="Last run Statní podniky", bootstyle="light")
        self.label_last_run_likvidace.grid(row=8, column=0, padx=5, pady=(5, 30), sticky="nw")
    #   ------------ tab 2 ---------------------------------------------------------------------------------------------
        self.label_zadej_subjekt = ttk.Label(self.tab2, text="Enter the subject name:")
        self.label_zadej_subjekt.grid(row=0, column=0, columnspan=2, sticky="n", pady=(30, 0))

        self.label_set_up = ttk.Label(self.tab2, text="Set UP and Save:")
        self.label_set_up.grid(row=3, column=0, sticky="e")

        self.label_set_down = ttk.Label(self.tab2, text="Set DOWN and Save:")
        self.label_set_down.grid(row=4, column=0, sticky="e")

    def add_entry(self):
        self.entry_sub_name = ttk.Entry(self.tab2, width=57, bootstyle="success")
        self.entry_sub_name.grid(row=1, column=0, columnspan=2, pady=2, padx=(7, 5))

    def add_text_box(self):
        # style = ttk.Style()
        # self.scrolledtext = ScrolledText(
        #     master=self.frame2,
        #     # highlightcolor=style.colors.primary,
        #     # highlightbackground=style.colors.border,
        #     # highlightthickness=1
        # )

        self.scrolledtext = ScrolledText(self.frame2, bootstyle="dark-round", width=130, height=60, wrap=WORD, font=("Segoe", 10))
        self.scrolledtext.grid(row=0, column=0, sticky="n")

        default_txt = "Click the button to start comparing."
        self.scrolledtext.insert(END, default_txt)

    def add_progress_meter(self):
        self.progrsess_meter = ttk.Meter(self.tab1, bootstyle="secondary",
                            # subtext="Working!!!",
                            # interactive=True,
                            textright="",
                            # textleft="Working!!!",
                            metertype="semi",
                            stripethickness=2,
                            metersize=200,
                            padding=20,
                            amountused=0,
                            amounttotal=100,
                            # subtextstyle="success"
                            # textfont="-size 30 -weight bold",
                            # subtextfont="-size 20 -weight bold",
                            )
        self.progrsess_meter.grid(row=9, column=0, columnspan=2)
