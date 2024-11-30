from itertools import permutations
from collections import defaultdict

def evaluate_guess(target, guess):
    hits = sum(1 for t, g in zip(target, guess) if t == g)
    blows = sum(min(target.count(g), guess.count(g)) for g in set(guess)) - hits
    return hits, blows

def filter_candidates(candidates, guess, hits, blows):
    filtered = []
    for c in candidates:
        if evaluate_guess(c, guess) == (hits, blows):
            filtered.append(c)
    return filtered

def select_best_guess(candidates):
    best_guess = None
    min_worst_case = float('inf')

    frequencies = defaultdict(int)
    for c in candidates:
        for perm in permutations(c):
            frequencies[''.join(perm)] += 1

    for guess in candidates:
        worst_case_size = max(frequencies[guess] for guess in candidates)
        if worst_case_size < min_worst_case:
            min_worst_case = worst_case_size
            best_guess = guess

    return best_guess

def hit_and_blow_solver():
    digits = '0123456789'
    length = 4
    candidates = [''.join(p) for p in permutations(digits, length)]

    previous_guesses = []

    while True:
        if previous_guesses:
            guess = select_best_guess(candidates)
        else:
            guess = candidates[0]

        print(f"推測: {guess}")
        hits = int(input("ヒットの数を入力してください: "))
        blows = int(input("ブローの数を入力してください: "))

        if hits + blows > length or hits < 0 or blows < 0:
            print("ヒットとブローの合計は4以下であり、負の値は無効です。")
            continue

        previous_guesses.append((guess, hits, blows))
        candidates = filter_candidates(candidates, guess, hits, blows)

        print(f"現在の候補数: {len(candidates)}")
        print(f"候補: {candidates}")

        if hits == length:
            print(f"おめでとうございます！正解の数は {guess} です。")
            break

if __name__ == "__main__":
    hit_and_blow_solver()

