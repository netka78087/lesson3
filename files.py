with open('referat.txt', 'r', encoding='utf-8') as ref:
    content = ref.read()
    print(len(content))
    print(len(content.split(' ')))
with open('referat2.txt', 'w', encoding='utf-8') as ref:
    ref.write(content.replace('.', '!'))