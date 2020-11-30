from random import  randint
class Random9Num:
    """
    产生9个随机数,返回字符串
    """
    def returnNum(self):
        num=''
        for i in range(9):
            num=num+str(randint(1,9))
        return  num
if __name__=="__main__":
    print(Random9Num().returnNum())
