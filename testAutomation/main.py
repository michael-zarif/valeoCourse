import calculations, strings, dictionaries

dict_1 = {
    'key_1': 5,
    'key_2': 10
}

dict_2 = {
    'key_1': 2,
    'key_2': 4,
    'key_3': 6
}

if __name__ == '__main__':
    print(calculations.calculate_sum(int(input("Enter a number to calculate its sum: "))))
    print(f'even sum: {calculations.calculate_even_odd_sum(5)[0]}, while odd sum: {calculations.calculate_even_odd_sum(5)[1]}')
    print(strings.reverse_text('Hello!'))
    print(strings.text_to_list('John,Doe,30'))
    print(strings.upper('hellO!'))
    print(strings.lower('HELLo!'))
    print(dictionaries.sum_dict(dict_1, dict_2))