from functions.get_file_content import get_file_content

# Büyük dosya: içeriği print etme, sadece truncate kontrolü
result = get_file_content("calculator", "lorem.txt")
print(f"lorem.txt length: {len(result)}")
print(f"lorem.txt truncated: {'truncated' in result}")

# Küçük / hata case'leri: çıktıyı print et
print(get_file_content("calculator", "main.py"))
print(get_file_content("calculator", "pkg/calculator.py"))
print(get_file_content("calculator", "/bin/cat"))  # outside → Error
print(get_file_content("calculator", "pkg/does_not_exist.py"))  # Error
