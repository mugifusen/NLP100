# NLP100本ノック
安藤研2023年度12月から始まる勉強会として、
言語処理100本ノックに取り組みます。 \
教材：https://nlp100.github.io/ja/

参加者は毎週1章(10問)を解いてください。
勉強会では担当者に問題の解説をしてもらいます。

## 使い方
1. まずリポジトリをクローンしてください。
```
$ git clone git@github.com:mugifusen/NLP100.git
```

2. 次に自分のブランチを作成し、そのブランチに移動します。\
(以下のSampleという名前は各自のブランチ名に変更してください)
```
$ git checkout -b Sample 
```

作成したソースコードは各章ごとにフォルダで管理します。
フォルダ名・ファイル名共に2桁の数字にしてください \
(e.g. `chap01`, `ans01`)

3. `git add`と`git commit`は作業のキリが良いところでする
```
$ git add -A
$ git commit -m "your message"
```

特定のファイルのみコミット
```
$ git add { ファイルパス }
```

コメントがいらない場合
```
$ git commit --allow-empty-message -m ""
```

4. GitHubのリモートリポジトリに反映
```
$ git push origin Sample
```

## よく使うコマンド
- `git branch` : 現在いるブランチを表示できる
- `git branch Sample` : ブランチを作成できる
- `git checkout Sample` or `git switch Sample` : ブランチの移動
- `git pull` : リモートリポジトリの最新状態をローカルに反映
- `git status` : 作業ディレクトリの状態とステージングエリアの状態を表示