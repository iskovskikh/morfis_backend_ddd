from datetime import timedelta

MORFIS = {
    'REGISTRATION_NUMBER': {
        # время аренда нового регистрационного номера
        'REGISTRATION_NUMBER_LIFETIME': timedelta(seconds=10),

        # шаблон генерации нового регистрационного номера
        # {smth:07} - отформатирует переменную до 7 знаков (заполнит лидирующими нулями)
        # {current_no}
        # {yearly_current_no}
        # {day}
        # {month}
        # {year}
        # {day_of_week}
        # {week_no}
        'REGISTRATION_NUMBER_TEMPLATE': '{day}/{month}/{year}#{current_no:06}',
    }
}
