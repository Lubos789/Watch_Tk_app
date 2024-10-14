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


class StatPodFce:
    def __init__(self, scroledtext, type_address, last_run_label, last_run):
        address_podniky = ['555249', '59981', '421745', '698257', '54435', '539505', '422055', '55479', '707389', '94331', '540281', '653893', '707795', '715543', '156901', '214034', '422176', '548927', '705650', '14200', '705055', '197960', '433082', '153005', '648534', '101482', '232449', '703613', '63996', '708491', '232598', '620172', '680072', '68370', '707464', '61898', '883621', '421257', '422060', '423315', '678007', '433958', '157000', '421841', '706866', '538121', '422467', '473760', '56839', '46595', '55727', '724833', '923323', '678947']
        address_likvidace = ['715849', '422987', '539388', '411213', '538390', '62310', '706318', '42326', '136274', '452693', '561634', '218815', '704580', '135795', '670012', '490737', '422784', '540195', '685592', '411036', '423035', '724566', '423110', '685292', '428491', '422955', '670021', '540294', '654377', '345155', '423080', '452841', '572937', '94288', '527391', '156922', '653645', '540463', '540387', '421949', '717171', '653744', '42280', '42278', '424888', '94792', '712867', '540523', '710141', '699582', '421349', '422485', '156947', '156873']
        if type_address == 1:
            self.address_list = address_podniky
        else:
            self.address_list = address_likvidace

        self.obj_window = ObjWindow()
        self.database = Database()
        self.output = []
        self.datum = self.date_time_now()
        self.scroledtext = scroledtext
        self.obj_window.label_last_run_podniky = last_run_label
        self.last_run = last_run
        self.last_run_fce()

    def date_time_now(self):
        datum_src = datetime.datetime.now()
        return datum_src.strftime("%Y-%m-%d %H:%M:%S")

    def last_run_fce(self):
        self.obj_window.label_last_run_podniky.config(text=f"LAST RUN: {self.database.last_run_fce_db(self.last_run)}")

    def web_last_record(self, soup):
        web_last_record = soup.find_all("span")[10:12]
        web_last_record_Text = "Typ listiny - "
        for one_span in web_last_record:
            x = one_span.getText()
            web_last_record_Text += " " + x
        return web_last_record_Text

    def add_to_folder_date(self, soup):
        zalozeno_do_sl_all = soup.find_all("td")[8:9]
        zalozeno_do_sl = ""
        for zalozeno_do_sl_part in zalozeno_do_sl_all:
            zalozeno_do_sl = zalozeno_do_sl_part.getText()
        return zalozeno_do_sl

    def link_to_doc_page(self, soup):
        doc_link_tag = soup.find_all("a")[3:4]
        part_link = ""
        for link in doc_link_tag:
            part_link = link.get("href")
        half_link = part_link[1:]
        link_to_doc_page = "https://or.justice.cz/ias/ui" + half_link
        return link_to_doc_page

    def doc_link_tag_download(self, soup):
        doc_link_tag_download = soup.find_all("a")[4:8]
        doc_link_part = ""
        time.sleep(1)
        for doc_link_work in doc_link_tag_download:
            doc_link_part = doc_link_work.get("href")
        doc_link = f"https://or.justice.cz{doc_link_part}"
        return doc_link

    def date_fce(self, progress, frame0):
        searching_outputs = ""
        self.scroledtext.delete('1.0', END)
        cal = Querybox()
        date_input = str(cal.get_date())
        print(date_input)

        step = round(100 / len(self.address_list))
        progress.configure(amountused=0, bootstyle="danger", subtextstyle="danger", subtext="Working", textright="%")
        frame0.update()
        for one_address in self.address_list:
            if progress['amountused'] > 90:
                step = 1
            progress.step(step)
            frame0.update()

            response = requests.get(f"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId={one_address}")
            web = response.text
            soup = BeautifulSoup(web, "html.parser")
            name = soup.find("h2").getText()
            link_to_view = f"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId={one_address}"
            or_tables_pages = pd.read_html(f"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId={one_address}")
            df = or_tables_pages[1]
            df['Založeno do SL'] = pd.to_datetime(df['Založeno do SL'], dayfirst=True)
            df = df[df['Založeno do SL'] > date_input]
            if not df.empty:
                table_found_str = df.to_string()
                searching_message = f"{name}:\n\n {table_found_str}\n\nOdkaz na Náhled: \n{link_to_view}\n{180 * '-'}\n\n"
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



    def run_main_fce(self, progress, frame0):
        step = round(100 / len(self.address_list))
        progress.configure(amountused=0, bootstyle="danger", subtextstyle="danger", subtext="Working", textright="%")
        frame0.update()
        self.scroledtext.delete('1.0', END)
        txt_output = "ZMĚNY U NÁSLEDUJÍCÍCH SUBĚKTŮ:\n\n\n"
        for one_address in self.address_list:
            if progress['amountused'] > 90:
                step = 1
            progress.step(step)
            frame0.update()

            line_record_db = self.database.one_line_record_podniky(one_address)
            last_record = line_record_db[1]

            response = requests.get(f"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId={one_address}")
            web = response.text
            soup = BeautifulSoup(web, "html.parser")

            web_last_record = self.web_last_record(soup)
            name_of_subject = soup.find("h2").getText()
            add_to_folder_date = self.add_to_folder_date(soup)
            link_to_view = f"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId={one_address}"
            link_to_doc_page = self.link_to_doc_page(soup)

            or_tables_pages = pd.read_html(f"https://or.justice.cz/ias/ui/vypis-sl-firma?subjektId={one_address}")
            content = or_tables_pages[1][:5]
            table_string = content.to_string()
            doc_link_tag_download = self.doc_link_tag_download(soup)
# ----------------------------------------------------------------------------------------------------------------------
#             self.database.fill_table_podniky(one_address, web_last_record, name_of_subject, add_to_folder_date, link_to_view, link_to_doc_page)
# ----------------------------------------------------------------------------------------------------------------------
            if last_record == web_last_record:
                print(f"{name_of_subject} lr == wlr\n")

            else:
                txt_part = f"{name_of_subject}\nZveřejněno na stránkách dne: {add_to_folder_date}\n\nNáhled:\n\n\n{table_string}\n\nOdkaz na náhled suběktu:\n{link_to_view}" \
                           f"\n\nOdkaz na náhlede dokumetu ke stažení:\n{link_to_doc_page}\n\nStažení dokumetnu:\n{doc_link_tag_download}\n\n{180 * '-'}\n\n"
                print(txt_part)
                txt_output += txt_part
                self.database.update_record_podniky(web_last_record, add_to_folder_date, one_address, self.date_time_now())

        progress.configure(bootstyle="dark", subtext="DONE", subtextstyle="success", textright="", amountused=0)
        frame0.update()
        time.sleep(2)
        progress.configure(bootstyle="dark", subtextstyle="dark", subtext="", textright="")
        frame0.update()
        self.database.last_run_update_db(self.date_time_now(), self.last_run)
        self.last_run_fce()
        if txt_output == "ZMĚNY U NÁSLEDUJÍCÍCH SUBĚKTŮ:\n\n\n":
            return "Nové dokumenty nepřidány"
        else:
            return txt_output



# n = ""
# statpodfec = StatPodFce(n, 0, n)
# statpodfec.run_main_fce(progress, frame0)


