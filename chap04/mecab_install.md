### aptitudeのインストール
```
sudo apt-get install aptitude
```
### MeCabのインストール
```
sudo aptitude install make automake autoconf autotools-dev m4 mecab libmecab-dev mecab-ipadic-utf8 git make curl xz-utils file
```
```
Do you want to continue? [Y/n] y
```
```
sudo sed -i -e 's%/lib/mecab/dic%/share/mecab/dic%' /usr/bin/mecab-config
```
### mecab-ipadic-NEologdのインストール
```
git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git
```
```
cd mecab-ipadic-neologd
/mecab-ipadic-neologd$ ./bin/install-mecab-ipadic-neologd -n
```
```
[install-mecab-ipadic-NEologd] : Do you want to install mecab-ipadic-NEologd? Type yes or no.
yes
```
### mecab-Python3のインストール
```
pip install mecab-python3
```