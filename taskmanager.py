import psutil
import psutil, datetime
import time
_times=psutil.cpu_times()

# Левый формат.
def format_left(*argc):
    print("|\t{:<90}|".format(*argc))
    return

# Заголовок
def name(*argc):
    print("|{:■^90}".format(*argc),end=" ⊟ ⊡ ⊠ |\n")
    return

def Info_get():
    def format_right(*argc):
        print("|\t{:>90}|".format(*argc))
        return
        # Имя пользователя
    def user_get(): 
        user=psutil.users()
        for i in user:
            format_right("User name :    "+i[0])
            n=int(i[3])
        time_format = time.strftime("%H:%M:%S", time.gmtime(n)) 
        format_right("On system :"+time_format)

    # Данные процессора  
    def CPU_show():    
        a=psutil.cpu_percent(interval=1)
        while a!=None:
            z=None
            if a <=10.0:
                z='[|.........]'
                break
            elif a<=20.0:
                z='[||........]'
                break
            elif a<=30.0:
                z='[|||.......]'
                break
            elif a<=40.0:
                z='[||||......]'
                break
            elif a<=50.0:
                z='[|||||.....]'
                break   
            elif a<=60.0:
                z='[||||||....]'
                break
            elif a<=70.0:
                z='[|||||||...]'
                break 
            elif a<=80.0:
                z='[||||||||..]'
                break 
            elif a<=90.0:
                z='[|||||||||.]'
                break
            elif a<=100.0:
                z='[||||||||||]'
                break                     
        format_left("CPU        Load   : "+str(a)+"% "+ z)
        format_left('CPU time   User   : '+ ("{:.1f}".format(_times[0])) + " Min.")
        format_left('           System : '+ ("{:.1f}".format(_times[1]/60)) + " Min.")
        format_left("") # space

    # Оперативная память
    def memory():
        mem=psutil.virtual_memory()
        percent=mem[2]
        while percent!=None:
            a=None
            if percent <= 10:
                a=('[|.........]')
                break
            elif percent <=20:
                a=('[||........]')
                break
            elif percent <=30:
                a=('[|||.......]')
                break
            elif percent <=40:
                a=('[||||......]')
                break
            elif percent <=50:
                a=('[|||||.....]')
                break
            elif percent <=60:
                a=('[||||||....]')
                break
            elif percent <=70:
                a=('[|||||||...]')
                break
            elif percent <=80:
                a=('[||||||||..]')
                break
            elif percent <=90:
                a=('[|||||||||.]')
                break
            elif percent <=100:
                a=('[|||||||||!]')
                break
        format_left('Ram        Load   : ' + str(percent)+"% "+ a )
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
        format_this((" №  | "+"{:<30}".format("Name")+ "|{:^10}".format("%")+ "|{:^10}".format("PID") + "|{:^10}| ".format("Status")+str("User")))
        edge()
    #Список прилож.
        num=0    
        for p in psutil.process_iter():
            num+=1
            a=p.as_dict(['pid'])
            b=p.as_dict(['name'])
            c=p.as_dict(['username'])
            d=p.as_dict(['cpu_percent'])
            e=p.as_dict(['status'])
            if num <=9:
                format_this(str(num)+".  | "+"{:<30}".format(b['name'])+ "|{:^10}".format(d['cpu_percent'])+ "|{:^10}".format(a['pid']) + "|{:^10}| ".format(e['status'])+str(c['username']))
            elif num>=10 and num <=99:
                format_this(str(num)+". | "+"{:<30}".format(b['name'])+ "|{:^10}".format(d['cpu_percent'])+ "|{:^10}".format(a['pid']) + "|{:^10}| ".format(e['status'])+str(c['username']))
            elif num > 99:
                format_this(str(num)+".| "+"{:<30}".format(b['name'])+ "|{:^10}".format(d['cpu_percent'])+ "|{:^10}".format(a['pid']) + "|{:^10}| ".format(e['status'])+str(c['username']))
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
