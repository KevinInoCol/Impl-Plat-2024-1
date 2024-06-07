import requests #pip install requests

def main():
    file_web = open('jonathan.html', 'w+', encoding='utf-8')
    response = requests.get('https://lorem2.com/')
    consulta = response.text
    file_web.write(consulta)
    file_web.close()

if __name__ == '__main__':
    main()