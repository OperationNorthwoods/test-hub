import syslog


def exceptionTest():
    print('testing exception start')
    myException = Exception('uh oh, stinky!')
    raise myException


def handleException():
    try:
        print('do this')
        exceptionTest()
        print('than that')
    except Exception as e:
        print(e)
        syslog.syslog('This is a test')
        syslog.closelog()
        print('This has been logged.')
    finally:
        print('Done.')
    print('than that')


logPriors = (syslog.LOG_EMERG, syslog.LOG_ALERT, syslog.LOG_CRIT, syslog.LOG_ERR,
             syslog.LOG_WARNING, syslog.LOG_NOTICE, syslog.LOG_INFO, syslog.LOG_DEBUG)


def logPriorsTest():
    for prior in logPriors:
        syslog.syslog(prior, f'just testing {prior}. Ignore this.')
    syslog.closelog()
    print('Done.')


logPriorsTest()
