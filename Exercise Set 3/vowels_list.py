input_string = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_list = [char for char in input_string if char in vowels]
print(vowel_list)
