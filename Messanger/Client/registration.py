import hashing as hs
import contact as con   # Все функции для взаимодействия с сервером

def log_in():
  print("Приветсвуем, это вход в аккаунт! Введите ваше имя и ваш пароль(через пробел) ")
  name, password = map(str(), input().split())

  hash_password = hashing(password)   # Хэшируем пароль для безопасности))

  ID = get_ID(name, hash_password)    # Получаем собственный ID для пользованием услугами

  # Отправляем данные о нас для входа
  flag = post_anketa_to_server(name, hash_password)
  if (flag == True):
    
    notifications()
    print(" ")
    print("=========================================================================")
    print(" ")

    while(True):

      #print("Кому хотите написать?(ID друга) ", end='')
      #id = input()
      ans = input()
      if (ans == "help"):
        Help()    # Функция, позволяющая представить функционал
      elif (ans == "list"):   # Лист друзей пользователя
        print_list_of_friends()
      elif(ans == "chat"):    # Пользователь будет переписываться с друзьями
        writing()

  sock.close()

def registration():

  print("Здравствуйте, раз уж вы здесь первый раз, то пора получить анкету!")
  print("Введите свое имя ", end='')

  name = input()
  get_ID("1")    # Получаем от сервера индивидуальный ID
  print("Так, хорошо!Но нужно позаботиться и об безопасности!")
  print("Теперь введите пароль ", end='')

  password = input()
  flag_pas = hs.varify_password(password)   # проверка пароля на надежность и кол-во символов, и  т.п.

  while(flag_pas == False):
    password = input()
    flag_pas = hs.varify_password(password)

  print("Повторите ваш пароль: ", end='')

  password_one = input()
  while (password_one != password):
    print("Пароли не совпадают!! Повторите ввод ", end="")
    password_one = input()
    #TODO Возможно нужно добавить такую функцию, которая бы выводила в консоль 
    # текст и пользователь вводил его для проверки того, что он является человеком 

  hash_password = hs.hashing(password)
  post_anketa_to_server(name, hash_password)    # Отпрявляем свое имя и хэш пароль для БД сервера

  print("Отлично. Вы зарегестрировались!")
  print("============================================================================")
  