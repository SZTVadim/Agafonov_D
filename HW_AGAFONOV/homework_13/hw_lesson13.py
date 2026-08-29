class TestCase:

    def __init__(self, name, status="new", duration=None):
        self.name = name
        self.status = status
        self.duration = duration

    def can_run(self):
        return self.status == "new"

    def finish(self, result, duration):
        if self.can_run() == False:
            return False
        elif result != "passed" and result != "failed":
            return False
        else:
            self.status = result
            self.duration = duration
            return True

    def is_slow(self):
        if self.duration is None:
            return None
        elif self.duration >= 5:
            return True
        else:
            return False


test_1 = TestCase("Авторизация")
test_2 = TestCase("Регистрация")
test_2.finish("passed", 4)
test_3 = TestCase("Оплата")
test_3.finish("passed", 7)
test_3.finish("failed", 10)
print(test_1.name)
print(test_1.can_run())
print(test_1.is_slow())
print(test_1.status)

print(test_2.name)
print(test_2.can_run())
print(test_2.is_slow())
print(test_2.status)

print(test_3.name)
print(test_3.can_run())
print(test_3.is_slow())
print(test_3.status)
