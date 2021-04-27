import socket
#Константы
PORT = 9090         # Не требует спец прав для использования
HOST = socket.gethostbyname(socket.gethostname())   # Если роутер наш поменяется, то мы находим автоматически наш IP

"""
    get_ID 
    Аргументы:
    n - флаг для функционала. Принимает 0 или 1. 1 - Получение нового ID, 0 - получение ID;
    name - имя пользователя;
    hash_password - хэш пароль;

    Получает от сервера новый ID пользователя , а также (для зарегестрированных) просто ID пользователя
"""
def get_ID(n, name, hash_password):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      # Установка с сервером контакта
  sock.connect((HOST, PORT))

  if (n == "1"):
    # Нужно получить от сервера новый ID ,которого еще не существует
    #TODO написать функцию для получение нового ID
    pass

  elif (n == "0"):
    try:
      message = n + "*" + name + "*" + hash_password
      message = message.encode()
      sock.sendall(message)
    
      # Получение ответа от сервера
      amount_received = 0
      amount_expected = 7 # Длина ID
      while amount_received < amount_expected:
          data = sock.recv(16)
          amount_received += len(data)
          mess = data.decode()
          print(f'Получено: {data.decode()}')
    finally:
      sock.close()



"""
    notifications
    Аргументы:
    ID - ID пользователя

    Выдает список сообщений от других клиентов (направленных к данному пользователю)
"""
def notifications(ID):
  # Сервер получит такое сообещение и выдаст весь лист сообщений для данного пользователя

  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      # Установка с сервером контакта
  sock.connect((HOST, PORT))
  try:
    message = ID + "*" + notifications
    message = message.encode() 
    sock.send(message)
    
    # Придумать какое условие должно прерывать цикл приема сообещний от клиента
    while (True):
      data = sock.recv(1024)
      mess = data.decode()
      print(mess)
      if (data == "0"):   # Уведомлений от других пользователей к данному клиенту нет!
        break
      if (data == "stop"):
        break
  finally:
    sock.close()


"""
    post_anketa_to_server
    Аргументы:
    name - имя пользователя;
    hash_password - хэш пароль;

    Отправляет анкету нового пользователя на сервер
"""
def post_anketa_to_server(name, hash_password):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      # Установка с сервером контакта
  sock.connect((HOST, PORT))

  try:
    message = name + "*" + hash_password
    mess = message.encode()
    sock.send(mess)
    return True
  finally:
    sock.close()
    print("Готово")



"""
    writing
    Аргументы:
    -

   Создает контакт с дугим пользоваетелем в виде переписки. 
   #TODO Если перписка сущесвтует, то берем ее и выводим все клиенту
    
"""
def writing():
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)      # Установка с сервером контакта
  sock.connect((HOST, PORT))

  print("Введите ID друга:  ", end='')
  id_friend = input()
  try:
    message = id + "*" + mess + "*" + id_friend
    message = message.encode()
    sock.sendall(message)

    # Придумать какое условие должно прерывать цикл приема сообещний от клиента
    while (True):
      data = sock.recv(1024)
      mess = data.decode()
      print(mess)
      #if (data == "0"):   # Уведомлений от других пользователей к данному клиенту нет!
       # break
     # if (data == "stop"):
       # break
  finally:
    sock.close()


"""
"""
def print_list_of_friends():
  pass

