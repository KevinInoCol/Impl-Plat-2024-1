def main():
    web = open('jonathan.html', 'r', encoding='utf-8') #Aqui leo jonathan.html
    Inicio = '<title>'
    Final = '</title>'
    #Voy a leer linea por linea el HTML
    for linea_html in web.readlines():
        #Voy a obtener las lineas que empiecen en <li>
        if Inicio in linea_html:
            ini = linea_html.find(Inicio) #Cuando encuentra el <li> lo guarda en "ini"
            ini = ini + len(Inicio)
            fin = linea_html.find(Final)
            print(linea_html[ini:fin])

if __name__ == '__main__':
    main()