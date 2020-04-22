# ввод своих фин остатков
cash = int(input("Введите пожалуйста сколько у вас налички \n"))
bez_nal = int(input("Введите пожалуйста сколько у вас карточки\n"))
y = ["Январе", "Феврале", "Марте", "Апреле", "Мае", "Июне", "Июле", "Августе", "Сентябре", "Октябре", "Ноябре",
     "Декабре"]


# Функция для подсчета финансов
def test(nal, b_nal):
    global bez_nal, cash
    counter = 0
    # цикл по месяцам
    while counter < 12:
        cash = int(cash)
        bez_nal = float(bez_nal)
        cash = round(cash, 2)
        bez_nal = round(bez_nal, 2)
        cash = str(cash)
        bez_nal = str(bez_nal)
        print(f"\nУ вас в {y[counter]} будет: \n Налички:{cash}\n На карточке: {bez_nal}")
        counter = counter + 1
    return cash, bez_nal


# Проверка если у вас деньги, или нет
if (cash > 0) or (bez_nal > 0):
    # вызов функции
    test(cash, bez_nal)
else:
    print("Вы бедные :(")