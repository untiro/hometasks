try:
    import os
    import sys
    from crontab import CronTab
except(ImportError, ImportWarning):
    print('Errors importing python modules')

# Reading arguments from command line
if len(sys.argv) > 1:
    if sys.argv[1] == 'install' and len(sys.argv) > 2:
        my_cron = CronTab(user='student')
        job = my_cron.new(command='python {}/task5.py'.format(os.path.dirname(__file__)))
        job.comment = 'Task5'
        job.minute.every(sys.argv[2])
        my_cron.write()
        print('task5.py was successfully scheduled in cron')
    elif sys.argv[1] == 'uninstall':
        my_cron = CronTab(user='student')
        for job in my_cron:
            if job.comment == 'Task5':
                my_cron.remove(job)
                my_cron.write()
                print('task5.py was successfully removed from cron')
    else:
        print('Script usage: {} (install <x>|uninstall)\n where <x> - interval in minutes to run from cron.'.format(sys.argv[0]))
else:
    print('Script usage: {} (install <x>|uninstall)\n where <x> - interval in minutes to run from cron.'.format(sys.argv[0]))

