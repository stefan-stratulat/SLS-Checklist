import sqlite3

conn = sqlite3.connect('studies.db')

c = conn.cursor()

"""c.execute("""CREATE TABLE studies(
        sponsor text,
        study_code text,
        language_number text,
        pm_name text,
        pds_name text,
        device_type text,
        internal_kom integer,
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
        check_po_oct integer,
        loca_plan integer,
        access_ts_tm integer,
        access_platform integer,
        handover_ls integer,
        notes text,
        to_do text)""")"""

conn.commit()

conn.close()

