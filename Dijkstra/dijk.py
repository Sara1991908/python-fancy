import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import seaborn



class Node:
    def __init__(self, x, y, cost, parent_index):
        self.x = x  # index of grid
        self.y = y  # index of grid
        self.cost = cost  # g(n)
        self.parent_index = parent_index  # index of previous Node

    def __str__(self):
        return str(self.x) + "," + str(self.y) + "," + str(
            self.cost) + "," + str(self.parent_index)




# main函数
def main():

    # 设置四堵墙
    x1 = np.arange(-10,100,1)
    y1 = np.ones(110)*100
    x2 = np.arange(-10, 100, 1)
    y2 = np.ones(110) * (-10)
    y3 = np.arange(-10, 100, 1)
    x3 = np.ones(110) * 100
    y4 = np.arange(-10, 100, 1)
    x4 = np.ones(110) * (-10)
    plt.plot(x1, y1, label='list1',color='chocolate',marker = "x",markersize=2)  # 添加linestyle设置线条类型
    plt.plot(x2, y2, label='list1', color='chocolate', marker="x", markersize=2)
    plt.plot(x3, y3, label='list1', color='chocolate', marker="x", markersize=2)
    plt.plot(x4, y4, label='list1', color='chocolate', marker="x", markersize=2)
    plt.plot(-5,90,color='red', marker="p", markersize=2)
    plt.plot(10,5,color='blue', marker="p", markersize=2)

    # 设置障碍物
    ox1 = np.arange(-10, 30, 1)
    oy1 = np.ones(40) * 80
    ox2 = np.arange(10, 70, 1)
    oy2 = np.ones(60) * 30
    ox3 = np.arange(20, 50, 1)
    oy3 = np.ones(30) * 9
    oy4 = np.arange(-10, 20, 1)
    ox4 = np.ones(30) * 90
    oy5 = np.arange(45, 60, 1)
    ox5 = np.ones(15) * 62
    ox6 = np.arange(20, 80, 1)
    oy6 = np.ones(60) * 80
    plt.plot(ox1, oy1, label='list1', color='chocolate', marker="x", markersize=2)
    plt.plot(ox2, oy2, label='list1', color='chocolate', marker="x", markersize=2)
    plt.plot(ox3, oy3, label='list1', color='chocolate', marker="x", markersize=2)
    plt.plot(ox4, oy4, label='list1', color='chocolate', marker="x", markersize=2)
    plt.plot(ox5, oy5, label='list1', color='chocolate', marker="x", markersize=2)
    plt.plot(ox6, oy6, label='list1', color='chocolate', marker="x", markersize=2)
    plt.show()

 # 起点和终点
    start = [-2,90]
    goal = [10,5]
    grid_size = 2 #障碍物大小
    robot_radius = 1 #机器人半径

    open_list = []
    open_list.append(start)
     #遍历八个方向






# def djsk(obstaclerange,start,end):
#     # open_stack和closestack

if __name__ == '__main__':
   main()



