import utils


# Ссылка на список операций, совершенных клиентом банка
http_json = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230209T044708Z&X-Amz-Expires=86400&X-Amz-Signature=033d7d7e6cbe598c998c491239e9d0f6e5f1d9dfef273cb58a6a79eeb5524216&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject"

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
