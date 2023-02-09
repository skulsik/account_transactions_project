from utils import ListOfOperation


# Создаем экземпляр для теста
LOO = ListOfOperation()


class Test_ListOfOperation():
    def test_modified_from_account_false(self):
        assert LOO.modified_from_account() == "Номер счета неизвестен"


    def test_modified_from_account_16symbol(self):
        assert LOO.modified_from_account({"rtr": "fhghfg", "from": "Cчет 1234123456785678"}) == "Cчет 1234 12** **** 5678"


    def test_modified_from_account_20symbol(self):
        assert LOO.modified_from_account(
            {"rtr": "fhghfg", "from": "Cчет 12341234567856780000"}) == "Cчет 1234 12** **** **** 0000"


    def test_modified_to_account_true(self):
        assert LOO.modified_to_account("Счет 12341234567856788980") == "Счет **8980"


    def test_modified_to_account_false(self):
        assert LOO.modified_to_account() == "Номер счета неизвестен"


    def test_load_list_of_operations_true(self):
        http_json = "https://s3.us-west-2.amazonaws.com/secure.notion-static.com/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230209%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230209T044708Z&X-Amz-Expires=86400&X-Amz-Signature=033d7d7e6cbe598c998c491239e9d0f6e5f1d9dfef273cb58a6a79eeb5524216&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22operations.json%22&x-id=GetObject"
        assert LOO.load_list_of_operations(http_json) != None


    def test_add_list_of_date(self):
        LOO.list_of_operations = [{'date': '4355', 'state': 'EXECUTED'},
                                  {'id': '999', 'state': 'EXECUTED'},
                                  {'date': '000', 'state': 'CANCELED'},
                                  {'date': '777', 'state': 'EXECUTED'},
                                  {}]
        assert LOO.add_list_of_date() == ['4355', '777']


    def test_sort_list_of_date(self):
        LOO.list_of_date = [1, 5, 8, 9, 3, 18, 4]
        assert LOO.sort_list_of_date() == [18, 9, 8, 5, 4, 3, 1]


    def test_range_list_of_date_no_value(self):
        LOO.list_of_date = [1, 5, 8, 9, 3, 18, 4]
        assert LOO.range_list_of_date() == [1]


    def test_range_list_of_date_yes_value(self):
        LOO.list_of_date = [1, 5, 8, 9, 3, 18, 4]
        assert LOO.range_list_of_date(3) == [1, 5, 8]
