# This is TANI's branch!
おすすめ設定（真似していいよ）
# git.sh
```sh
$ touch git.sh
```
でファイルを作成。
```
$ vim git.sh
```
でファイルを編集。  
ファイルには以下のように記述する。
```sh
git add -A
git commit -m 'edited'
git push origin tani
```
つまりこのスクリプトを実行すると、`tani`というブランチに対して一括でadd、commit、pushまでしてくれる。

```sh
$ sh git.sh
```
でスクリプトを実行。  
```
sh g
```
まで打って`Tabキー`を押すと自動で補完してくれるはず。
