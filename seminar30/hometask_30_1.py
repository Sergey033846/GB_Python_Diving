# Задание 1. Логирование с использованием нескольких файлов
# Напишите скрипт, который логирует разные типы сообщений в разные файлы.
# Логи уровня DEBUG и INFO должны сохраняться в debug_info.log, 
# а логи уровня # WARNING и выше — в warnings_errors.log.


import logging


# Создание логгера
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)


# Создание обработчиков для файлов логов
debug_handler = logging.FileHandler('debug_info.log', encoding='utf-8')
debug_handler.setLevel(logging.DEBUG)


warning_handler = logging.FileHandler('warnings_errors.log', encoding='utf-8')
warning_handler.setLevel(logging.WARNING)


# Создание форматтера для форматирования сообщений логов
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
debug_handler.setFormatter(formatter)
warning_handler.setFormatter(formatter)


# Добавление обработчиков к логгеру
logger.addHandler(debug_handler)
logger.addHandler(warning_handler)


logger.debug('Это сообщение отладки')
logger.info('Информационное сообщение')
logger.warning('Предупреждение')
logger.error('Ошибка!')
logger.critical('Критическое сообщение!!!')
