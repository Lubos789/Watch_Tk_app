import sqlite3
import pandas as pd
import openpyxl

# # Databases
# # Create a database or connect to one
# conn = sqlite3.connect('control_app_records.db')
# # Create cursor
# c = conn.cursor()
# # Create table
# c.execute("""
#     CREATE TABLE IF NOT EXISTS vs_skoly (
#         subject_name TEXT,
#         last_record TEXT,
#         web TEXT,
#         date TEXT
#
#     );
#     """)
# # Commit changes
# conn.commit()
# # Close Connection
# conn.close()
# # ------------------------------------------------------
#
# # Create a database or connect to one
# conn = sqlite3.connect('control_app_records.db')
# # Create cursor
# c = conn.cursor()
#
# data = [
#     ["Akademie múzických umění v Praze (AMU)", "test", "https://www.amu.cz/cs/uredni-deska/strategicke_dokumenty/vyrocni-zpravy/", "15-11-2024"],
#     ["Akademie výtvarných umění v Praze (AVU)", "test", "https://avu.cz/stranka/vyrocni-zpravy", "15-11-2024"],
#     ["Česká zemědělská univerzita v Praze (ČZU)", "test", "https://www.czu.cz/cs/r-7210-o-czu/r-7702-oficialni-dokumenty/r-7812-vyrocni-zpravy", "15-11-2024"],
#     ["České vysoké učení technické v Praze (ČVUT)", "test", "https://www.cvut.cz/rozvoj/vyrocni-zpravy", "15-11-2024"],
#     ["Janáčkova akademie múzických umění (JAMU)", "test", "https://is.jamu.cz/do/jamu/doc/5499/Vyrocni_zpravy_hospodareni/", "15-11-2024"],
#     ["Jihočeská univerzita v Českých Budějovicích (JU)", "test", "https://www.jcu.cz/cz/univerzita/dokumenty/vyrocni-zprava-ju/vyrocni-zpravy-ju-o-hospodareni", "15-11-2024"],
#     ["Masarykova univerzita (MU)", "test", "https://www.muni.cz/o-univerzite/uredni-deska/vyrocni-zpravy-mu-a-soucasti#mu", "15-11-2024"],
#     ["Mendelova univerzita v Brně (MENDELU)", "test", "https://mendelu.cz/o-univerzite/uredni-deska/vyrocni-zpravy-univerzity/", "15-11-2024"],
#     ["Ostravská univerzita (OU)", "test", "https://www.osu.cz/dokumenty/", "15-11-2024"],
#     ["Slezská univerzita v Opavě (SU)", "test", "https://www.slu.cz/slu/cz/udvyrocnizpravy", "15-11-2024"],
#     ["Technická univerzita v Liberci (TUL)", "test", "https://www.tul.cz/univerzita/uredni-deska/vyrocni-zpravy/", "15-11-2024"],
#     ["Univerzita Hradec Králové (UHK)", "test", "https://www.uhk.cz/cs/univerzita-hradec-kralove/uhk/uredni-deska/verejne-informace/vyrocni-zpravy", "15-11-2024"],
#     ["Univerzita Jana Evangelisty Purkyně v Ústí nad Labem (UJEP)", "test", "https://www.ujep.cz/cs/vyrocni-zpravy", "15-11-2024"],
#     ["Univerzita Karlova (UK)", "test", "https://cuni.cz/UK-8533.html", "15-11-2024"],
#     ["Univerzita Palackého v Olomouci (UP)", "test", "https://strategie.upol.cz/strategicke-dokumenty/vyrocni-zpravy/", "15-11-2024"],
#     ["Univerzita Pardubice (UPCE)", "test", "https://www.upce.cz/deska/dokumenty/vyr-zpravy.html#panel_28917", "15-11-2024"],
#     ["Univerzita Tomáše Bati ve Zlíně (UTB)", "test", "https://www.utb.cz/univerzita/uredni-deska/ruzne/vyrocni-zpravy/", "15-11-2024"],
#     ["Veterinární univerzita Brno (VETUNI)", "test", "https://www.vetuni.cz/vyrocni-zpravy-a-hodnoceni-cinnosti", "15-11-2024"],
#     ["Vysoká škola báňská - Technická univerzita Ostrava (VŠB)", "test", "https://www.vsb.cz/cs/o-univerzite/uredni-deska/vyrocni-zpravy", "15-11-2024"],
#     ["Vysoká škola ekonomická v Praze (VŠE)", "test", "https://www.vse.cz/informace-o-vse/profil-skoly/vyrocni-zpravy/", "15-11-2024"],
#     ["Vysoká škola chemicko-technologická v Praze (VŠCHT Praha)", "test", "https://www.vscht.cz/uredni-deska/zakladni-dokumenty/vyrocni-zpravy", "15-11-2024"],
#     ["Vysoká škola polytechnická Jihlava (VŠPJ)", "test", "https://www.vspj.cz/skola/uredni-deska/vyrocni-zpravy-o-hospodareni", "15-11-2024"],
#     ["Vysoká škola technická a ekonomická v Českých Budějovicích (VŠTE)", "test", "https://is.vstecb.cz/do/vste/uredni_deska/VZ/", "15-11-2024"],
#     ["Vysoká škola uměleckoprůmyslová v Praze (UMPRUM)", "test", "https://www.umprum.cz/www/cs/web/o-umprum/uredni-deska/strategicke-dokumenty", "15-11-2024"],
#     ["Vysoké učení technické v Brně (VUT)", "test", "https://www.vut.cz/uredni-deska/vyrocni-zpravy-vut/vyrocni-zpravy-vut-f18830", "15-11-2024"],
#     ["Západočeská univerzita v Plzni (ZČU)", "no fce", "https://www.zcu.cz/cs/University/Important-documents/index.html#VZpr", "2024-02-13 13:20:11"],
#     ["Policejní akademie České republiky v Praze (PO)", "test", "https://www.polac.cz/g2/view.php?dokument/index.html", "15-11-2024"],
#     ["Univerzita obrany (UO)", "test", "https://unob.cz/univerzita/dokumenty/vyrocni-zpravy-uo/", "15-11-2024"]
# ]
#
# for record in data:
#     c.execute("INSERT INTO vs_skoly VALUES (:subject_name, :last_record, :web, :date)",
#               {
#                 'subject_name': record[0],
#                 'last_record': record[1],
#                 'web': record[2],
#                 'date': record[3]
#               }
#               )
#
# # Commit chang
# conn.commit()
# # Close Connection
# conn.close()

