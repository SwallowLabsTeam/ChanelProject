import logging
import logging.handlers
from org.swallow_labs.tool.LoggingConf import LoggingConf
import json


class LoggerAdapter:

    def __init__(self, level, host, port, facility, format, id_logger):

        self.id_logger = id_logger
        self.level = level
        self.host = host
        self.port = port
        self.facility = facility
        self.format = format

        self.logger = logging.getLogger(id_logger)
        self.logger.setLevel(level)
        syslog = logging.handlers.SysLogHandler(address=(host, port), facility=facility)
        # fh.setLevel(level)
        formatter = logging.Formatter(format)
        syslog.setFormatter(formatter)
        self.logger.addHandler(syslog)

    def log(self, msg, level):

        if level is 'debug':
            self.logger.debug(msg)
        elif level is 'info':
            self.logger.info(msg)
        elif level is 'emerg':
            self.logger.emerg(msg)
        elif level is 'error':
            self.logger.error(msg)
        elif level is 'warning':
            self.logger.warning(msg)
        elif level is 'alert':
            self.logger.alert(msg)

    def log_broker_start(self, arg1, arg2):
        self.logger.info('Broker start: ' + 'PORT: Frontend: ' + str(arg1) + ' Backend: ' + str(arg2))

    def log_broker_send(self, arg1, arg2):
        self.logger.debug('Sent to client {} : {}'.format(arg1, json.dumps(arg2.__dict__)))

    def log_broker_receive(self, arg1):
        self.logger.debug('Received from client {} : {}'.format(arg1.get_id_sender(), json.dumps(arg1.__dict__)))

    def log_client_connect(self, arg1, arg2, arg3):
        self.logger.info('Client {} Connected to {} on port: {}'.format(arg1, arg2, arg3))

    def log_client_push(self, arg1):
        self.logger.debug('Sent : {}'.format(arg1.__dict__))

    def log_client_pull(self, arg1):
        self.logger.debug('Messages received {}'.format(arg1.__dict__))

    def log_server_down(self):
        self.logger.debug('Server down')

