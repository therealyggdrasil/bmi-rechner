weight = 0
size = 0
bmi = 0

print('Wir unterscheiden nicht zwischen männlich und weiblich.')
print('Ärzte sind wir auch nicht und daher ist diese Auswertung nur eine ungefähre Angabe ohne Gewähr!')
print()
print('Bevor wir etwas berechnen können, brauchen wir zwei Angaben von dir...')

while weight <=0:
    weight = float(input('Gib bitte dein Gewicht in -kg- (z.B. 75) ein: '))
    print(f'Dein eingegebenes Gewicht beträt: {weight}')
while size <=0:
    size = float(input('Gib bitte deine Körpergröße in -m- (z.B. 1.82)ein: '))
    print(f'Deine angegebene Körpergröße beträgt: {size}')

bmi = weight / (size * size)
print(f'Dein BMI beträgt: ', round(bmi, 2))

if bmi > 40:
    print(f'Leider fällst du in die Kategorie "Adipositas III (Behandlungsbedürftig)".')
elif 35 <= bmi < 40:
    print(f'Deinen Angaben nach fällst du in die Kategorie "Adipositas II (Behandlungsbedürftig).')
elif 30 <= bmi < 35:
    print (f'Du bist deinen Angaben nach in der Kategorie "Adipositas I (Behandlungsbedürftig)".')
elif 25 <= bmi < 30:
    print (f'Deine Kategorie ist "Präadipositas (Übergewichtig)".')
elif 18.5 <= bmi <25:
    print (f'Du hast "Normalgewicht".')
elif 17 <= bmi < 18.5:
    print(f'Du hast leichtes Untergewicht.')
elif 16 <= bmi < 17:
    print(f'Du hast mäßiges Untergewicht.')
elif 13 <= bmi < 16:
    print(f'Du hast hochgradiges Untergewicht "Grad I (hochgradiges Untergewicht)".')
    print(f'Liegt dein BMI unter "16" ist eine stationäre Aufnahme empfehlenswert- Es kann zu organischen Komplikationen kommen!')
elif 12 <= bmi < 13:
    print(f'Du hast hochgradiges Untergewicht "Grad II (hochgradiges Untergewicht)".')
    print(f'Liegt dein BMI unter "16" ist eine stationäre Aufnahme empfehlenswert- Es kann zu organischen Komplikationen kommen!')
elif 10 <= bmi < 12:
    print(f'Du schwebst in akuter Lebensgefahr!!!')
elif bmi < 10:
    print(f'Solltest du in diese Kategorie fallen, wirst du deine Daten kaum selbst eingegeben haben "Kaum ein Überleben möglich".')
