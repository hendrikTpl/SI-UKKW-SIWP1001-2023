def reverseWords(s: str) -> str:
    # Split the string into individual words
    words = s.split()
    
    # Reverse each word and join them back together
    reversed_words = [word[::-1] for word in words]
    
    return ' '.join(reversed_words)

s = "belajar Algoritma dan Pemrograman Dasar"
print(reverseWords(s))  # Output: "s'teL ekat edoCteeL tsetnoc"

s2 = "Program studi Sistem Informasi UKRIDA"
print(reverseWords(s2))  # Output: "doG gniD"
