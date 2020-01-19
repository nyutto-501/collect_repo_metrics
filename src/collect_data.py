import glob


def get_java_file_list(repo_name):
    path = '../repo/before/' + repo_name
    java_files = glob.glob(path + '/**/*.java', recursive=True)
    for i in range(len(java_files)):
        java_files[i] = java_files[i][14:]  # delete before [repo_name]
        # print(java_files[i])
    return java_files


def get_LOC(files):
    """
    /repo/before/[repository]/を見てLOCを出す
    :param files: fileのパスのリスト
    :return: [file_path, LOC]を要素に持つ二次元リスト
    """
    data = []
    head = '../repo/before'
    for file in files:
        path = head + file
        # print(path)
        data.append([file, sum(1 for line in open(path, mode='r'))])
    # print(len(data))
    # print(data)
    return data


def find_begin_hoge(files):
    """
    'begin_hoge'の一覧（とか）を表示
    """
    head = '../repo/after'
    begin_list = []
    # ast_list = []
    for i in range(len(files)):
        path = head + files[i]
        with open(path) as f:
            lines = f.readlines()
        for line in lines:
            if 'begin_' in line:
                if line[:-1] not in begin_list:
                    begin_list.append(line[:-1])
                # if line[:-1] == 'begin_decl_stmt':
                #     print(path)
            # elif 'name|' in line:
            #     pass
            # elif 'literal|' in line:
            #     pass
            # elif 'comment|' in line:
            #     pass
            # elif 'import|' in line:
            #     pass
            # elif 'operator|' in line:
            #     pass
            # else:
            #     if line[:-1] not in ast_list:
            #         ast_list.append(line[:-1])
    for begin_hoge in begin_list:
        print(begin_hoge)
    # for ast in ast_list:
    #     print(ast)


def get_metrics(files):
    """
    'file_path'や'if'などをキーに持つ辞書のリストを作成する．
    'if'などの出現する回数をファイルごとに数える．
    :param files: fileのパスのリスト
    :return: 作成した辞書リスト
    """
    path_loc = get_LOC(files)
    data_list = []
    for i in range(len(path_loc)):
        data = {'file_path': path_loc[i][0], 'LOC': path_loc[i][1],
                'if': 0, 'switch': 0, 'for': 0, 'while': 0, 'do-while': 0, 'try': 0,
                'begin_import': 0, 'begin_class': 0, 'begin_function': 0}
        data_list.append(data)

    head = '../repo/after'
    for data in data_list:
        path = head + data['file_path']
        with open(path) as f:
            lines = f.readlines()
        for line in lines:
            if 'if|' in line:
                data['if'] += 1
            elif 'switch|' in line:
                data['switch'] += 1
            elif 'for|' in line:
                data['for'] += 1
            elif 'while|' in line:
                data['while'] += 1
            elif 'do|while' in line:
                data['do-while'] += 1
            elif 'try|' in line:
                data['try'] += 1
            elif 'begin_import' in line:
                data['begin_import'] += 1
            elif 'begin_class' in line:
                data['begin_class'] += 1
            elif 'begin_function' in line:
                if 'begin_function_decl' in line:
                    pass
                else:
                    data['begin_function'] += 1
    return data_list


if __name__ == '__main__':
    repository_name = 'ant'
    file_paths = get_java_file_list(repository_name)
    # find_begin_hoge(file_paths)
    res = get_metrics(file_paths)
