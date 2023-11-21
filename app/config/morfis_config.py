from datetime import timedelta

MORFIS = {
    'REGISTRATION_NUMBER': {
        # время аренда нового регистрационного номера
        'REGISTRATION_NUMBER_LIFETIME': timedelta(seconds=60),

        # шаблон генерации нового регистрационного номера
        'REGISTRATION_NUMBER_TEMPLATE': '{current_no} REGISTRATION_NUMBER_TEMPLATE!',
    }
}
