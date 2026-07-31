# w1,w2,w3 = [2,3,4,4,1,1,1],[1,2,4,3,3],[1,1,1,1,2,2]
combinations = [(4,),(3,1),(2,2),(2,1,1),(1,1,1,1),(3,),(2,1),(1,1,1),(2,),(1,1),(1,)]

def count_subsets(watched, needed):
    return min(watched.count(element) // needed.count(element) for element in needed)

amount, watched = int(input()), list(map(int, input().split()))

steps = 0
for needed in combinations:
        local = count_subsets(watched, needed)
        steps += local

        for j in range(local):
            for i in needed:
                watched.remove(int(i))

print(steps)