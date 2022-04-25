from ..log_file import Loggers

print("in test1")


def test_logger():
    log = Loggers(level='info')
    log.logger.info('nihao')


test_logger()

333
