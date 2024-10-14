from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Querybox
from db_sqllite import Database
from obj_window import ObjWindow
import requests
from bs4 import BeautifulSoup
import datetime
import time
import pandas as pd
import lxml


class VviFce:
    def __init__(self, scrolledtext, last_run_label, to_sql_last_run):
        self.obj_window = ObjWindow()
        self.database = Database()
        self.records = self.database.query_database_vvi()
        self.output = []
        self.output_str = "\nZveřejněn nový dokument u těchto suběktů:\n\n"
        self.scrolledtext = scrolledtext
        self.obj_window.label_last_run_vvi = last_run_label
        self.to_sql_last_run = to_sql_last_run
        self.last_run_fce()

    def last_run_fce(self):
        self.obj_window.label_last_run_vvi.config(text=f"LAST RUN: {self.database.last_run_fce_db(self.to_sql_last_run)}")

    def date_time_now(self):
        datum_src = datetime.datetime.now()
        return datum_src.strftime("%Y-%m-%d %H:%M:%S")

    def vvi_main(self, progress, frame0):
        step = 1
        progress.configure(amountused=0, bootstyle="danger", subtextstyle="danger", subtext="Working", textright="%")
        frame0.update()
        self.scrolledtext.delete('1.0', END)
        for line in self.records:
            if progress['amountused'] > 50:
                step = 2
            progress.step(step)
            frame0.update()

            ico = line[0]
            name = line[1]
            last_record = line[2]

            or_tables_pages = pd.read_html(f"https://rvvi.msmt.cz/detail.php?ic={ico}", encoding='windows-1250')
            df = or_tables_pages[1]
            df[0] = pd.to_datetime(df[0], dayfirst=True)
            df = df.sort_values(by=0, ascending=False)
            web_record = df[:3].to_string()
            print(web_record)

            if last_record == web_record:
                pass
            else:
                df.columns = ['date', 'name', 'nan']
                df = df[['date', 'name']][:3]
                table_str = df.to_string()
                self.output_str += f"{name}:\n\n{table_str}\n\nOdkaz:\nhttps://rvvi.msmt.cz/detail.php?ic={ico}\n\n"

                self.database.update_record_vvi(web_record, ico, self.date_time_now())

        if self.output_str == "\nZveřejněn nový dokument u těchto suběktů:\n\n":
            self.output_str = "\nNové dokumenty nenalezeny!"

        progress.configure(bootstyle="dark", subtext="DONE", subtextstyle="success", textright="", amountused=0)
        frame0.update()
        time.sleep(2)
        progress.configure(bootstyle="dark", subtextstyle="dark", subtext="", textright="")
        frame0.update()

        self.database.last_run_update_db(self.date_time_now(), self.to_sql_last_run)
        self.last_run_fce()

        print(self.output_str)
        return self.output_str


    def date_fce(self, progress, frame0):
        searching_outputs = ""
        cal = Querybox()
        date_input = str(cal.get_date())
        print(date_input)
        progress.configure(amountused=0, bootstyle="danger", subtextstyle="danger", subtext="Working", textright="%")
        self.scrolledtext.delete('1.0', END)


        for line in self.records:
            step = 1
            if progress['amountused'] > 50:
                step = 2
            progress.step(step)
            frame0.update()

            ico = line[0]
            name = line[1]
            last_record = line[2]

            or_tables_pages = pd.read_html(f"https://rvvi.msmt.cz/detail.php?ic={ico}", encoding='windows-1250')
            df = or_tables_pages[1]
            df[0] = pd.to_datetime(df[0], dayfirst=True)
            df = df[df[0] > date_input]
            df = df.sort_values(by=0, ascending=False)
            if not df.empty:
                df.columns = ['date', 'name', 'nan']
                df = df[['date', 'name']]
                table_str = df.to_string()
                searching_message = f"{name}:\n\n{table_str}\n\nOdkaz:\nhttps://rvvi.msmt.cz/detail.php?ic={ico}\n\n\n\n"
                searching_outputs += searching_message

        progress.configure(bootstyle="dark", subtext="DONE", subtextstyle="success", textright="", amountused=0)
        frame0.update()
        time.sleep(2)
        progress.configure(bootstyle="dark", subtextstyle="dark", subtext="", textright="")
        frame0.update()
        if searching_outputs == "":
            return "Dokumenty k zadanému datu nenalezeny"
        else:
            return searching_outputs
