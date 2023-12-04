COLOUR_CODES = {"xanadu": "#738678", "yellow Orange": "#ffae42", "yellow Pantone": "#fedf00",
                "yellow1": "#ffff00", "yellow2": "#eee00", "yellow3": "#cdcd00",
                "yellow4": "8b8b00", "yellowGreen": "#9acd32", "zaffre": "#0014a8",
                "zomp": "#39a78e"}

colour_name = input("Enter the colour name: ").lower()
while colour_name != "":
    colour_code = COLOUR_CODES.get(colour_name.lower())
    if colour_code in COLOUR_CODES.values():
        print(f"The codes for {colour_name} is {colour_code}")
    else:
        print("Error colour name")
    colour_name = input("Enter the colour name: ").lower()
