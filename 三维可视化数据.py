import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


if __name__ == "__main__":
    # 创建一个三维绘图工程
    ax = plt.subplot(111, projection='3d')

    with open('datingTestSet.txt') as info:
        for i in info.readlines():
            infos = i.split('\t')
            if infos[3][0] == 'l':
                color = 'r'
            elif infos[3][0] == 's':
                color = 'g'
            else:
                color = 'y'
            ax.scatter(float(infos[0]), float(infos[1]), float(infos[2]), c = color)
            
    # 坐标轴的名称设置和显示我们所绘制的图
    ax.set_zlabel('water')
    ax.set_ylabel('game')
    ax.set_xlabel('travel')
    plt.show()
