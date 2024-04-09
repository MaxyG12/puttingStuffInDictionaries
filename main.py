myBeast = {"name": None, "type": None, "move": None, "hp": None, "mp": None}

print("MokeBeast")
print()

for name, value in myBeast.items():
  myBeast[name] = input(f"{name}: ").strip().title()
  
if myBeast["type"]=="Earth":
  print("\033[32m", end="")
elif myBeast["type"]=="Air":
  print("\033[37m", end="")
elif myBeast["type"]=="Fire":
  print("\033[31m", end="")
elif myBeast["type"]=="Water":
  print("\033[34m", end="")
else:
  print("\033[33m", end="")

for name, value in myBeast.items():
  print(f"{name:<15}: {value}")