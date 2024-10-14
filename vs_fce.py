from tkinter import *
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Querybox
from db_sqllite import Database
from obj_window import ObjWindow
import requests
from bs4 import BeautifulSoup
import datetime
import time
import tkinter as tk


class VsFce:
    def __init__(self, scroledtext, last_run_label):
        self.obj_window = ObjWindow()
        self.database = Database()
        self.records = self.database.query_database()
        self.output = []
        self.datum = self.date_time_now()
        self.scroledtext = scroledtext
        # "2024-02-15 10:32:31"
        self.obj_window.label_last_run_vs = last_run_label
        self.last_run_fce()

    def date_time_now(self):
        datum_src = datetime.datetime.now()
        return datum_src.strftime("%Y-%m-%d %H:%M:%S")

    def last_run_fce(self):
        self.obj_window.label_last_run_vs.config(text=f"LAST RUN: {self.database.last_run_fce_db('vs_fce')}")

    def date_fce(self):
        self.scroledtext.delete('1.0', END)
        cal = Querybox()
        date_input = cal.get_date()
        date_compare_output = self.database.compare_date(date_input)
        txt = ""
        for part_p in date_compare_output:
            for part in part_p:
                txt += f"{part}\n"
            txt += "\n"
        if not txt:
            return "NO RECORD FOUND!!!"
        else:
            return txt

    def run_main_fce(self, progress, frame0):
        # self.frame0 = frame0
        # self.tk.call(("tk", "busy", "hold", self.frame0))
        # try block button viz youtube
        # self.root.bind("<Button-1>", self.print_event)
        # def print_event(self, event):
        #     position = "(x={}, y={})".format(event.x, event.y)
        #     print(event.type, "event", position)
        progress.configure(amountused=0, bootstyle="danger", subtextstyle="danger", subtext="Working", textright="%")
        frame0.update()
        self.scroledtext.delete('1.0', END)
        self.records = self.database.query_database()
        self.output = []
        self.amu()
        progress.step(4)
        frame0.update()
        self.avu()
        progress.step(4)
        frame0.update()
        self.czu()
        progress.step(3)
        frame0.update()
        self.cvut()
        progress.step(4)
        frame0.update()
        self.jamu()
        progress.step(3)
        frame0.update()
        self.ju()
        progress.step(4)
        frame0.update()
        self.mu()
        progress.step(3)
        frame0.update()
        self.mendelu()
        progress.step(4)
        frame0.update()
        self.ou()
        progress.step(3)
        frame0.update()
        self.su()
        progress.step(4)
        frame0.update()
        self.tul()
        progress.step(3)
        frame0.update()
        self.uhk()
        progress.step(4)
        frame0.update()
        self.ujep()
        progress.step(3)
        frame0.update()
        self.uk()
        progress.step(4)
        frame0.update()
        self.up()
        progress.step(3)
        frame0.update()
        self.upce()
        progress.step(4)
        frame0.update()
        self.utb()
        progress.step(3)
        frame0.update()
        self.vetuni()
        progress.step(4)
        frame0.update()
        self.vsb()
        progress.step(4)
        frame0.update()
        self.vse()
        progress.step(4)
        frame0.update()
        self.vscht()
        progress.step(4)
        frame0.update()
        self.vspj()
        progress.step(4)
        frame0.update()
        self.vste()
        progress.step(4)
        frame0.update()
        self.umprum()
        progress.step(4)
        frame0.update()
        self.vut()
        progress.step(4)
        frame0.update()
        self.po()
        progress.step(4)
        frame0.update()
        # self.zcu()
        self.uo()
        progress.step(4)
        frame0.update()
        progress.configure(bootstyle="dark", subtext="DONE", subtextstyle="success", textright="", amountused=0)
        frame0.update()
        time.sleep(2)
        progress.configure(bootstyle="dark", subtextstyle="dark", subtext="", textright="")
        frame0.update()
        self.database.last_run_update_db(self.date_time_now(), "vs_fce")
        self.last_run_fce()
        if self.output == []:
            return "Nové dokumenty nepřidány"
        else:
            return self.text_ou(self.output)

    def text_ou(self, output):
        txt = ""
        for record in output:
            db_record = self.database.main_fce_export(record)
            for part_p in db_record:
                for part in part_p:
                    txt += f"{part}\n"
                txt += "\n"
        print(txt)
        return txt

    # def db_output_txt(self, db_record):
    #     txt = ""
    #     for part_p in db_record:
    #         for part in part_p:
    #             txt += f"{part}\n"
    #         txt += "\n"
    #     print(txt)
    #     return txt

    def amu(self):
        web = self.records[0][2]
        odl_rec = self.records[0][1]
        name = self.records[0][0]
        target_x = self.records[0][4]
        target_y = self.records[0][5]
        oid = 1

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("h4")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda amu")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def avu(self):
        web = self.records[1][2]
        odl_rec = self.records[1][1]
        name = self.records[1][0]
        target_x = self.records[1][4]
        target_y = self.records[1][5]
        oid = 2

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("h2")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda avu")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def czu(self):
        web = self.records[2][2]
        odl_rec = self.records[2][1]
        name = self.records[2][0]
        target_x = self.records[2][4]
        target_y = self.records[2][5]
        oid = 3

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("b")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda czu")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def cvut(self):
        web = self.records[3][2]
        odl_rec = self.records[3][1]
        name = self.records[3][0]
        target_x = self.records[3][4]
        target_y = self.records[3][5]
        oid = 4

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda cvut")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def jamu(self):
        web = self.records[4][2]
        odl_rec = self.records[4][1]
        name = self.records[4][0]
        target_x = self.records[4][4]
        target_y = self.records[4][5]
        oid = 5

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda jamu")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def ju(self):
        web = self.records[5][2]
        odl_rec = self.records[5][1]
        name = self.records[5][0]
        target_x = self.records[5][4]
        target_y = self.records[5][5]
        oid = 6

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda ju")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def mu(self):
        web = self.records[6][2]
        odl_rec = self.records[6][1]
        name = self.records[6][0]
        target_x = self.records[6][4]
        target_y = self.records[6][5]
        oid = 7

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda mu")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def mendelu(self):
        web = self.records[7][2]
        odl_rec = self.records[7][1]
        name = self.records[7][0]
        target_x = self.records[7][4]
        target_y = self.records[7][5]
        oid = 8

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda mendelu")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def ou(self):
        web = self.records[8][2]
        odl_rec = self.records[8][1]
        name = self.records[8][0]
        target_x = self.records[8][4]
        target_y = self.records[8][5]
        oid = 9

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda ou")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def su(self):
        web = self.records[9][2]
        odl_rec = self.records[9][1]
        name = self.records[9][0]
        target_x = self.records[9][4]
        target_y = self.records[9][5]
        oid = 10

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda su")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def tul(self):
        web = self.records[10][2]
        odl_rec = self.records[10][1]
        name = self.records[10][0]
        target_x = self.records[10][4]
        target_y = self.records[10][5]
        oid = 11

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("li")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda tul")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def uhk(self):
        web = self.records[11][2]
        odl_rec = self.records[11][1]
        name = self.records[11][0]
        target_x = self.records[11][4]
        target_y = self.records[11][5]
        oid = 12

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda uhk")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def ujep(self):
        web = self.records[12][2]
        odl_rec = self.records[12][1]
        name = self.records[12][0]
        target_x = self.records[12][4]
        target_y = self.records[12][5]
        oid = 13

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda ujep")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def uk(self):
        web = self.records[13][2]
        odl_rec = self.records[13][1]
        name = self.records[13][0]
        target_x = self.records[13][4]
        target_y = self.records[13][5]
        oid = 14

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a", class_='i-download')[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda uk")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def up(self):
        web = self.records[14][2]
        odl_rec = self.records[14][1]
        name = self.records[14][0]
        target_x = self.records[14][4]
        target_y = self.records[14][5]
        oid = 15

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda up")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def upce(self):
        web = self.records[15][2]
        odl_rec = self.records[15][1]
        name = self.records[15][0]
        target_x = self.records[15][4]
        target_y = self.records[15][5]
        oid = 16

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("span")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda upce")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def utb(self):
        web = self.records[16][2]
        odl_rec = self.records[16][1]
        name = self.records[16][0]
        target_x = self.records[16][4]
        target_y = self.records[16][5]
        oid = 17

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all(class_='content-page')[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a


        if odl_rec == new_rec:
            print("shoda utb")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def vetuni(self):
        web = self.records[17][2]
        odl_rec = self.records[17][1]
        name = self.records[17][0]
        target_x = self.records[17][4]
        target_y = self.records[17][5]
        oid = 18

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda vetuni")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def vsb(self):
        web = self.records[18][2]
        odl_rec = self.records[18][1]
        name = self.records[18][0]
        target_x = self.records[18][4]
        target_y = self.records[18][5]
        oid = 19

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda vsb")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def vse(self):
        web = self.records[19][2]
        odl_rec = self.records[19][1]
        name = self.records[19][0]
        target_x = self.records[19][4]
        target_y = self.records[19][5]
        oid = 20

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("span")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda vse")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def vscht(self):
        web = self.records[20][2]
        odl_rec = self.records[20][1]
        name = self.records[20][0]
        target_x = self.records[20][4]
        target_y = self.records[20][5]
        oid = 21

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda vscht")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def vspj(self):
        web = self.records[21][2]
        odl_rec = self.records[21][1]
        name = self.records[21][0]
        target_x = self.records[21][4]
        target_y = self.records[21][5]
        oid = 22

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")
        new_rec = soup.find_all('li', class_='soubor-ke-stazeni')[0:1]

        for a in new_rec:
            a = a.getText()
            new_rec = a


        if odl_rec == new_rec:
            print("shoda vspj")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def vste(self):
        web = self.records[22][2]
        odl_rec = self.records[22][1]
        name = self.records[22][0]
        target_x = self.records[22][4]
        target_y = self.records[22][5]
        oid = 23

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda vste")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def umprum(self):
        web = self.records[23][2]
        odl_rec = self.records[23][1]
        name = self.records[23][0]
        target_x = self.records[23][4]
        target_y = self.records[23][5]
        oid = 24

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda umprum")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def vut(self):
        web = self.records[24][2]
        odl_rec = self.records[24][1]
        name = self.records[24][0]
        target_x = self.records[24][4]
        target_y = self.records[24][5]
        oid = 25

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda vut")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    # def zcu(self):
    #     web = self.records[25][2]
    #     odl_rec = self.records[25][1]
    #     name = self.records[25][0]
    #     oid = 26
    #
    #     print(web)
    #
    #     response = requests.get(web)
    #     web = response.text
    #     soup = BeautifulSoup(web, "html.parser")
    #
    #     # print(soup)
    #
    #     new_rec = soup.find_all("main")
    #     print(new_rec)
    #     for a in new_rec:
    #         a = a.getText()
    #         new_rec = a
    #         print(new_rec)
    #
    #     if odl_rec == new_rec:
    #         print("shoda uk")
    #     else:
    #         self.output.append(name)
    #         self.database.update_record(new_rec, self.datum, oid)

    def po(self):
        web = self.records[26][2]
        odl_rec = self.records[26][1]
        name = self.records[26][0]
        target_x = self.records[26][4]
        target_y = self.records[26][5]
        oid = 27

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("a")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda po")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)

    def uo(self):
        web = self.records[27][2]
        odl_rec = self.records[27][1]
        name = self.records[27][0]
        target_x = self.records[27][4]
        target_y = self.records[27][5]
        oid = 28

        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")

        new_rec = soup.find_all("p")[target_x:target_y]
        for a in new_rec:
            a = a.getText()
            new_rec = a

        if odl_rec == new_rec:
            print("shoda uo")
        else:
            self.output.append(name)
            self.database.update_record(new_rec, self.datum, oid)


# n = ""
# m = ""
# vsfce = VsFce(n, m)
# vsfce.jamu()

