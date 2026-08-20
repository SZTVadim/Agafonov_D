# ЗАДАНИЕ 1: Распаковка списка и слияние

statuses = ["queued", "running", "testing", "deploy", "done"]
first, *middle, last = statuses
print(first)
print(last)
print(middle)

statuses = ["failed", "skipped"]
new_statuses = [*middle, *statuses]
print(first)
print(last)
print(new_statuses)


# ЗАДАНИЕ 2: Словарь, слияние и вызов функции

browser = {"browser": "chrome", "timeout": 3000}
options = {"headless": True, "timeout": 5000}

config = {**browser, **options}
def start_session(browser, timeout, headless):
    return f"{browser}, timeout={timeout}, headless={headless}"


print(start_session(**config))
