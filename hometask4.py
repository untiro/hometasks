try:
    import psutil
    import datetime
    import configparser
    import os
    import json
    import sys
    from time import sleep
except(ImportError, ImportWarning):
    print('Errors importing python modules')


class Logger:
    def __init__(self, file_name):
        if not os.path.isfile(file_name):
            try:
                with open(file_name, 'a') as fl:
                    pass
            except:
                print('Error creating log file: {}'.format(file_name))


class JsonLogger(Logger):
    @staticmethod
    def write_json(log_file, jsn_data):
        try:
            with open(log_file, 'a') as fl:
                fl.write(json.dumps(jsn_data, ensure_ascii=False))
                fl.write('\n')
        except:
            print('Error writing json data to file: {}'.format(log_file))


class TextLogger(Logger):
    @staticmethod
    def write_log(log_file, log_data):
        try:
            if os.path.isfile(log_file):
                with open(log_file, 'a') as fl:
                    fl.write(log_data)
        except:
            print('Error writing log data to file: {}'.format(log_file))


class Counter(Logger):
    @staticmethod
    def counter(cnt_file, cnt=None):
        if cnt is None:
            if os.path.isfile(cnt_file) and os.path.getsize(cnt_file) > 0:
                with open(counters, 'r') as fl:
                    return int(fl.readline().strip())
            else:
                return 0
        else:
            with open(counters, 'w') as fl:
                fl.write(str(cnt))


# Define config file
if len(sys.argv) > 1:
    conf_file = sys.argv[1]
else:
    conf_file = 't5.conf'

# Reading config file and parameters
try:
    os.chdir(os.path.dirname(__file__))
    path = os.path.abspath(conf_file)
    print('Reading monitoring script {} config file: {}'.format(sys.argv[0], path))
    config = configparser.ConfigParser()
    config.read(path)
    log_type = config.get('common', 'output')
    interval = config.getint('common', 'interval')
    iterations = config.getint('common', 'iterations')
    counters = config.get('common', 'counters')
    log_file = config.get(log_type, 'filename')
except:
    print('Error reading config file: {}'.format(conf_file))

data, i = {}, 0

# Creating class objects
if log_type == 'log':
    lg = TextLogger(log_file)
else:
    js = JsonLogger(log_file)
sn = Counter(counters)

while True:
    if iterations > 0 and i < iterations:
        i += 1
    elif 0 < iterations == i:
        break
    cpu_load = str(psutil.cpu_percent())
    mem_load = str(psutil.virtual_memory().used)
    virtmem_load = str(psutil.swap_memory().used)
    disk_io = str(psutil.disk_io_counters())
    net_inf = str(psutil.net_io_counters())
    moment = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    count = 1 + sn.counter(counters)
    log_data = 'SNAPSHOT ' + str(count) + ': ' + moment + ' \tCPU load(%): ' + cpu_load + '\tMEM used: ' + \
        mem_load + '\tVirt mem used: ' + virtmem_load + '\tIO: ' + disk_io + '\tNetwork: ' + net_inf + '\n'
    data['SNAPSHOT'] = count
    data['Date'] = moment
    data['CPU load(%)'] = cpu_load
    data['MEM used'] = mem_load
    data['Virt mem used'] = virtmem_load
    data['IO'] = disk_io
    data['Network'] = net_inf
    print(log_data)

    if log_type == 'log':
        lg.write_log(log_file, log_data)
    else:
        js.write_json(log_file, data)
    sn.counter(counters, count)
    sleep(interval*60)

