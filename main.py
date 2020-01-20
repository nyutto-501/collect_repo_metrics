#! /usr/bin/env python3
import sys

import src


if __name__ == '__main__':
    args = sys.argv
    if len(args) != 2:
        print('wrong arguments')
        exit()
    db_name = 'TEST'
    repository_name = args[1]
    # repository_name = 'ant'
    path = src.collect_data.get_java_file_list(repository_name)
    data = src.collect_data.get_metrics(path)
    src.make_db.make_db(db_name, repository_name, data)
