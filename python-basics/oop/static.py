class Test:

    def test_method(self):
        print(f"Called instance method of {self}")

    @classmethod # factory pattern
    def class_method(cls):
        print(f"Called class method of {cls}")

    @staticmethod
    def static_method():
        print("Called static method")
    
    def __str__(self):
        return "Test object"


test = Test()
print(test.test_method())
print(test.class_method())
Test.static_method()