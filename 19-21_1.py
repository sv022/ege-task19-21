from functools import lru_cache

def moves(h):
    return h + 1, h * 2

@lru_cache(None)
def f(h):
    if h >= 75:
        return 'СР'
    elif any(f(m) == 'СР' for m in moves(h)):
        return 'П1'
    elif all(f(m) == 'П1' for m in moves(h)):
        return 'В1'
    elif any(f(m) == 'В1' for m in moves(h)):
        return 'П2'
    elif all(f(m) == 'П1' or f(m) == 'П2' for m in moves(h)):
        return 'В2'

for s in range(1, 75):
    print(f'{s}: {f(s)}')
