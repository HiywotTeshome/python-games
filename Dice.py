import random

#print("\u25cf \u250c \u2500 \u2510 \u2502 \u2514 \u2518")
#● ┌ ─ ┐ │ └ ┘
dies = {
    1 : ("┌────────────┐",
         "│            │",
         "│            │",
         "│     ●      │",
         "│            │",
         "└────────────┘"),
    2 : ("┌────────────┐",
         "│   ●        │",
         "│            │",
         "│            │",
         "│       ●    │",
         "└────────────┘"),
    3 : ("┌────────────┐",
         "│ ●          │",
         "│            │",
         "│     ●      │",
         "│       ●    │",
         "└────────────┘"),
    4 : ("┌────────────┐",
         "│ ●       ●  │",
         "│            │",
         "│            │",
         "│ ●       ●  │",
         "└────────────┘"),
    5 : ("┌────────────┐",
         "│ ●       ●  │",
         "│            │",
         "│     ●      │",
         "│ ●       ●  │",
         "└────────────┘"),
    6 : ("┌────────────┐",
         "│ ●       ●  │",
         "│            │",
         "│ ●       ●  │",
         "│ ●       ●  │",
         "└────────────┘")}

def main():
    dice = []
    total = 0
    num_of_dice = int(input("How many dice?: "))

    for die in range(num_of_dice):
        dice.append(random.randint(1,6))

    for line in range(6):
        for die in dice:
            print(dies.get(die)[line], end = " ")
        print()

    for die in dice:
        total += die
    print(f"total: {total}")


if __name__ == "__main__":
    main()