import sqlite3

conn = sqlite3.connect('studies.db')

c = conn.cursor()

"""Create table studies that contains all our widgets from the checklist"""
c.execute("""CREATE TABLE IF NOT EXISTS studies(
        sponsor text,
        study_code text,
        language_number text,
        pm_name text,
        pds_name text,
        device_type text,
        cis text,
        internal_kom text,
        check_wf integer,
        sls_task integer,
        draft_lp integer,
        loca_kom integer,
        check_msr integer,
        check_mqrg integer,
        check_ldc integer,
        check_paper_source integer,
        check_translation_service integer,
        check_tft integer,
        check_irb integer,
        check_quote integer,
        check_po integer,
        add_quote_po_oct integer,
        loca_plan integer,
        access_ts_tm integer,
        assign_ls_wf integer,
        access_platform integer,
        handover_ls integer,
        notes text,
        to_do text)""")


c.execute("SELECT * from studies")
column_name = [row[0] for row in c.description]

print(*column_name)

#select()
conn.commit()

conn.close()

