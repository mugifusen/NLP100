# This is TANI's branch!
教材  
[https://nlp100.github.io/ja/](https://nlp100.github.io/ja/)

以下おすすめ設定（真似していいよ）
# git.sh
`.git`フォルダがあるディレクト（おそらく作成した`NLP100`ディレクトリ直下）にて、ファイルを作成。
```sh
$ touch git.sh
```
ファイルを編集。
```
$ vim git.sh
```  
ファイルには以下のように記述する。
```sh
git add -A
git commit -m 'edited(なんでも好きな文字列を)'
git push origin tani
```
つまりこのスクリプトを実行すると、`tani`というブランチに対して一括でadd、commit、pushまでしてくれる。  
したがって、皆さんが自身のブランチに対しての`git.sh`を作成する場合は、`tani`の部分を自身のブランチ名に変更する必要あり。

`.git`フォルダがあるディレクトにて、以下のコマンドを実行。
```sh
$ sh git.sh
```
下のように、途中まで打って`Tabキー`を押すと自動で補完してくれる（はず）。
```
$ sh g
```
