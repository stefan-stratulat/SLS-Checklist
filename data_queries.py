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
        translation_vendor text,
        cis text,
        internal_kom text,
        check_wf text,
        sls_task text,
        draft_lp text,
        loca_kom text,
        check_msr text,
        check_mqrg text,
        check_ldc text,
        check_paper_source text,
        check_translation_service text,
        check_tft text,
        check_irb text,
        check_quote text,
        check_po text,
        add_quote_po_oct text,
        loca_plan text,
        access_ts_tm text,
        assign_ls_wf text,
        access_platform text,
        handover_ls text,
        notes text,
        to_do text)""")


#select()
conn.commit()

conn.close()

