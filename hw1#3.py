def urutkan_dan_pasangkan(angka):
    angka_terurut = sorted(angka)
    angka_dipasangkan = []

    for i in range(0, len(angka_terurut), 2):
        if i + 1 < len(angka_terurut):
            angka_dipasangkan.append((angka_terurut[i], angka_terurut[i + 1]))
        else:
            angka_dipasangkan.append(angka_terurut[i])
            
    return angka_dipasangkan

# Uji
angka = [4, 2, 7, 3, 1, 5, 8]
print(urutkan_dan_pasangkan(angka))
