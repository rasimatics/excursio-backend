import logging
from ..config.settings import app_settings


class UpdatableLogger(logging.Logger):
    """
        Logger (parameters can be modified)
    """
    def makeRecord(self, name, level, fn, lno, msg, args, exc_info,
                   func=None, extra=None, sinfo=None):
        """
        A factory method which can be overridden in subclasses to create
        specialized LogRecords.
        """
        rv = logging._logRecordFactory(name, level, fn, lno, msg, args, exc_info, func,
                             sinfo)
        if extra is not None:
            for key in extra:
                rv.__dict__[key] = extra[key]
        return rv
    
    def __str__(self) -> str:
        return self.name + " -" + str(id(self))

logging.setLoggerClass(UpdatableLogger)


def setup_logger(name, log_file, level, formatter):    
    """
        Create logger
    """
    handler = logging.FileHandler(log_file)
    handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger


def get_app_logger():
    """
        get app logger for dependency
    """
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(funcName)s %(statuscode)s %(pathname)s %(message)s')
    logger = setup_logger("Application logs", f"{app_settings.APP_LOG_FILE_PATH}/{app_settings.APP_LOG_FILE}", logging.INFO, formatter)
    return logger
