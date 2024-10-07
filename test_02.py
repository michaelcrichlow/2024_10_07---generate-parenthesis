# NOTE: This is my introduction to Depth First Search (dfs) and backtracking
# Here to learn. Let's go.

# POINT TO UNDERSTAND 1. You can only add a closing parentheses if the count of closing paretheses is less
# than the count of open parentheses.

# POINT TO UNDERSTAND 2. You can add as many open parentheses as you want as long as it is less than 'n'.

# POINT TO UNDERSTAND 3. This kind of feels magic. Like, you just say what you want to happen (if left < n) and
# (if right < left) do this and then you get all the answers. I don't quite understand how
# that works yet, but I'll keep looking at it. I'll get there.

# Apparently, this is more of a backtracking solution than an introduction to depth first search,
# but I'll take it all the same. I'm learning. >_<

def generate_parenthesis(n: int) -> list[str]:
    def dfs(left, right, s):
        # if len(s) == n * 2: (this works too)
        if left == right == n:
            res.append(s)
            return

        if left < n:
            dfs(left + 1, right, s + "(")

        if right < left:
            dfs(left, right + 1, s + ")")

    res: list[str] = []
    dfs(0, 0, "")
    return res


def main() -> None:
    print(generate_parenthesis(4))


if __name__ == '__main__':
    main()
