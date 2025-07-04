n = int(input("Enter a number: "))
binary = bin(n)[2:]
print("Binary:", binary)

# Find longest group of 1's
longest = max(len(x) for x in binary.split('0'))
print("Longest consecutive 1's:", longest)
