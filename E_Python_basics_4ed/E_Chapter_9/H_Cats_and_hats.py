"""Challenge: Cats With Hats 9.9"""

cats = {}

for i in range(1, 101):
    cats[f'cat{i}'] = ''
count = 1
while count < 101:
    for i in range(1, 101):
        if i % count == 0:
            if cats[f'cat{i}'] == 'hat':
                cats[f'cat{i}'] = ''
            else:
                cats[f'cat{i}'] = 'hat'
    count += 1
for cat, hat in cats.items():
    if cats[f'{cat}'] == 'hat':
        print(cat)
    else:
        continue

