import pytesseract

text = str(((pytesseract.image_to_string(Image.open(filename)))))

print(text)
