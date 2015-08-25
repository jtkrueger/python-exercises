def sillycase(stringy):
    string_half = round(len(stringy)/2)
    print(stringy[:string_half].lower() + stringy[string_half:].upper())

sillycase("Treehouse")
