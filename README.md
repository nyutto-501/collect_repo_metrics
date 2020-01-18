# collect_repo_metrics
gitのリポジトリに含まれるソースファイル（.javaのみを想定）を解析し，LOCなどのメトリクスを抽出，データベースを作成する．

## memo
cregitを適用する前後のリポジトリを保存する．
適用した後，ブランチ切ってコミットしておけばtokenの状態のファイルがmasterブランチに残る．

TODO
- javaファイルのパスの一覧を取得
- beforeからLOCを計算
- afterからif, for, while, begin_class, の数を取得