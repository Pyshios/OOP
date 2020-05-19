import datetime

class wrstu:
#Log class
    def __init__(self ,file_name):
        self.dt = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
        self.file_name = file_name
        self.alist = list()

    def create(self , msg):
        with open(self.file_name ,'w') as my_file:
            for i in msg:
                my_file.write(i)
                my_file.write(',')

class wrsto(wrstu):



    def log(self , msg):
        with open(self.file_name, 'w') as my_file:
            for i in msg:
                my_file.write(i)
                my_file.write('\n')
                my_file.write(self.dt)




a = wrstu('myfile.txt')
b = wrsto('mysecondfile.csv')

a.create('aaaa')
b.log(['a' , 'e' , 't', 'r'])
