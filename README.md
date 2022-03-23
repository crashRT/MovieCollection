# MovieCollection
## これは何
映像のリファレンスを管理するサイト。

Youtube, Vimeo 両方の映像を管理することができる。

また、タグ機能や映像作家の名前での検索機能をつけた。


# 使い方
## 事前準備
必要なものは以下のとおり。

- Python (3.10.x)
- Django (4.0.x)
- Django-taggit

映像のリストをリセットする場合は、
1. `db.sqlite3`を削除
2. `manage.py`のあるディレクトリに移動
3. `python3 manage.py migrate`を実行

サイトの起動は
`manage.py`のあるディレクトリで
`python3 manage.py runserver`

サイトは`localhost:8000`でアクセスできる

## サイトの使い方
### 1. 映像作品の追加
各ページにある「追加」ボタンを押すと、映像追加のページへ移動する。

フォームに以下のように入力する
- タイトル：タイトルを入力
- 埋め込みリンク：YoutubeやVimeoの共有ボタンからコピーできる埋め込みリンクを入力する
- 映像作家：映像作家の名前を入力する；複数人いる場合は で区切カンマなどして入力する。
- 概要：概要欄の情報やメモなどを入力
- タグ：タグを追加する。下にタグ一覧を表示しているので、そこから選んで入力するか、新規作成する場合はそれを入力すれば良い。カンマで区切れば複数登録できる。

入力が終われば、追加ボタンを押すとリストに追加される。

### 2. 情報の編集、削除
