import schedule
import time
import threading

def run_continuously_task():
    cease_continuous_run = threading.Event()

    class ScheduleThread(threading.Thread):
        @classmethod
        def run(cls):
            while not cease_continuous_run.is_set():
                schedule.run_pending()
                time.sleep(1)

    continuous_thread = ScheduleThread()
    continuous_thread.start()
    return cease_continuous_run

def get_time():
    return time.strftime('%X (%d/%m/%y)')

def validate_time(input):
    time_formats = ['%H:%M:%S', '%H:%M', '%H']
    for format in time_formats:
        try:
            time.strptime(input, format)
            return format
        except ValueError:
            pass
    return False

def set_one_time_job(job, arg1, arg2, arg3):
    job(arg1, arg2, arg3)
    return schedule.CancelJob