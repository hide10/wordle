# wordleのヘルパー

## 使い方

* 起動すると最初に"correct and wrong:"の入力待ちになる
  * 位置確定済みの文字は大文字、位置未確定の文字は小文字、それ以外はアルファベット以外(空白やドット)を入力
* 続いて"not in any spot:"の入力待ちになるので使用されない文字列を入力する
* 次回の推奨入力単語が最大3単語まで表示される
* 再度 "correct and wrong:"の入力待ちになる。終了したい場合は"correct and wrong:"、"not in any spot:"ともに入力せずにEnterを押す

## 使用例

wordleの一番最初の入力は ALERT がお薦めです。

```sh
> python wordle_helper.py"
correct and wrong: a Er
not in any spot: lt
Possible words: SHEAR,SMEAR,SPEAR,
correct and wrong:   EAr
not in any spot: ltsh
Possible words: CREAK,CREAM,
correct and wrong:  REAK
not in any spot: ltshc
Possible words: BREAK,
correct and wrong:
not in any spot: 
> 
```

## 当てられない単語

".ATCH"は7単語あるので、このヘルパーでは当たらないことがあります。
".AUNT"も6単語あるので、このヘルパーでは当たらないことがあります。
".I.ER"も24単語あるので、このヘルパーでは当たらないことがあります。

以上
