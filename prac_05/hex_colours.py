"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_COLOUR = {"Apricot": "#fbceb1", "Aquamarine": "#7fffd4",
                  "Azure1": "#f0ffff", "Beige": "#f5f5dc",
                  "DarkSalmon": "#e9967a", "DarkSeaGreen": "#8fbc8f",
                  "DarkSlateBlue": "#483d8b", "DarkSlateGray": "#2f4f4f",
                  "DarkSlateGrey": "#2f4f4f", "DarkTurquoise": "#00ced1"}

colour_code = input("Enter a colour: ")
while colour_code != "":  # while colour_code is not empty
    if colour_code in CODE_TO_COLOUR:
        print(colour_code, "is", CODE_TO_COLOUR[colour_code])
    else:
        print("Invalid colour name")
    colour_code = input("Enter a colour: ")
