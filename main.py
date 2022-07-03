import application.people as app
import application.salary as aps
from datetime import date


if __name__ == '__main__':
    print(app.get_employees())
    print(aps.calculate_salary())
    print(date.today())

