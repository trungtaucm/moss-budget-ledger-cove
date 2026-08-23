"""moss-budget-ledger-cove tool for profile 0015.
PROJECT = "moss-budget-ledger-cove"
PROFILE = "0015"

def run(value):
    return {"project": PROJECT, "profile": PROFILE, "value": value}

if __name__ == "__main__":
    print(run("ready"))
