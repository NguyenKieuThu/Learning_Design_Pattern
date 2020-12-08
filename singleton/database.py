"""
Create only one instance for one class in all times of programming. Prefer to connect a database or open a file.
ref: https://refactoring.guru/design-patterns/singleton
"""


class Database:
    _instance = None
    _number_instance = 0

    def __init__(self):
        if Database._instance is None:
            print("Init new instance")
            self._name_database = "test"
            self._ip = 'localhost'
            self._status = 'connect'
            Database._instance = self
            Database._number_instance += 1
        else:
            raise Exception("You can't create second instance, use get_instance to get instance!")

    @staticmethod
    def get_instance():
        if Database._instance is None:
            return Database()
        else:
            print("Return old instance")
            return Database._instance

    @staticmethod
    def show_information():
        print("the number of instance is: {}".format(Database._number_instance))


if __name__=='__main__':
    print("Create first instance")
    instance_data1 = Database()
    instance_data1.show_information()
    print("Add 3 instances")
    instance_data2 = Database.get_instance()
    instance_data3 = Database.get_instance()
    instance_data4 = Database.get_instance()
    print("Show information of 4th instance")
    instance_data4.show_information()
    print("When you call constructor of Database in the second time, it's not work")
    instance_data5 = Database()  # raise the error
