class Test:
    x = 1
    y = '2'
    z = {3}

    # 非静态方法需要传入一个self,代表当前对象本身
    def test_method(self, arg):
        print('TestMethod!')
        print(arg)
        return 'TestMethod'


class TestExtend(Test):

    # 静态方法不要传入当前对象本身,因为即使没有对象静态方法依然可以调用
    @staticmethod
    def extend_method():
        print("extend_method")
        return 'extend'


test = TestExtend()
print(test.x)
print(test.y)
print(test.z)
result1 = test.test_method('arg')
print(result1)
result2 = TestExtend.extend_method()
print(result2)