# --------------------------- LAST RUN TABLE -------------------------------------
# # Create a database or connect to one
# conn = sqlite3.connect('control_app_records.db')
# # Create cursor
# c = conn.cursor()
# # Create table
# c.execute("""
#     CREATE TABLE IF NOT EXISTS last_run (
#         fce_to_memo TEXT,
#         date TEXT
#     );
#     """)
# # Commit changes
# conn.commit()
# # Close Connection
# conn.close()
# # ------------------------------------------------------
#
# # Create a database or connect to one
# conn = sqlite3.connect('control_app_records.db')
# # Create cursor
# c = conn.cursor()
#
# data = [
#     ["vs_fce", "2024-02-15 10:32:31"],
#     ["vvi_fce", "2024-02-15 10:32:31"],
#     ["podniky_v_likvidaci_fce", "2024-02-15 10:32:31"],
#     ["or_fce", "2024-02-15 10:32:31"],
# ]
#
# for record in data:
#     c.execute("INSERT INTO last_run VALUES (:fce_to_memo, :date)",
#               {
#                 'fce_to_memo': record[0],
#                 'date': record[1],
#               }
#               )
#
# # Commit chang
# conn.commit()
# # Close Connection
# conn.close()

# --------------------------------------------------------------------------

# -------
# SELECT subject_name, web FROM vs_skoly
# WHERE date > "2024-02-15 10:32:31";
# -------

