datas = {"a": 10, "b": 25, "c": 8, "d": 47, "e": 3}

max_key = min_key = "a"

for key, value in datas.items():
    if value > datas[max_key]:
        max_key = key
    if value < datas[min_key]:
        min_key = key

print(f"Mayor: {max_key} → {datas[max_key]}")
print(f"Menor: {min_key} → {datas[min_key]}")