#!/usr/bin/env python3
icecream = ["flavors", "salty"]
icecream.append(99)
print(icecream)
name = input("What is your handle?").strip()
print(f"{icecream[-1]} flavors, and {name} chooses to be {icecream[-2]}.")
