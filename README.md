# wordleのヘルパー

## 使い方

* 起動すると最初に"correct and wrong:"の入力待ちになる
  * 位置確定済みの文字は大文字、位置未確定の文字は小文字、それ以外はアルファベット以外を入力
* 続いて"not in any spot:"の入力待ちになる
  * 使用されない文字列を入力する
* 可能性のある単語がリストアップされる

## 使用例

```sh
> python wordle.py
correct and wrong:
SrAd

not in any spot:
pnkmilkyzoeu

Possible words:
shard
sward
```
