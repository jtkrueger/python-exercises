string = "Jordan krueger"

def stringcases(string):
    upper = string.upper()
    lower = string.lower()
    title = string.title()

    reverse = list(string)
    reverse = reverse[::-1]
    reverse = ''.join(reverse)

    print(upper)
    print(lower)
    print(title)
    print(reverse)

    return (upper, lower, title, reverse)


stringcases(string)
