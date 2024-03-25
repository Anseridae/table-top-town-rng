from logic.load_json import towns, policies, taxPolicies, conflicts
import random


def townTurn(town):
    towns[town]['policies'] = random.choice(list(policies.items()))
    towns[town]['tax policies'] = random.choice(list(taxPolicies.items()))
    towns[town]['conflict'] = random.choice(list(conflicts.items()))
