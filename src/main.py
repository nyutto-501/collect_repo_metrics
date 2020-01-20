import collect_data
import make_db


if __name__ == '__main__':
    repository_name = 'ant'
    path = collect_data.get_java_file_list(repository_name)
    data = collect_data.get_metrics(path)
    make_db.make_db('TEST', repository_name, data)
