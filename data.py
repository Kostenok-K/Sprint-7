class URL:
    BASE = 'https://qa-scooter.praktikum-services.ru'
    LOGIN = f'{BASE}/api/v1/courier/login'
    COURIER = f'{BASE}/api/v1/courier'
    ORDER = f'{BASE}/api/v1/orders'
    ACCEPT_ORDER = f'{BASE}/api/v1/orders/accept/'
    TRACK_ORDER = f'{BASE}/api/v1/orders/track'


class Answers:
    SAME_LOGIN = 'Этот логин уже используется. Попробуйте другой.'
    NOT_DATA_FOR_CREATE = 'Недостаточно данных для создания учетной записи'
    NOT_DATA_FOR_AUTH = 'Недостаточно данных для входа'
    ACCOUNT_NOT_FOUND = 'Учетная запись не найдена'