# ------------------- podniky-------------------------------------------------------------------------------------------

# # Create a database or connect to one
# conn = sqlite3.connect('control_app_records.db')
# # Create cursor
# c = conn.cursor()
# # Create table
# c.execute("""
#     CREATE TABLE IF NOT EXISTS statni_podniky (
#         web_id TEXT,
#         last_record TEXT,
#         web_address TEXT,
#         date TEXT,
#         link_to_dc TEXT,
#         name_of_subject
#
#     );
#     """)
# # Commit changes
# conn.commit()
# # Close Connection
# conn.close()
# # ------------------------------------------------------
#
# # Create a database or connect to one
# conn = sqlite3.connect('control_app_records.db')
# # Create cursor
# c = conn.cursor()
#
# # data = ['555249', '59981', '421745', '698257', '54435', '539505', '422055', '55479', '707389', '94331', '540281',
# #                '653893', '707795', '715543', '156901', '214034', '422176', '548927', '705650', '14200', '705055',
# #                '197960', '433082', '153005', '648534', '101482', '232449', '703613', '63996', '708491', '232598',
# #                '620172', '680072', '68370', '707464', '61898', '883621', '421257', '422060', '423315', '678007',
# #                '433958', '157000', '421841', '706866', '538121', '422467', '473760', '56839', '46595', '55727',
# #                '724833', '923323', '678947']
#
# data = ['715849', '422987', '539388', '411213', '538390', '62310', '706318', '42326', '136274', '452693', '561634',
#         '218815', '704580', '135795', '670012', '490737', '422784', '540195', '685592', '411036', '423035', '724566',
#         '423110', '685292', '428491', '422955', '670021', '540294', '654377', '345155', '423080', '452841', '572937',
#         '94288', '527391', '156922', '653645', '540463', '540387', '421949', '717171', '653744', '42280', '42278',
#         '424888', '94792', '712867', '540523', '710141', '699582', '421349', '422485', '156947', '156873']
#
# for record in data:
#     c.execute("INSERT INTO statni_podniky VALUES (:web_id, :last_record, :web_address, :date, :link_to_dc, :name_of_subject)",
#               {
#                 'web_id': record,
#                 'last_record': "test",
#                 'web_address': "test",
#                 'date': "test",
#                 'link_to_dc': "test",
#                 'name_of_subject': "test"
#               }
#               )
#
# # Commit chang
# conn.commit()
# # Close Connection
# conn.close()


# ----------------- VVI ----------------------------------
# # Create a database or connect to one
# conn = sqlite3.connect('control_app_records.db')
# # Create cursor
# c = conn.cursor()
# # Create table
# c.execute("""
#     CREATE TABLE IF NOT EXISTS vvi (
#         ICO TEXT,
#         Name TEXT,
#         last_record TEXT
#     );
#     """)
# # Commit changes
# conn.commit()
# # Close Connection
# conn.close()
# ------------------------------------------------------


# # Create a database or connect to one
# conn = sqlite3.connect('control_app_records.db')
# # Create cursor
# c = conn.cursor()
#
# df = pd.read_excel("vvi.xlsx")
# ico_f = df['ICO']
#
# name_f = df['Nazev_vyzkumne_organizace']
#
#
# for n, ico in enumerate(ico_f):
#     c.execute("INSERT INTO vvi VALUES (:ico, :name, :last_record)",
#               {
#                 'ico': ico,
#                 'name': name_f[n],
#                 'last_record': 'test'
#               }
#               )
#
# # Commit chang
# conn.commit()
# # Close Connection
# conn.close()

