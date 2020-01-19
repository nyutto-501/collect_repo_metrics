# collect_repo_metrics
gitのリポジトリに含まれるソースファイル（.javaのみを想定）を解析し，LOCなどのメトリクスを抽出，データベースを作成する．

## memo
cregitを適用する前後のリポジトリを保存する．
適用した後，ブランチ切ってコミットしておけばtokenの状態のファイルがmasterブランチに残る．

### やってること
- javaファイルのパスの一覧を取得
- repo/before からLOCを計算
- repo/after からif|if, switch|switch, for|for, while|while, do|while, try|try, begin_import, begin_class, begin_function の数を取得
- 結果をDBにぶちこむ
