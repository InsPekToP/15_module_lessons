#15main1_1
#Создание сервера

#создаем локальный сервер без помощи сторонних фрейморков
from http.server import HTTPServer,CGIHTTPRequestHandler
#HTTPServer - за счет этого класса сможем создать локальный сервер
#CGIHTTPRequestHandler - отслеживать переходы пользовотеля по разным страничкам

#этот код лучше обернуть в ф-ию(метод)
def server():

#создаем пер-ю-множество.Указываем localhost,и 2м пар-ом надо указывать порт(4 числа)
    server_data = ("localhost", 8000)
    server = HTTPServer(server_data,CGIHTTPRequestHandler)
#можно было и так передать: server = HTTPServer("localhost", 8000)

    print("Server started")
#чтобы он работал постоянно
    server.serve_forever()


#теперь можем зайти на это сервер через браузер http://localhost:8000/
#остановить сервер Ctrl+C

#если создаем index.html,то сразу подключится(важно создавать в той же папке)
#если не работает,то надо установить биб-ку python -m http.server --cgi

#и теперь лучше его вызывать
#делаем чтобы она вызывалась только из этого файла
if __name__== "__main__":
    try:
        server()
    except KeyboardInterrupt:
        print("Сервер остановлен")

# if __name__== "__main__":
#     print("Main")