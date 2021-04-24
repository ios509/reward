'''  End of service reward   '''
import datetime

class  eosr():



    def __init__(self, name, joining_date, salary):
        self.name = name
        self.joining_date = datetime.datetime( int(joining_date[0:4]) , int(joining_date[5]) , int(joining_date[-1]) )
        self.salary = salary

    def reward(self):
        dn = datetime.datetime.now()
        a = str(dn - self.joining_date)
        b = ''
        for i in a:
            b += i
            if i.isspace() == True:
                break

        x = int(b) / 365

        if 1 < int(x) <= 3 :
            g = int(b) / 30
            gg = (0.10 * self.salary) * g
            return f'He mr {self.name}, You worked with us {int(x)} years \nyou will git {int(gg)}$ end of service Benefits'
        elif int(x) > 4 :
            g = int(b) / 30
            gg = (0.25 * self.salary) * g
            return f'He mr {self.name}, You worked with us {int(x)} years \nyou will git {int(gg)}$ end of service Benefits'
        else:
            g = int(b) / 30
            gg = (0.05 * self.salary) * g
            return f'He mr {self.name}, You worked with us {int(x)} years \nyou will git {int(gg)}$ end of service Benefits'





p = eosr('nasser','2015-5-12',5000)
print(p.reward())
''' 
He mr nasser, You worked with us 5 years 
you will git 91000$ end of service Benefits
'''   