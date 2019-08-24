import random
import string

def GetRandomString(len,NumberOfOutputs):

    if len <= 0:
        print('文字列は1文字以上設定してください。Error len <= 0')
        return
    
    if NumberOfOutputs <= 0:
        print('出力個数は1個以上設定してください。Error NumberOfOutputs <= 0')
        return

    sPopulation = string.digits+string.ascii_lowercase + string.ascii_uppercase+'!"#$%&()'

    for i in range(NumberOfOutputs):
        sRandom = ''.join(random.sample(sPopulation,len))
        print(sRandom)
    
    return

if __name__ == '__main__':

    GetRandomString(0,1)
    GetRandomString(1,0)
    GetRandomString(10,3)
    