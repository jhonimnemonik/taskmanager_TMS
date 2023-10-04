import psutil, datetime, time


def user_info_get():
    users = psutil.users()
    for user in users:
        name = user[0]
        time = user[3]
        return name , time
    

def title_show(user_name, user_time , titl_name):
    buton = "⊟ ⊡ ⊠ ╗"
    print (f"╔{titl_name:═^104}" , f"{buton:<7}")
    print ("║{:>90}{:<10}{:<10}║" .format ("" , "User name: " , user_name))
    print ("║{:>90}{:<10}{:<10}║" .format ("" , "On system: " , time.strftime("%H:%M:%S" , time.gmtime(user_time))))


def cpu_get():
    _times = psutil.cpu_times()  
    percent = psutil.cpu_percent(interval=0)
    return _times[0] ,_times[1] , percent

      
def cpu_load_show(percent):
    bar = "{:░<10}"
    load = bar.format ("▓" * int(percent / 10))
    return print ("║\t{:<10}{:<10}{:<10}{}{:<64}║".format("CPU" , "Load:" , str(percent) + " % " , load , ""))


def cpu_timesup_show():
    user_time = time.strftime("%H:%M:%S" , time.gmtime(cpu_get()[0]))
    system_time = time.strftime("%H:%M:%S" , time.gmtime(cpu_get()[1]))
    print ("║\t{:<10}{:<10}{:<10}{:<74}║".format("CPU time" , "User:" , str(user_time) , ""))
    print ("║\t{:<10}{:<10}{:<10}{:<74}║".format("" , "System:" , str(system_time) , ""))
    print ("║{:<111}║" .format(""))


def memory_get():
    mem_info = psutil.virtual_memory()
    total = mem_info[0]
    percent = mem_info[2]
    free = mem_info[4]
    return total , percent , free


def memory_show(total , percent , free):
    bar = "{:░<10}"
    load = bar. format ("▓" * int(percent / 10))
    print ("║\t{:<10}{:<10}{:<10}{}{:<64}║".format("Ram" , "Load:" , str(percent) + " % " , load , ""))
    print ("║\t{:<10}{:<10}{:<10}{:<74}║".format("" , "Total:" , str(total//1000**2) + " Mb." , ""))
    print ("║\t{:<10}{:<10}{:<10}{:<74}║".format("" , "Free:" , str(free//1000**2) + " Mb." , ""))
    print ("║{:<111}║" .format(""))

  
def boot_time_show():
    time_value = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(time_value).strftime("%Y-%m-%d %H:%M:%S")
    since_time = "{:.0f}".format(time_value/360)+' H.'
    print ("║\t{:<15}{:<5}{:<30}{:<54}║" .format ("Boot time:" , "" , boot_time , ""))
    print ("║\t{:<15}{:<5}{:<30}{:<54}║" .format ("Time since On:", ""  , since_time , ""))
 

def number_apps_get():
    num_app = 0 
    for number in psutil.process_iter():
        num_app += 1
    return num_app
 

def process_list_show(num_app):
    print ("║\t{:<20}{:<10}{:<21}{:<53}║" .format ("Runs applications:" , num_app , "" , ""))
    print ("║{:<111}║" .format(""))
    print ("╠{:─^6}┬{:─^65}┬{:─^10}┬{:─^12}┬{:─^14}╣" .format ("─" , "─" , "─" , "─" , "─" , "─" ))
    print ("║{:^6}│{:^65}│{:^10}│{:^12}│{:^14}║" .format ("№" , "Name" , "%" , "PID" , "Status", "User"))
    print ("╠{:─^6}┼{:─^65}┼{:─^10}┼{:─^12}┼{:─^14}╣" .format ("─" , "─" , "─" , "─" , "─" , "─" ))

    
    def name_list(): 
        n_app = 0

        for list_string in psutil.process_iter():
            n_app += 1   
            pid = list_string.as_dict(['pid'])
            name = list_string.as_dict(['name'])
            user = list_string.as_dict(['username'])
            perc = list_string.as_dict(['cpu_percent'])
            stat = list_string.as_dict(['status'])
            
            print (
                  "║{:^6}│{:<65}│{:^10}│{:^12}│{:^14}║" .format 
                  (str(n_app) , name['name'] , perc['cpu_percent'] ,
                  pid['pid'] , stat['status'] , user['username'])
                  )
    
    name_list()
    return print ("╚{:═^6}╧{:═^65}╧{:═^10}╧{:═^12}╧{:═^14}╝" .format ("═" , "═" , "═" , "═" , "═"))
       

def main():
    title_show(user_info_get()[0] , user_info_get()[1] , "Task Manager")
    cpu_load_show(cpu_get()[2])
    cpu_timesup_show()
    memory_show(memory_get()[0] , memory_get()[1] , memory_get()[2])
    boot_time_show()
    process_list_show(number_apps_get())

    
main()
 