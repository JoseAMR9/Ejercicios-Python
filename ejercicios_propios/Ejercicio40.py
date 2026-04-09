total = float(input("What was the total: "))

if total > 200:
    print("You have a 10 percent discount ")
    print(f"Final total: {total - total * 0.10}")
elif total > 100:
    print("You have a 5 percent discount ")
    print(f"Final total: {total - total * 0.05}")
else:
    print("You dont have a discount")
    print(f"Final total: {total}")