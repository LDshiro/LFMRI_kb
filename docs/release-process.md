# Release Process

## Release cadence

- 月次: 軽量スナップショット `vYYYY.MM`
- 四半期: レビュー済み版 `vYYYY.QN`
- 重要更新: 必要に応じて `vX.Y.Z`

## Pre-release checklist

- [ ] `make check` が通る。
- [ ] `make index` を実行した。
- [ ] テスト結果をユーザーへ共有した。
- [ ] `git commit`、`git push`、`git tag` などの git 更新について、ユーザーの明示的承認を得た。
- [ ] `CHANGELOG.md` を更新した。
- [ ] `logs/review-log.csv` を更新した。
- [ ] `literature/reading-list.md` の優先度を見直した。
- [ ] `draft` と `stable` の区別を確認した。
- [ ] 公開してはいけないPDF、raw export、患者データが含まれていない。

## Approval gate

- Codexは、リリース前の確認や検証コマンドを実行してよい。
- ただし、`git commit`、`git push`、`git tag` は、結果を要約して共有し、ユーザーの承認を得た後に行う。
- テスト未実行または失敗時は、その状態を明示した上で承認を求める。

## Tagging

```bash
git tag -a v0.1.0 -m "Initial low-field MRI KB scaffold"
git push origin v0.1.0
```

## Release bundle

```bash
make bundle
```

生成物は `release-bundles/` に出力されます。公開前に中身を確認してください。
