import urllib3

def main():
    file_web = open('elias.html', 'w+')
    http = urllib3.PoolManager()
    response = http.request('GET', 'https://lorem2.com/')
    consulta = response.data.decode('utf-8')
    file_web.write(consulta)
    file_web.close()


if __name__ == '__main__':
    main()