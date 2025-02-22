# (C) 2025 A.Voß, a.voss@fh-aachen.de, info@codebasedlearning.dev

""" Task 'Big Pea' """


def counter_add(counter: dict, item):
    counter[item] = counter.get(item, 0) + 1

def counter_subtract(counter: dict, item):
    if item in counter:
        counter[item] -= 1
        if counter[item] <= 0:
            del counter[item]

def counter_most_common(counter: dict):
    # return max(counter.items(), key=lambda x: x[1])[0]        # short version using lambdas

    most_common_key = None
    max_count = float('-inf')
    for key in counter:
        if counter[key] > max_count:
            most_common_key = key
            max_count = counter[key]
    return most_common_key

def count_banana():
    banana = {}
    for c in "banana":
        counter_add(banana, c)
    print(f" 1| {banana=}")                                     # {'b': 1, 'a': 3, 'n': 2}

    counter_subtract(banana, 'b')
    print(f" 2| {banana=}")                                     # {'a': 3, 'n': 2}

    print(f" 3| {counter_most_common(banana)=}")                # 'a'

if __name__ == "__main__":
    count_banana()
