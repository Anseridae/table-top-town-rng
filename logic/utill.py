def checkInList(validationList: list, inputPrompt: str) -> str:
    """compare the input against the list and returns the input if it's in there, otherwise ask for input again."""
    validResult = ""
    while not validResult:
        checkedValue = input(inputPrompt)
        if checkedValue in validationList:
            validResult = checkedValue
    return validResult
