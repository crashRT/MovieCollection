# MovieCollection
映像のリファレンス管理サイトを作りたい

Youtube, Vimeo, Twitter, Instagram のつよい映像を一箇所にまとめたい


## 個人用サーバーの建て方
自分用のリストがほしい場合

### 前提
docker インストール済

### 手順
- リポジトリを clone する
- 僕が追加したものを含めたくない場合は `db.sqlite` を削除
- 以下のコマンドを実行
```bash
docker compose up -d
```
