import easyocr

reader = easyocr.Reader(['en']) # specify the language  
result = reader.readtext('Images/GIANT0.jpg')

for (bbox, text, prob) in result:
    print(f'Text: {text}, Probability: {prob}')