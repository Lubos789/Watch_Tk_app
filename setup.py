from db_sqllite import Database
from obj_window import ObjWindow
import requests
from bs4 import BeautifulSoup
from tkinter import *



class Setup:
    def __init__(self, scroledtext):
        self.database = Database()
        self.obj_window = ObjWindow()
        self.scroledtext = scroledtext

    def show(self, entry):
        show_output = "PREVIEW OF THE CLOSEST SITE TAGS:\n\n\n"
        self.scroledtext.delete('1.0', END)
        self.obj_window.entry_sub_name = entry
        subject = self.obj_window.entry_sub_name.get()
        # subject = "České vysoké učení technické v Praze (ČVUT)"
        self.records = self.database.setup_query_database(subject)

        web = self.records[2]
        name = self.records[0]
        target_x = self.records[4]
        target_y = self.records[5]
        db_tag = self.records[6]
        clas = self.records[7]
        response = requests.get(web)
        web = response.text
        soup = BeautifulSoup(web, "html.parser")
        print(clas)
        if clas:
            rec = soup.find_all(db_tag, class_=clas)[target_x:target_y]
        else:
            rec = soup.find_all(db_tag)[target_x:target_y]
        # rec = soup.find_all('li', class_='soubor-ke-stazeni')[target_x:target_y]

        print(rec)
        for tag in rec:
            tag = tag.getText()
            rec = tag
        print(rec)

        # uper rec
        upper_text = ""
        for n in range(3, 0, -1):
            upper_x = target_x - n
            upper_y = target_y - n

            upper_rec = soup.find_all(db_tag)[upper_x:upper_y]
            print(upper_x)
            print(upper_y)

            for tag in upper_rec:
                upper_rec_part = tag.getText()
                upper_text += f"{upper_rec_part}\n\n"
            print(upper_text)
        print("-------------------------------------------------")
        # downer rec
        downer_text = ""
        for n in range(1, 4):
            downer_x = target_x + n
            downer_y = target_y + n

            downer_rec = soup.find_all(db_tag)[downer_x:downer_y]
            print(downer_x)
            print(downer_y)

            for tag in downer_rec:
                downer_rec = tag.getText()
                downer_text += f"{downer_rec}\n\n"
            print(downer_text)

        show_output += f"---------- tags before -----------------------------------------{20 * '-'}\n\n{upper_text}\n\n"
        show_output += f"---------- target tag ------------------------------------------{20 * '-'}\n\n{rec}\n\n\n\n" \
                       f"---------- tags after ------------------------------------------{20 * '-'}\n\n"
        show_output += f"{downer_text}"

        print(show_output)
        return show_output

    def up(self, entry):
        self.obj_window.entry_sub_name = entry
        subject = self.obj_window.entry_sub_name.get()
        # subject = "České vysoké učení technické v Praze (ČVUT)"
        self.records = self.database.setup_query_database(subject)
        target_x = self.records[4]
        target_y = self.records[5]
        target_x -= 1
        target_y -= 1
        self.database.setup_update_target(subject, target_x, target_y)

        return self.show(entry)


    def down(self, entry):
        self.obj_window.entry_sub_name = entry
        subject = self.obj_window.entry_sub_name.get()
        # subject = "České vysoké učení technické v Praze (ČVUT)"
        self.records = self.database.setup_query_database(subject)
        target_x = self.records[4]
        target_y = self.records[5]
        target_x += 1
        target_y += 1
        self.database.setup_update_target(subject, target_x, target_y)

        return self.show(entry)

# setup = Setup("")
# setup.show("Vysoká škola polytechnická Jihlava (VŠPJ)")


# after up or down update last_recort v db ?
