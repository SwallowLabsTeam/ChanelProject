import logging


class LoggingConf:
    HOST = '192.168.1.250'
    PORT = 514

    LEVEL_BROKER = logging.DEBUG
    LEVEL_CAPSULE = logging.DEBUG
    LEVEL_CLIENT = logging.DEBUG

    FACILITY_BROKER = 'local0'
    FACILITY_CAPSULE = 'local1'
    FACILITY_CLIENT = 'local2'

    FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

