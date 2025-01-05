# utils/logger_config.py
import logging

def setup_logger():
    # Crear un logger
    logger = logging.getLogger("test_logger")
    logger.setLevel(logging.INFO)  # Configuramos el nivel de log deseado

    # Crear un manejador de consola para los logs
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)  # Establecer el nivel para la consola

    # Crear un manejador de archivo para guardar los logs en un archivo
    file_handler = logging.FileHandler('test_logs.log')  # El archivo de log
    file_handler.setLevel(logging.INFO)  # Establecer el nivel para el archivo

    # Crear un formato para los logs
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    file_handler.setFormatter(formatter)

    # Agregar ambos manejadores al logger
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger
