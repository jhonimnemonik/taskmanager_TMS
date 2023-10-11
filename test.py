import psutil
import datetime
import time
from functools import wraps


def log_to_file(file_name):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            dat_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            result = func(*args, **kwargs)
            with open(file_name, 'a') as file:
                file.write(f"{dat_time}\n")
                file.write(f"Get  for: '{func.__name__}'\n")
                file.write(f"Info : {result}\n\n")
            return result  
        return wrapper
    return my_decorator


@log_to_file('log.txt')
def user_info_get():
    user_info_list = []
    users = psutil.users()
    for user in users:
        name = user.name
        session_time = user.started
        user_info_list.append((name, session_time))
    return user_info_list


@log_to_file('log.txt')
def cpu_get():
    _times = psutil.cpu_times()  
    percent = psutil.cpu_percent(interval= 0)
    return _times, percent


@log_to_file('log.txt')
def memory_get():
    mem_info = psutil.virtual_memory()
    total = mem_info.total
    percent = mem_info.percent
    free = mem_info.available
    return {total, percent, free}


@log_to_file('log.txt')
def boot_get():
    time_value = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(time_value).strftime("%Y-%m-%d %H:%M:%S")
    since_time = "{:.0f}".format(time_value / 360) + ' H.'
    return {boot_time, since_time}


@log_to_file('log.txt')
def info_apps_get():
    process_info = []
    for number, proc in enumerate(psutil.process_iter(['name', 'pid', 'status', 'username', 'cpu_percent']), start = 1):
        info = proc.as_dict(['name', 'pid', 'status', 'username', 'cpu_percent'])
        process_info.append({
            'number': number,
            'name': info.get('name'),
            'pid': info.get('pid'),
            'status': info.get('status'),
            'username': info.get('username'),
            'cpu_percent': info.get('cpu_percent')
        })
    return process_info


def title_show(user_info_list, title_name):
    buton = "⊟ ⊡ ⊠ ╗"
    print(f"╔{title_name:═^104}", f"{buton:<7}")
    for user_name, user_time in user_info_list:
        print("║{:>90}{:<10}{:<10}║".format("", "User name: ", user_name))
        print("║{:>90}{:<10}{:<10}║".format("", "On system: ", time.strftime("%H:%M:%S", time.gmtime(user_time))))


def cpu_show(cpu_data):
    _times, percent = cpu_data
    load = "{:░<10}".format("▓" * int(percent / 10))
    user_time = time.strftime("%H:%M:%S", time.gmtime(_times.user))
    system_time = time.strftime("%H:%M:%S", time.gmtime(_times.system))
    print("║\t{:<10}{:<10}{:<10}{}{:<64}║".format("CPU", "Load:", str(percent) + " % ", load, ""))
    print("║\t{:<10}{:<10}{:<10}{:<74}║".format("CPU time", "User:", str(user_time), ""))
    print("║\t{:<10}{:<10}{:<10}{:<74}║".format("", "System:", str(system_time), ""))
    print("║{:<111}║".format(""))


def memory_show(mem_data):
    total, free, percent = mem_data
    load = "{:░<10}".format("▓" * int(percent / 10))
    print("║\t{:<10}{:<10}{:<10}{}{:<64}║".format("Ram", "Load:", str(percent) + " % ", load, ""))
    print("║\t{:<10}{:<10}{:<10}{:<74}║".format("", "Total:", str(total // 1024 ** 2) + " Mb.", ""))
    print("║\t{:<10}{:<10}{:<10}{:<74}║".format("", "Free:", str(free // 1024 ** 2) + " Mb.", ""))
    print("║{:<111}║".format(""))


def boot_show(boot_time, since_time):
    print("║\t{:<15}{:<5}{:<30}{:<54}║".format("Boot time:", "", boot_time, ""))
    print("║\t{:<15}{:<5}{:<30}{:<54}║".format("Time since On:", "", since_time, ""))


def process_list_show(processes, num_running_apps):
    print("║\t{:<20}{:<84}║".format("Runs applications:", num_running_apps))
    print("║{:<111}║".format(""))
    print("╠{0:─^3}┬{0:─^64}┬{0:─^22}┬{0:─^5}┬{0:─^5}┬{0:─^7}╣".format("─"))
    print("║{:^3}│{:^64}│{:^22}│{:^5}│{:^5}│{:^7}║".format("№", "Name", "User", "%", "PID", "Status"))
    print("╠{0:─^3}┼{0:─^64}┼{0:─^22}┼{0:─^5}┼{0:─^5}┼{0:─^7}╣".format("─"))
    for process in processes:
        if process['username'] is not None:
            print("║{:<3}│{:<64}│{:^22}│{:^5}│{:^5}│{:^7}║".format(
                process['number'], process['name'],
                process['username'], process['cpu_percent'],
                process['pid'], process['status']
            ))
        else:
            print("║{:<3}│{:<64}│{:^22}│{:^5}│{:^5}│{:^7}║".format(
                process['number'], process['name'],
                "None", process['cpu_percent'],
                process['pid'], process['status']
            ))
    print("╚{0:═^3}╧{0:═^64}╧{0:═^22}╧{0:═^5}╧{0:═^5}╧{0:═^7}╝".format("═"))


def main():
    title_show(user_info_get(), "Task Manager")
    cpu_show(cpu_get())
    memory_show(memory_get())
    boot_show(*boot_get()) 
    num_running_apps = len([process for process in info_apps_get() if process['status'] == 'running'])
    process_list_show(info_apps_get(), num_running_apps)

if __name__ == "__main__":
    main()
