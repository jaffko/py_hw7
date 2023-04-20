def count_vows(obj):
    result = []
    for item in obj:
        count = 0
        for i in item:
            if i in vowels:
                count += 1
        result.append(count)
    return result
   

poem = input('Введите стих: ')
phrases = poem.split()
vowels = 'аеёиоуэюя'
counted_vows = count_vows(phrases)
if min(counted_vows) == max(counted_vows):
    print('Парам пам-пам')
else:
    print('Пам парам')

