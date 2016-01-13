# Input
nric = "S0000001"

# Process
WEIGHTS = [2, 7, 6, 5, 4, 3, 2]
DIGITS_FOR_S_T = ['J', 'Z', 'I', 'H', 'G', 'F', 'E', 'D', 'C', 'B', 'A']
DIGITS_FOR_F_G = ['X', 'W', 'U', 'T', 'R', 'Q', 'P', 'N', 'M', 'L', 'K']
OFFSET_FOR_T_G = 4

prefix = str()
product = int()
index = int()
check_digit = str()

prefix = nric[0]
product = 0
for index in range(len(WEIGHTS)):
	product += WEIGHTS[index] * int(nric[index + 1])
if prefix == 'T' or prefix == 'G':
	product += OFFSET_FOR_T_G
product %= 11
if prefix == 'S' or prefix == 'T':
	check_digit = DIGITS_FOR_S_T[product]
elif prefix == 'F' or prefix == 'G':
	check_digit = DIGITS_FOR_F_G[product]
else:
	check_digit = None

# Output
print(check_digit)
