from logic.update_towns import townTurn
from logic.utill import checkInList
from logic.load_json import towns
import json

print()
print()
print(r'type "update" and press enter to update the towns')
print(r'type "exit" to cancel')
userinput = checkInList(["update", "exit"], "> ")

if userinput == "update":
    for town in towns:
        townTurn(town)

    with open("towns/towns.json", "w") as outfile:
        json.dump(towns, outfile, indent=4, sort_keys=True)

if userinput == "exit":
    exit()
