from itertools import permutations
from functools import lru_cache
from collections import Counter

@lru_cache(maxsize=None)
def evaluate_guess(target, guess):
    hits = sum(1 for t, g in zip(target, guess) if t == g)
    blows = sum(min(target.count(g), guess.count(g)) for g in set(guess)) - hits
    return hits, blows

def filter_candidates(candidates, guess, hits, blows):
    return [c for c in candidates if evaluate_guess(c, guess) == (hits, blows)]

def select_best_guess(candidates):
    best_guess = None
    min_worst_case = float('inf')
    for guess in candidates:
        outcome_counts = Counter(evaluate_guess(candidate, guess) for candidate in candidates)
        worst_case = max(outcome_counts.values())
        if worst_case < min_worst_case:
            min_worst_case = worst_case
            best_guess = guess
    return best_guess

def hit_and_blow_solver():
    digits = '0123456789'
    while True:
        try:
            length = int(input("何桁の数字を使いますか？: "))
        except ValueError:
            print("有効な数字を入力してください。")
            continue
        if length <= 0 or length > len(digits):
            print(f"桁数は1以上かつ最大で {len(digits)} 桁までです。")
            continue
        candidates = [''.join(p) for p in permutations(digits, length)]
        previous_guesses = []
        while True:
            if previous_guesses:
                guess = candidates[0] if len(candidates) > 200 else select_best_guess(candidates)
            else:
                guess = candidates[0]
            print(f"推測: {guess}")
            try:
                hits = int(input("ヒットの数を入力してください: "))
                blows = int(input("ブローの数を入力してください: "))
            except ValueError:
                print("有効な数字を入力してください。")
                continue
            if hits + blows > length or hits < 0 or blows < 0:
                print(f"ヒットとブローの合計は {length} 以下で、負の値は無効です。")
                continue
            previous_guesses.append((guess, hits, blows))
            candidates = filter_candidates(candidates, guess, hits, blows)
            print(f"現在の候補数: {len(candidates)}")
            if len(candidates) <= 30:
                print(f"候補: {candidates}")
            if hits == length:
                print(f"おめでとうございます！正解は {guess} です。")
                break
        again = input("もう一度プレイしますか？ (y/n): ")
        if again.lower() != 'y':
            print("ゲームを終了します。ありがとうございました！")
            break

if __name__ == "__main__":
    hit_and_blow_solver()
