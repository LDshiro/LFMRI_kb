# Release Process

## Release cadence

- 月次: 軽量スナップショット `vYYYY.MM`
- 四半期: レビュー済み版 `vYYYY.QN`
- 重要更新: 必要に応じて `vX.Y.Z`

## Pre-release checklist

- [ ] `make check` が通る。
- [ ] `make index` を実行した。
- [ ] `CHANGELOG.md` を更新した。
- [ ] `logs/review-log.csv` を更新した。
- [ ] `literature/reading-list.md` の優先度を見直した。
- [ ] `draft` と `stable` の区別を確認した。
- [ ] 公開してはいけないPDF、raw export、患者データが含まれていない。

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
