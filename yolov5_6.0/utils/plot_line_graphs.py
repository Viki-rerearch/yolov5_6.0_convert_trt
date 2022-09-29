import matplotlib.pyplot as plt
import os
import numpy as np

def plot_img(path):
    '''
    本方法严重依赖yolo训练产生的结果文件：results.txt 以及 精度与召回.txt,不要修改文件中内容的形式！！！禁止在该目录下存放其他txt文件，将会导致该脚本无法绘图。
    '''
    os.remove(os.path.join(path, 'unique_classes.txt'))
    for root, dirs, files in os.walk(path):
        for file in files:
            if file[-3:] == 'txt':
                P = []
                total_loss =[]
                R = []
                map5 = []
                map95 = []
                class_dictionary = {}
                with open(os.path.join(root, file), 'r') as f:
                    for line in f.readlines():
                        if line == '\n':
                            continue
                        line = line.split()
                        if file == 'results.txt':
                            total_loss.append(line[5])
                            P.append(line[8])
                            R.append(line[9])
                            map5.append(line[10])
                            map95.append(line[11])
                        else:
                            if line[0] not in class_dictionary:
                                class_dictionary[line[0]] = {'P': [], 'R': [], 'map5': [], 'map95': []}
                            class_dictionary[line[0]]['P'].append(line[3])
                            class_dictionary[line[0]]['R'].append(line[4])
                            class_dictionary[line[0]]['map5'].append(line[5])
                            class_dictionary[line[0]]['map95'].append(line[6])
                    if file == 'results.txt':
                        total_loss = np.array(total_loss, dtype=np.float32)
                        P = np.array(P, dtype=np.float32)
                        R = np.array(R, dtype=np.float32)
                        map5 = np.array(map5, dtype=np.float32)
                        map95 = np.array(map95, dtype=np.float32)
                        plt.figure(figsize=(16, 8))
                        plt.suptitle('Total')
                        plt.subplot(2, 3, 1)
                        plt.ylim(0, 1)
                        plt.title('total_p')
                        plt.plot(P, 'r-')
                        plt.subplot(2, 3, 2)
                        plt.ylim(0, 1)
                        plt.title('total_R')
                        plt.plot(R, 'b-')
                        plt.subplot(2, 3, 3)
                        plt.ylim(0, 1)
                        plt.title('total_map.5')
                        plt.plot(map5, 'g-')
                        plt.subplot(2, 3, 4)
                        plt.ylim(0, 1)
                        plt.title('total_map.95')
                        plt.plot(map95, 'y-')
                        plt.subplot(2, 3, 5)
                        plt.title('total_loss')
                        plt.plot(total_loss,  color = '#87CEFA')
                        plt.subplot(2, 3, 6)
                        plt.ylim(0,1)
                        plt.plot(P, 'r-')
                        plt.plot(R, 'b-')
                        plt.plot(map5, 'g-')
                        plt.plot(map95, 'y-')
                        plt.title('total')
                        # plt.suptitle('Total')
                        plt.savefig(os.path.join(path, 'total_img.png'))
                        # plt.show()
                    else:
                        color = ['r-', 'b-', 'g-', 'y-']
                        for cn in class_dictionary:
                            plt.figure(figsize=(12, 8))
                            plt.suptitle(cn)
                            for i, target in enumerate(class_dictionary[cn]):
                                plt.subplot(2, 2, i+1)
                                plt.title(cn + '_' + target)
                                line_list = np.array(class_dictionary[cn][target], dtype=np.float32)
                                plt.ylim(0, 1)
                                plt.plot(line_list, color[i])
                            plt.savefig(os.path.join(path, cn+'_img.png'))

if __name__ == '__main__':

    plot_img()