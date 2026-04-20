# Prompt: Claim Checking

```text
次のKBページまたは草稿に含まれる主張を、検証対象として分解してください。

目的:
- 出典が必要な主張を抽出する。
- 断定しすぎている箇所を特定する。
- 数値・比較・臨床性能・安全性・規制に関する主張を優先的にチェックする。

出力形式:

| Claim | Type | Why source is needed | Current source | Verification action | Suggested wording |
|---|---|---|---|---|---|

Typeは以下から選ぶ:
- numeric
- clinical-performance
- device-spec
- safety
- regulatory
- methodological
- general-background
- interpretation
```
