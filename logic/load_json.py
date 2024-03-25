import json

try:
    with open("data/policies.json") as policies:
        policies = json.load(policies)

    print("policies.json loading done")
except FileNotFoundError as e:
    print(e)
    input("> ")
    exit()

try:
    with open("data/conflicts.json") as conflicts:
        conflicts = json.load(conflicts)

    print("conflicts.json loading done")
except FileNotFoundError as e:
    print(e)
    input("> ")
    exit()

try:
    with open("data/tax policies.json") as taxPolicies:
        taxPolicies = json.load(taxPolicies)

    print("tax policies.json loading done")
except FileNotFoundError as e:
    print(e)
    input("> ")
    exit()


try:
    with open("towns/towns.json") as towns:
        towns = json.load(towns)

    print("towns.json loading done")
except FileNotFoundError as e:
    print(e)
    input("> ")
    exit()
