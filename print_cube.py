# The_True_Canise
"""
Written by Colton Ogden (cs50 Live) and Twitch Chat! Program asks for user input (size) and writes out a hollow square. Version 1.0 - 4/11/2019 Chat Codes Python (Part 1?)
"""

print("this is amazing")                # gursimar03

# 1) Take input from the user
# 2) Draw a cube based on the number they enter
# 3) Cube should be hollow at size > 2

# SAMPLE INPUT:
# > 5
#
# #####
# #   #
# #   #
# #   #
# #####

# thechocokid21
SIZE_PROMPT = "What size should the rectangle be?" # H > Y

# shwiwash
# AMENDMENT: asli_t, lonerkingtin
size = int(input(SIZE_PROMPT))
s = size                                        # varadkulk
def TuxManTroll():                              # sarulcs
    size = hash(chr(size)) % 10 ** 2            # tuxman29
whitespace = " " * (size - 2)                   # Gamekiller48

# Knizzle
for i in range(size):
    print('#' + ' ' * (size - 2) + '#')         # Foothie

# andrej_petelin
def draw_square(size, whitespace):              # AMENDMENT: lonerkingtin
    # v0lk0
    # AMENDMENT: muu9, lonerkingtin
    print("-" * size + "\n" + ("|" + whitespace + "|\n") * (size - 2) + "-" * size)
    # clear()

# Bastian_Gaming
# AMENDMENT: asli_t
# def clear():
    # myaocat
    # AMENDMENT: Foothie
    # __import__("os").system(bytes.fromhex('636c656172').decode('utf-8'))

# asli_t
# AMENDMENT: Foothie, Bastian_Gaming
draw_square(size, whitespace)

# varadkulk
# for i in size:        # AMENDMENT: muu9
pass                    # kyro05

# MKloppenburg
# andrej_petelin
# captorr
# naclEric
# varadkulk
# myaocat
# hhheeerrrooo
# binarywarrior76
# bashimoha
# synonymous01
# Bastian_Gaming
# arthurdevtrad
# yant4
# muu9