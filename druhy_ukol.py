herci = int(input('napis pocet hercu: '))
plat_za_jednoho_herce = 22392
platy = herci * plat_za_jednoho_herce
studenska_sleva = 0.65
cele_vstupne = 12
studenske_vstupne = studenska_sleva * cele_vstupne
predstaveni = 'Romeo a Julie'

novy_herci = herci + 2
platy = novy_herci * plat_za_jednoho_herce

print(f'Na predstaveni {predstaveni} je cena {cele_vstupne} eur za osobu a za studenta {studenske_vstupne} eur.')

print(f'V nasem divadle hraje {novy_herci} hercu a plat dohromady pro vsechny herce je {platy} kc.')