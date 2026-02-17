

original = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k","l", "m","n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

new = ["@", "8", "(", "|)", "3", "#", "6", "[-]", "|", "_|", "|<","1", "[]\/[]", "[]\[]", "0", "|D", "(,)", "|Z", "$", "']['", "|_|", "\/", "\/\/", "}{", "`/", "2"]


string = input()
new_string = ""

for s in string.lower():
    
    if s not in original: 
        new_string += s
    else: 
        index = original.index(s)
        new_string += new[index]
    
print(new_string)
    
print("@11 `/0|_||Z 8@$3 @|Z3 8310[]\[]6 ']['0 |_|$."=="@11 `/0|_||Z 8@$3 @|Z3 8310[]\[]6 ']['0 |_|$.")