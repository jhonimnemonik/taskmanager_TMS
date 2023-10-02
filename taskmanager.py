import psutil
import datetime
import time

TIMES=psutil.cpu_times()


def format_left(*argc):
    """Левый формат."""
    print("|\t{:<90}|".format(*argc))
    return


def name(*argc):
    # Заголовок
    print("|{:■^90}".format(*argc), end=" ⊟ ⊡ ⊠ |\n")
    return


def format_right(*argc):
    for arg in argc:
        print("|\t{:>90}|".format(arg))
    return


# Имя пользователя
def user_get(): 
    users = psutil.users()
    for user in users:
        format_right("User name :    " + user[0])
        n = int(user[3])
        time_format = time.strftime("%H:%M:%S", time.gmtime(n)) 
        format_right("On system :" + time_format)


def load_bar(value):
    template = "[{:<.10}]"
    return template.format("|" * int(val / 10))


# Данные процессора  
def CPU_show():    
    a = psutil.cpu_percent(interval=1)  
    format_left("CPU        Load   : "+str(a)+"% "+ load_bar(a))
    format_left('CPU time   User   : '+ ("{:.1f}".format(_times[0])) + " Min.")
    format_left('           System : '+ ("{:.1f}".format(_times[1]/60)) + " Min.")
    format_left("") # space


# Оперативная память
def memory():
    mem = psutil.virtual_memory()
    percent = mem[2]
    format_left('Ram        Load   : ' + str(percent)+"% "+ load_bar(persent))
    format_left('           Total  : '"{:.0f}".format(mem[0]/1000**2)+ "Mb.")
    format_left('           Free   : '"{:.0f}".format(mem[4]/1000**2)+ "Mb.")
    format_left("      ") # space


# Боот
def Boot_Time():
    format_left('Boot time         : '+str(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S")))
    format_left('Time since On     : '"{:.0f}".format(psutil.boot_time()/360)+' H.')
    format_left("")
    return


user_get()
CPU_show()
memory()
Boot_Time()


# Список запущенных приложений
def Process_list():
    
    # Форматирование границы
    def edge():
        print("|{:-^97}|".format(''))
        return
        
    # Форматирование спсика
    def format_this(*argc):
        print("| {:<96}|".format(*argc))
        return
        
    #Количество Зап. прилож.
    def runs():
        num=0 
        for p in psutil.process_iter():
            num+=1
        format_left('Runs applications : ' + str(num))
        format_left("")

    #Заголовок списка
    def Name_List():
        edge()
        templ_1 = " №  | {:<30} | {:^10} |{:^10} |{:^10}| {}".format("Name", "%", "PID", "User", "Status")
        format_this(templ_1)
        edge()
   
        for num, p in enumerate(psutil.process_iter()):
            a=p.as_dict(['pid'])
            b=p.as_dict(['name'])
            c=p.as_dict(['username'])
            d=p.as_dict(['cpu_percent'])
            e=p.as_dict(['status'])
            if num <=9:
                format_this(str(num)+".  | " + "{:<30}".format(b['name'])+ "|{:^10}".format(d['cpu_percent'])+ "|{:^10}".format(a['pid']) + "|{:^10}| ".format(e['status']) + str(c['username']))
            elif num>=10 and num <=99:
                format_this(str(num)+". | "+"{:<30}".format(b['name'])+ "|{:^10}".format(d['cpu_percent'])+ "|{:^10}".format(a['pid']) + "|{:^10}| ".format(e['status']) + str(c['username']))
            elif num > 99:
                format_this(str(num)+".| "+"{:<30}".format(b['name'])+ "|{:^10}".format(d['cpu_percent'])+ "|{:^10}".format(a['pid']) + "|{:^10}| ".format(e['status']) + str(c['username']))
        edge()
    runs()
    Name_List()
    return

def Main():
    name("Task Manager")
    Info_get()
    Process_list()
    return
    
Main()
