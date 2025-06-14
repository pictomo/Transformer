#!/usr/bin/env python3

# https://qiita.com/ytaki0801/items/b45696aa0c3f8bd259db

# 状態遷移定義：(状態, 記号) -> (状態, 記号, ヘッド移動)
delta = {
    0: {0: (1, 1, 1), 1: (0, 2, -1), 2: (0, 1, -1)},
    1: {0: (0, 2, -1), 1: (1, 2, 1), 2: (0, 0, 1)},
}

# 初期状態
state = 0
# 初期テープ
tape = [0] * 6
# ヘッダの初期位置
head = 2

print(tape)
for _ in range(20):
    t = delta[state][tape[head]]
    state = t[0]
    tape[head] = t[1]
    head += t[2]
    print(tape)
