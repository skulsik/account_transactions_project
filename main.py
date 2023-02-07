import utils


# Ссылка на список операций, совершенных клиентом банка
http_json = "https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1675831434998&signature=lY-pAzeCBWbr947P24hidfo3crgVkrY0R2N_9iZFXKE&downloadName=operations.json"

# Количество последних операций, которые мы хотели бы увидеть
number_of_operations = 5

# Создаем экземпляр класса
list_of_operation = utils.ListOfOperation()

# Получает файл со списком операций, совершенных клиентом банка: с внешнего ресурса
list_of_operation.load_list_of_operations(http_json)

# Создание списка с успешно проведенными операциями и их датами
list_of_operation.add_list_of_date()

# Сортировка дат
list_of_operation.sort_list_of_date()

# Создаем список с нужным количеством дат
list_of_operation.range_list_of_date(number_of_operations)

# Выводим последнии n операций
list_of_operation.print_list_of_operations()
