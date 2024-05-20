import os

path = r'C:\Users\User\Desktop\Laba9'
def ob(path,l=1):
    
print(os.listdir(path))
for i in os.listdir(path):
    print(i,type(i),path+'\\'+i,os.path.isfile(path+'\\'+i))
