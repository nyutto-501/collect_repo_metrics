# collect_repo_metrics
gitのリポジトリに含まれるソースファイル（.javaのみを想定）を解析し，LOCなどのメトリクスを抽出，データベースを作成する．

## 使い方
1. repo/beforeにリポジトリをクローンする．
2. クローンしたリポジトリを，cregitで作成されるdockerコンテナ内のrepositoryにコピーする．（docker cp とか使う）
3. cregitを実行し，ブランチを切ってからcommitする（masterでcommitしない．もっといいやり方ありそう）．
cregitはtokenに変換したものを元に戻すところまでやってくれるが，戻す必要がないためこのようにする．
4. 3でできたものをrepo/afterにコピーする．
5. `./main.py [リポジトリ名]` を実行．
6. TEST.dbが作成される．テーブル名は"metrics"にしている．
`sqlite3 TEST.db` して `SELECT * FROM metrics;` とかで見れる．


## memo
cregitを適用する前後のリポジトリを保存する．
適用した後，ブランチ切ってコミットしておけばtokenの状態のファイルがmasterブランチに残る．

### やってること
- javaファイルのパスの一覧を取得
- repo/before からLOCを計算
- repo/after からif|if, switch|switch, for|for, while|while, do|while, try|try, begin_import, begin_class, begin_function の数を取得
- 結果をDBにぶちこむ
