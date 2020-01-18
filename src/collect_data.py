import subprocess
import glob


def get_java_file_list(repo_name):
    path = '../repo/before/' + repo_name
    java_files = glob.glob(path + '/**/*.java', recursive=True)
    for i in range(len(java_files)):
        java_files[i] = java_files[i][14:]  # delete before [repo_name]
        # print(java_files[i])
    return java_files


def count_LOC(files):
    """
    /repo/before/[repository]/を見てLOCを出す
    :param files: fileのパスのリスト
    :return: [file_path, LOC]を要素に持つ二次元リスト
    """
    data = []
    head = '../repo/before/'
    for file in files:
        path = head + file
        data.append([file, sum(1 for line in open(path, mode='r'))])
    # print(len(data))
    # print(data)
    return data


# TODO: afterから色々取得する


if __name__ == '__main__':
    repository_name = 'ant'
    file_paths = get_java_file_list(repository_name)
    # print(len(file_paths))
    res = count_LOC(file_paths)
