import os
import shutil
import datetime
class categorize_folder():
    def __init__(self,source,aim):
        self.source = source
        self.aim = aim
        self.file_name = os.path.split(source)
        if (os.path.isdir(self.source) and os.path.isdir(self.aim)) == False:
            raise Exception("lütfen geçerli bir dizin giriniz")
        return self.file_islem()
    def file_islem(self):
        self.datalist = []
        def inner_file_islem(adress):
            filelist = os.listdir(adress)
            for x in filelist:
                adresslist = adress+"\\"+x
                if not os.path.isdir(adresslist):
                    self.datalist.append(adresslist)
                else:
                    inner_file_islem(adresslist)
        inner_file_islem(self.source)
    def control_error(self,folder_control,sorted_name):
        try:
            os.makedirs(folder_control)
        except FileExistsError:
            print(f'SOURCE folder have already sorted {sorted_name}')
    def my_extension(self,symb="\\"):
        folder_name = self.aim +"\\"+self.file_name[1]+" file sorted extension"
        self.control_error(folder_name,"extension")
        def inner_extension_islem():
            for x in self.datalist:
                dizin,dosya = os.path.split(x)
                dosya,file_uzantı = os.path.splitext(dosya)
                aimfile = folder_name+symb+file_uzantı+" extension folder"
                if os.path.isdir(aimfile):
                    shutil.copy(x,aimfile)
                else:
                    os.makedirs(aimfile)
                    shutil.copy(x,aimfile )
        return inner_extension_islem()
    def time_operation(self):
        timeinfo = []
        for y in self.datalist:
            value = datetime.datetime.fromtimestamp(os.stat(y).st_mtime)
            dicti = {0:"%Y",1:"%B",3:"%d"}
            folder_time = []
            for x in dicti:
                timedata =datetime.datetime.strftime(value,dicti[x])
                folder_time.append(timedata)
            timeinfo.append(folder_time)
        return timeinfo
    def time_categorize(self,symb = "\\"):
        folder_name =self.aim +"\\"+"categorized time information"
        self.control_error(folder_name,"time ")
        timeinfo = self.time_operation()
        for x in range(0,len(timeinfo)):
            folder = self.aim +"\\"+"categorized time information"
            for y in range(0,3):
                folder = folder+"\\"+timeinfo[x][y]
                if os.path.isdir(folder):
                    continue
                else:
                    os.makedirs(folder)
            shutil.copy(self.datalist[x],folder)
    def time_sorting(self,symb ="\\"):#GG-AA-YY
        file_name = self.aim +"\\"+"categorized GG-AA-YY"
        self.control_error(file_name,"GG-AA-YY")
        time1info = self.time_operation()
        for k in range(0,len(self.datalist)):
            GGAAYY = ""
            time1info[k].reverse() #GG-AA-YY çeviriyoruz
            for t in time1info[k]:
                GGAAYY = GGAAYY+f' {t}'
            if os.path.isdir(file_name+"\\"+GGAAYY):
                shutil.copy(self.datalist[k],file_name+"\\"+GGAAYY)
            else:
                os.makedirs(file_name+"\\"+GGAAYY)
                shutil.copy(self.datalist[k],file_name+"\\"+GGAAYY)
source = "Please input the directory of the folder you want to classify"
aimfolder = "Please input the location of the folder where the classification will be made."
entry = categorize_folder(source,aimfolder)
