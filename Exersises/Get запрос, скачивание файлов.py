from requests import get

file = get('https://stepik.org/media/attachments/course67/3.6.3/699991.txt').text
print(file)

while True:
    try:
        
        url = 'https://stepik.org/media/attachments/course67/3.6.3/' + str(file)
        file = get(url).text
        if file.startswith('Me'):
            print(file)
    except:
        print('ТАкого нет')

