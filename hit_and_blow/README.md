# Hit and Blow Solver

## 概要
このプログラムは「ヒット・アンド・ブロー」のソルバーです。
ユーザーが指定した桁数の数字の中から、対戦相手からのフィードバック（ヒットとブローの数）に基づいて正解の数字を絞り込み、最適な推測を自動で導出します。

<br>

## 特徴
- **対話型インターフェース**  
  ユーザーに対して、使用する桁数の入力、各推測後のヒットとブローの数の入力を求めます。
- **候補の絞り込み**  
  初期状態で全ての候補を生成し、各回のフォードバックに応じて候補をフィルタリングしていきます。
- **高速計算**  
  評価関数 `evaluate_guess` に対してキャッシュ機構（`lru_cache`）を利用し、計算の高速化を図っています。

<br>

## 使用方法
1. **準備**  
   Python 3.x がインストールされていることを確認してください。

<details><summary>Python 3.xインストール確認方法</summary>

```
1. ターミナルまたはコマンドプロンプト(cmd)を開く

2. バージョン確認コマンドを実行する

   - Linux/Macの場合:
     ```bash
     python3 --version
     ```
   - Windowsの場合:
     ```bash
     python --version
     ```
     または
     ```bash
     py --version
     ```

3. 出力結果の確認

   - コマンド実行後、例えば以下のような出力が得られます:
     ```
     Python 3.11.9
     ```
   - このように「Python 3.x.x」と表示されれば、Python 3.x がインストールされています。
```
</details>

2. **プログラムの実行**  
   ターミナルまたはコマンドプロンプトから以下のコマンドで実行します。

   ```bash
   python hit_and_blow_solver.py
   ```

3. **使用方法**  
   - プログラム開始時に「何桁の数字を使いますか？」と表示されるので、使用する桁数（例: 3）を入力します。  
   - 自動的に初期の推測が表示されるので、表示された値をゲーム側で入力してください。
   - 続いて「ヒットの数」と「ブローの数」の入力を求められます。それぞれ必ず入力してください(*1)  
   - ユーザーのフィードバックに応じ、候補が絞られていき、最終的に正解の数字が導き出されると、ゲームクリアのメッセージが表示されます。  
   - ゲーム終了後、再度プレイするかどうかの確認が行われます。(続行するならyと、そうでないならnと入力)
     
    ※1　両方入力しないと無効判定になります。

<br>

## コードの構成
- **`evaluate_guess(target, guess)`**  
  対象の数字（target）と推測（guess）を比較し、位置も一致する「ヒット」の数と、数字自体は含まれるが位置が異なる「ブロー」の数を計算します。  
  ※ キャッシュを利用して計算結果を保存するため、同じ比較処理が繰り返される場合でも高速に動作します。

- **`filter_candidates(candidates, guess, hits, blows)`**  
  現在の候補リストから、前回の推測結果（ヒットとブローの数）と一致するものだけを抽出します。

- **`select_best_guess(candidates)`**  
  残っている候補の中から、各推測に対する worst-case（最悪の場合の候補数）を最小化する推測を選定します。  
  ※ 候補数が多い場合のみ採用。

- **`hit_and_blow_solver()`**  
  プログラムのメインループを担当し、ユーザーからの入力受付、候補の生成および絞り込み、推測の提示、ゲーム終了の判定など全体の流れを管理します。

## エラー処理
- ユーザーが無効な値（数値でない値や、指定された桁数の範囲外の値）を入力した場合、適切なエラーメッセージを表示し、再入力を促します。
- ヒットとブローの合計が使用桁数を超えたり、負の値が入力された場合にもエラー処理が行われます。

<br>

## 参考文献
- [はじめに — Python早見帳](https://chokkan.github.io/python/index.html)
- [Hit and Blowで勝てそうなアルゴリズムを書いてみる](https://qiita.com/Azukiii/items/2c154deed025503979cd)
- [Python｜ヌメロンの作り方を解説！【サンプルコード有】](https://coding-with-me.com/python-numeron/)
- [Python の filter() 関数](https://python.keicode.com/refs/filter-function.php)
- [lru_cacheを理解する（Python） - Yuta NakataのBlog](https://www.yuta-nakata.net/entry/2023/11/18/141029)

<br>

## ライセンス
このプログラムはオープンソースとして公開されています。
使用・改変・再配布はライセンス条件に従って行ってください。

---
