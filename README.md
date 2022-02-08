# wordleのヘルパー

## 使い方

* 起動すると最初に"correct and wrong:"の入力待ちになる
  * 位置確定済みの文字は大文字、位置未確定の文字は小文字、それ以外はアルファベット以外を入力
* 続いて"not in any spot:"の入力待ちになる
  * 使用されない文字列を入力する
* 次回の推奨入力単語が表示される
* 再度 "correct and wrong:"の入力待ちになる。終了したい場合は"correct and wrong:"、"not in any spot:"ともに入力せずにEnterを押す

## 使用例

wordleの一番最初の入力は ALERT がお薦めです。

```sh
> python wordle_helper.py
correct and wrong: ....T
not in any spot: aler
Possible words: BIGOT

correct and wrong: ..GoT
not in any spot: alerbi
Possible words: OUGHT

correct and wrong:
not in any spot: 
```
