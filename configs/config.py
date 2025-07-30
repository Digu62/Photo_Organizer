import sys
import logging
from colorama import Fore, Style

class CustomFormatter(logging.Formatter):
    LOG_COLORS = {
        "DEBUG": Fore.BLUE,
        "INFO": Fore.GREEN,
        "WARNING": Fore.YELLOW,
        "ERROR": Fore.RED
    }

    def format(self, record):
        """Formata a mensagem de log com core.

        Args:
            record (LogRecord): Objeto contendo informações do log.

        Returns:
            str: String formatado com a cor e o nível do log.
        """
        log_color = self.LOG_COLORS.get(record.levelname, Fore.WHITE)
        return f"{log_color}Photo Organizer |{record.levelname}(linha {record.lineno}){Style.RESET_ALL}: {record.msg}"


logger = logging.getLogger(__name__)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(CustomFormatter())
logger.addHandler(handler)

logger.setLevel(logging.DEBUG)

logger.info("Logger Initialized successfully.")