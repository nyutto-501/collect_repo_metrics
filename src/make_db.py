import sqlite3
import os
import subprocess
import re


def get_host_owner(repo):
    os.chdir('./repo/before/' + repo)
    proc = subprocess.run(['git', 'remote', '-v'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    proc = proc.stdout.decode('utf8')
    pattern = 'https://(.*?)/(.*?)/.*?.git'
    res = re.search(pattern, proc)
    os.chdir('../../../')
    return res.group(1), res.group(2)


def make_db(db_name, repo_name, data):
    db = './' + db_name + '.db'
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute(f"""
                CREATE TABLE IF NOT EXISTS metrics(id INTEGER PRIMARY KEY AUTOINCREMENT, host TEXT, owner TEXT, repo TEXT, path TEXT, loc INTEGER,
                if INTEGER, switch INTEGER, for INTEGER, while INTEGER, "do-while" INTEGER, try INTEGER,
                begin_import INTEGER, begin_class INTEGER, begin_function INTEGER)
                """)

    p = """
    INSERT INTO metrics(host, owner, repo, path, loc, if, switch, for, while, "do-while", try, begin_import, begin_class, begin_function) 
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    host, owner = get_host_owner(repo_name)
    for i in range(len(data)):
        cur.execute(p, (host, owner, repo_name, data[i]['file_path'], data[i]['LOC'],
                        data[i]['if'], data[i]['switch'], data[i]['for'], data[i]['while'], data[i]['do-while'],
                        data[i]['try'],
                        data[i]['begin_import'], data[i]['begin_class'], data[i]['begin_function']))
    conn.commit()
    conn.close()
