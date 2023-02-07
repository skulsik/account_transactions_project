import requests, datetime


class ListOfOperation:
    def modified_from_account(self, operation):
        """
        Скрываем часть счета отправителя, разбиваем счет по 4 цифры
        :param operation: Передает строку с названием счета и сам счет, может быть пустая строка
        :return: Возврат частично скрытых символов в счете
        """
        # Проверка существования счета отправителя
        if 'from' in operation:

            # Разбиваем строку по пробелам, получаем: слово/слова и последний элемент номер счета
            from_account = operation['from'].split()
            # Выделяем номер счет в переменную
            account = from_account[len(from_account) - 1]
            # Удаляем номер счета из переменной, для дальнейшего склеивания с модифицированной переменной
            del from_account[len(from_account) - 1]

            # Разбиваем номер счета на список из четырех символов и тут же склеиваем в строку
            modified_account = ' '.join(account[i:i + 4] for i in range(0, len(account), 4))
            # На случай когда символов в счете > 16
            if len(modified_account) > 19:
                add_str = "**** "
            else:
                add_str = ""
            modified_account = " " + modified_account[0:7] + "** **** " + add_str + modified_account[len(modified_account) - 4:len(modified_account)]

            from_account = " ".join(from_account) + modified_account
            return from_account
        else:
            return "Номер счета неизвестен"

    def modified_to_account(self, operation):
        """
        Скрываем часть счета получателя
        :param operation: Передает строку с названием счета и сам счет
        :return: Возврат частично скрытых символов в счете
        """
        to_account = operation[0:4] + " **" + operation[21:25]
        return to_account


    def __init__(self):
        self.list_of_operations = []
        self.list_of_date = []


    def load_list_of_operations(self, http_json):
        """
        получает файл со списком операций, совершенных клиентом банка: с внешнего ресурса
        :param http_json: ссылка на фаил json
        :return:
        """
        request = requests.get(http_json)
        self.list_of_operations = request.json()


    def add_list_of_date(self):
        """
        Создание списака с датами успешных операций
        :return:
        """
        for operation in self.list_of_operations:

            # Проверка существования ключа в словаре
            if 'date' in operation:

                # Отбор только успешных операций и запись их в список
                if operation['state'] == 'EXECUTED':
                    self.list_of_date.append(operation['date'])


    def sort_list_of_date(self):
        """
        Сортировка списка с датами, в порядке убывания
        :return:
        """
        self.list_of_date.sort(reverse=True)


    def range_list_of_date(self, number_of_operations = 1):
        """
        Оставляем желаемое количство дат(операций), от остальных избавляемся
        :param number_of_operations: количество дат(в дальнейшем операций, выведенных на экран)
        :return:
        """
        self.list_of_date = self.list_of_date[0:number_of_operations]


    def print_list_of_operations(self):
        """
        Вывод данных о операции на экран
        :return:
        """
        for index in self.list_of_date:
            for operation in self.list_of_operations:

                # Проверка: существования ключа в словаре; соответствие нужной даты в данной операции
                if 'date' in operation and index in operation['date']:

                    # Переводим строку к формату "дата"
                    date_D = datetime.datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')

                    # Выводим данные по ТЗ
                    print(f'{date_D.strftime("%d.%m.%Y")} {operation["description"]}')

                    # Скрываем часть счета отправителя
                    from_account = self.modified_from_account(operation)

                    # Скрываем часть счета на который поступили средства
                    to_account = self.modified_to_account(operation['to'])

                    print(f"{from_account} -> {to_account}")
                    print(f"{operation['operationAmount']['amount']} {operation['operationAmount']['currency']['name']}\n")