class Database:

    def query_database(self):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM vs_skoly")
        records = c.fetchall()
        # print(records)

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()

        return records

    def update_record(self, new_record, date, id_id):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()
        c.execute("""UPDATE vs_skoly SET
            last_record = :last,
            date = :date
        
        WHERE oid = :oid""",
        {
            'last': new_record,
            'date': date,
            'oid': id_id,
        })

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()

    def compare_date(self, date):
        compared_date = date
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()

        c.execute(f"""SELECT subject_name, web FROM vs_skoly
            WHERE date > "{compared_date}";""")

        records = c.fetchall()
        # print(records)

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()
        return records

    def main_fce_export(self, name):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()

        c.execute(f"""SELECT subject_name, web FROM vs_skoly
                        WHERE subject_name = "{name}";""")

        records = c.fetchall()
        # print(records)

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()
        return records

    def last_run_fce_db(self, druh_fce):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()

        c.execute(f"""SELECT date FROM last_run
            WHERE fce_to_memo = "{druh_fce}";""")

        records = c.fetchone()
        clean_record = list(records)
        for date in clean_record:
            clean_date = date

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()
        return clean_date

    def last_run_update_db(self, date, fce_to_memo):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()
        c.execute("""UPDATE last_run SET
            date = :date

        WHERE fce_to_memo = :fce_to_memo""",
                  {
                      'date': date,
                      'fce_to_memo': fce_to_memo,
                  })

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()


# fce_to_memo = "vs_fce"
# date = "2024-02-15 10:32:29"
# database = Database()
# database.last_run_update_db(date, fce_to_memo)

# Statni podniky  -----------------------------------------------------------------------------------------------------

    def one_line_record_podniky(self, web_id):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()

        c.execute(f"""SELECT * FROM statni_podniky
            WHERE web_id = "{web_id}";""")
        records = c.fetchone()
        # print(records)

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()

        return records

    def fill_table_podniky(self, one_address, web_last_record, name_of_subject, add_to_folder_date, link_to_view, link_to_doc_page):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()
        c.execute("""UPDATE statni_podniky SET
            last_record = :last_record,
            web_address = :web_address,
            date = :date,
            link_to_dc = :link_to_dc,
            name_of_subject = :name_of_subject

        WHERE web_id = :web_id""",
                  {

                      'web_id': one_address,
                      'last_record': web_last_record,
                      'web_address': link_to_view,
                      'date': add_to_folder_date,
                      'link_to_dc': link_to_doc_page,
                      'name_of_subject': name_of_subject
                  })

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()
        print(f"done {name_of_subject}")

    def update_record_podniky(self, new_record, date, one_address, app_change_date):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()
        c.execute("""UPDATE statni_podniky SET
            last_record = :last,
            date = :date,
            date_app_change = :app_change_date

        WHERE web_id = :web_id""",
                  {
                      'last': new_record,
                      'date': date,
                      'web_id': one_address,
                      'app_change_date': app_change_date
                  })

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()
        print(new_record)


    def setup_query_database(self, subject_name):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()

        c.execute(f"""SELECT * FROM vs_skoly
            WHERE subject_name = "{subject_name}";""")
        records = c.fetchone()
        # print(records)

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()

        return records


    def setup_update_target(self, subject_name,target_x, target_y):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()
        c.execute("""UPDATE vs_skoly SET
            target_x = :target_x,
            target_y = :target_y

        WHERE subject_name = :subject_name""",
                  {
                      'target_x': target_x,
                      'target_y': target_y,
                      'subject_name': subject_name,
                  })

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()


# database = Database()
# database.setup_update_target("Západočeská univerzita v Plzni (ZČU)", 3, 4)

#  ------------ VVI ----------------------------------------------------------------------------------

    def query_database_vvi(self):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()

        c.execute("SELECT * FROM vvi")
        records = c.fetchall()
        # print(records)

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()

        return records

    def update_record_vvi(self, record, ico, app_change_date):
        # Create a database or connect to one
        conn = sqlite3.connect('control_app_records.db')
        # Create cursor
        c = conn.cursor()
        c.execute("""UPDATE vvi SET
            last_record = :record,
            date_app_change = :app_change_date

        WHERE ICO = :ico""",
                  {
                      'record': record,
                      'ico': ico,
                      'app_change_date': app_change_date,
                  })

        # Commit changes
        conn.commit()
        # Close Connection
        conn.close()
