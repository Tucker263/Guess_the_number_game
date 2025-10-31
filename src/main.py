import random
from typing import Tuple

# デバック用フラグ
DEBUG_MODE = True


def get_int(prompt: str) -> int:
    # 整数入力を安全に取得
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("不正な入力です。整数を入力してください。")


def get_range() -> Tuple[int, int]:
    # 有効な整数範囲 (n, m) を取得
    while True:
        n = get_int("整数 n を入力してください: ")
        m = get_int("整数 m を入力してください: ")
        if n < m:
            return n, m
        print("n < m になるように入力してください。")


def play_number_guessing_game(n: int, m: int, debug: bool = False) -> None:
    # 指定範囲で数あてゲームをプレイ
    target = random.randint(n, m)
    if debug:
        print(f"(デバッグ) 正解は: {target}")

    attempts = 0
    while True:
        guess = get_int("数字を当ててください: ")
        attempts += 1
        if guess == target:
            print(f"{attempts} 回目で当たりました！ゲームを終了します。")
            print("-" * 20)
            break
        hint = "小さいです。" if guess < target else "大きいです。"
        print(f"{hint} もう一度挑戦してください。")


def main() -> None:
    # ゲーム全体のエントリーポイント
    print("------------")
    print("数あてゲーム")
    print("整数 n から m の範囲でランダムな数字を生成します。その範囲内で当ててください。")

    n, m = get_range()
    play_number_guessing_game(n, m, debug=DEBUG_MODE)


if __name__ == "__main__":
    main()
