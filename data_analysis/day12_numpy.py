import numpy as np
import matplotlib.pyplot as plt

# NumPy
# Numerical Python
# 支持大量的维度数组与矩阵运算，也针对数组运算提供大量的数学函数库
# ndarray：N Dimension Array

if __name__ == '__main__':
    # 1维
    # [1, 2, 3]

    # 2维
    # 3 * 4
    # 1 2 3 4
    # 4 5 6 7
    # 8 9 10 11
    a = [
            [1, 2, 3],
            [2, 3, 4],
            [2, 4, 5]
        ]

    # 3维
    a = [
        [
            [1, 2, 3],
            [2, 3, 4],
            [2, 4, 5]
        ],
        [
            [1, 2, 3],
            [2, 3, 4],
            [2, 4, 5]
        ],
        [
            [1, 2, 3],
            [2, 3, 4],
            [2, 4, 5]
        ]
    ]

    a = np.array([1, 2, 3])
    print(type(a))
    print(a)
    print()

    a = np.array([[1, 2, 3], [4, 5, 6]], dtype=np.int8)
    print(type(a))
    print(a)
    print()


    # 属性
    print(a.ndim)
    print(a.shape)
    print(a.size)
    print(a.dtype)

    # cat = plt.imread('../resources/cat.jpg')
    # plt.imshow(a)
    # plt.show()

    # R(0-255)  G(0-255)  B(0-255)
    # print(type(cat))
    # print(cat.ndim)
    # print(cat.shape)
    # print(cat.size)
    # print(cat)


    # 数据类型
    # int8, int16, int32, int64 四种数据类型可以使用字符串 'i1', 'i2','i4','i8' 代替
    dt = np.dtype('i8')
    print(type(dt))
    print(dt)

    dt = np.dtype([('age', 'i4')])
    a = np.array([1, 2, 3], dtype=dt)
    print(a['age'])

    dt = np.dtype([('name', 'S20'), ('age', 'i4'), ('xxx', 'i1')])
    a = np.array([('aaa', 20, 1), ('bbb', 21, 2), ('ccc', 22,3)], dtype=dt)
    print(a)
    print(a[0])
    print(a['name'])


    # 内置创建的方法
    # 1、np.zeros()
    a = np.zeros(shape=(2, 3), dtype=np.int8)
    print(a)

    # 2、np.ones()
    a = np.ones(shape=(2, 3), dtype=np.int8)
    print(a)

    # 3、np.full()
    a = np.full(fill_value=7, shape=(3, 2), dtype=np.int8)
    print(a)

    # 4、np.eye() 对角矩阵；k: 移动对角线
    a = np.eye(4, dtype=np.int8)
    print(a)
    a = np.eye(4, k=1, dtype=np.int8)
    print(a)

    # 5、等差数列
    # np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
    a = np.linspace(0, 100, dtype=np.int8, endpoint=False, retstep=True)
    print(a)
    print()

    # 6、np.random.randint()
    a = np.random.randint(0, 10, size=(3, 2), dtype=np.int8)
    print(a)

    # 7、np.random.random()
    a = np.random.random(size=(3, 2))
    print(a)

    # 8、np.random.rand()
    a = np.random.rand(2, 3)
    print(a)
    print()

    # 9、np.arange(0, 10)
    a = np.arange(0, 10, 2)  # range(0, 10)
    print(a)

    # 10、np.random.randn(n, m, ...)，创建一个服从 标准正态分布 的多维数组
    # 11、np.random.normal(loc=0.0, scale=1.0, size=None)，创建一个服从 正态分布 的多维数组


    # 索引操作 index
    a = np.array([[1, 2, 3], [4, 5, 6]])
    print(a)
    print()

    print(a[0])
    print(a[1][2], a[-1][-1])
    print(a[1, 2], a[-1, -1])
    print()

    a = np.random.randint(10, size=(2, 3, 4))
    print(a)
    print()

    print(a[0])
    print(a[0][1][-2])
    print()

    a[0][1][-2] = -1
    print(a)

    a[0][1] = [-1, -1, -1, -1]
    print(a)

    a[0][1] = 100
    print(a)


    # 切片操作 slice
    # 1 2 3
    # 4 5 6
    # 7 8 9
    a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(a[:1, ])
    print(a[:, :1])
    print(a[:, ::-1])

    # 单独取某些行
    print(a[[0, 2]])

    # 单独取某些行列
    print(a[:, [0, 2]])
    print()

    print(a[[0, 2], [0, 2]])

    b = a[[0, 2]]
    print(b[:, [0, 2]])


    # 图像处理
    cat = plt.imread('../resources/cat.jpg')
    # plt.imshow(cat)
    # plt.show()

    # 上下翻转
    plt.imshow(cat[::-1, :])
    plt.show()

    # 左右翻转
    plt.imshow(cat[::, ::-1])
    plt.show()

    # RGB ——> BGR
    plt.imshow(cat[:, :, ::-1])
    plt.show()

    # 马赛克：间隔选取像素点，使精度变小
    plt.imshow(cat[::200, ::200])
    plt.show()
