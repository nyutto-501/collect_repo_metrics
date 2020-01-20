import sqlite3


def make_db(db_name, table_name, data):
    db = '../' + db_name + '.db'
    conn = sqlite3.connect(db)
    cur = conn.cursor()

    cur.execute(f'DROP TABLE IF EXISTS {table_name}')
    cur.execute(f"""
                CREATE TABLE {table_name}(id INTEGER PRIMARY KEY AUTOINCREMENT, path TEXT, loc INTEGER,
                if INTEGER, switch INTEGER, for INTEGER, while INTEGER, "do-while" INTEGER, try INTEGER,
                begin_import INTEGER, begin_class INTEGER, begin_function INTEGER)
                """)

    p = """
    INSERT INTO ant(path, loc, if, switch, for, while, "do-while", try, begin_import, begin_class, begin_function) 
    VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
    for i in range(len(data)):
        cur.execute(p, (data[i]['file_path'], data[i]['LOC'],
                        data[i]['if'], data[i]['switch'], data[i]['for'], data[i]['while'], data[i]['do-while'],
                        data[i]['try'],
                        data[i]['begin_import'], data[i]['begin_class'], data[i]['begin_function']))
    conn.commit()
    conn.close()


if __name__ == '__main__':
    sample_data = [{'file_path': 'hoge', 'LOC': 0,
                    'if': 0, 'switch': 0, 'for': 0, 'while': 0, 'do-while': 0, 'try': 0,
                    'begin_import': 0, 'begin_class': 0, 'begin_function': 0},
                   {'file_path': 'piyo', 'LOC': 1,
                    'if': 0, 'switch': 0, 'for': 0, 'while': 0, 'do-while': 0, 'try': 0,
                    'begin_import': 0, 'begin_class': 0, 'begin_function': 0}
                   ]
    make_db('TEST', 'ant', sample_data)
