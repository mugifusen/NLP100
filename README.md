# This is TANI's branch!
おすすめ設定（真似していいよ）
# git.sh
```sh
$ sh git.sh
```
を打つと、その中に記述されているスクリプトが実行される。  
`git.sh`のファイルは以下の内容が記述されている。
```
git add -A
git commit -m 'edited'
git push origin tani
```
つまりこのスクリプトを実行すると、`tani`というブランチに対して一括でadd、commit、pushまでしてくれる。
