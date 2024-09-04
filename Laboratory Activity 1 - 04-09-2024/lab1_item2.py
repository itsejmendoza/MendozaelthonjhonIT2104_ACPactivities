char1, char2 = input("Enter two space-separated characters: ").split()

greater_char = max(char1, char2)

print("-" * 30)
print(f"The character with greater value is: {greater_char}")
print("-" * 30)
print("Showing ASCII Values:")
print(f"{char1} : {ord(char1)}")
print(f"{char2} : {ord(char2)}")