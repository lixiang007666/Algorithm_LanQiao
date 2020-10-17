
#若a,b是整数,且gcd(a,b)=d，那么对于任意的整数x,y,ax+by都一定是d的倍数，!!!!!!!!特别地，一定存在整数x,y，使ax+by=d成立。!!!!!!
#针对任意给出的x，y，z，可以假设用x与y分别往一个很大的容器里倒水和倒出水，那么如果z=mx+ny，找到合适的正整数m与n即为所求，其中m与n为负时，往外倒水，为正时，往里倒水。

#若z<=x+y且z%d==0,说明存在m、n使得最终剩余水为z。根据贝祖等式，d为x、y的最大公约数。

class Solution(object):
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        tmp = self.gcd(x, y)
        if z == 0: return True
        if z > x + y: return False
        return z % tmp == 0

    def gcd(self, x, y):
        if y == 0: return x
        return self.gcd(y, x % y)

if __name__=="__main__":
    t1=Solution()
    print(t1.canMeasureWater(3,5,4))