morse = {'а': '.- ', 'б': '-... ','в': '.-- ', 'г': '--. ', 'д': '-.. ','е': '. ','ж': '...- ',
              'з': '--.. ', 'и': '.. ', 'й': '.--- ', 'к': '-.- ', 'л': '.-.. ', 'м': '-- ', 'н': '-. ',
              'о': '--- ', 'п': '.--. ', 'р': '.-. ', 'с': '... ', 'т': '- ', 'у': '..- ', 'ф': '..-. ',
              'х': '.... ', 'ц': '-.-. ', 'ч': '---. ', 'ш': '---- ', 'щ': '--.- ' , 'ъ': '.--.-. ',
              'ь': '-..- ', 'э': '..-.. ', 'ю': '..-- ' , 'я': '.-.- ', ' ': '\n'}
text = input().lower()
for i in text:
    for key, value in morse.items():
        if i==key:
            print(value, end= ' ')