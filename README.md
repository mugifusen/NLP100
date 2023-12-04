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
git commit -m 'edited(なんでも好きな文字列を)'
git push origin tani
```
つまりこのスクリプトを実行すると、`tani`というブランチに対して一括でadd、commit、pushまでしてくれる。

なので皆が自身のブランチに対しての`git.sh`を作成する場合は、`tani`の部分を自身のブランチ名に変更する必要あり。

```sh
$ sh git.sh
```
でスクリプトを実行。  
```
$ sh g
```
まで打って`Tabキー`を押すと自動で補完してくれる（はず）。
