#打乱数据顺序，并划分训练集与验证集；使用gen_train_txt3抽取出训练数据的路径，再用此脚本划分训练验证，固化集
import os
from random import shuffle
import argparse

#打乱数据并存入新文件中
def disturbTrain(inputDir,outputDir,name):
    labelNames=[]
    f = open(inputDir + "/" + name, "r")
    lines = f.readlines()  # 将txt每行文件存入lines列表
    shuffle(lines)
    lf = open(outputDir + "/" + name[:-4] + "_disturb" + ".txt", "w")  # 指定路径下创建train.txt文件，如若为w，则新写入的会替换之前已写好的,改为a则将在文本末尾追加末尾
    lf.writelines(lines) #文本读出的再写入
    f.close()
    lf.close()

#截取数据，划分训练集与验证集,与partial固化数据集
def divideTrain(inputDir,outputDir,trainName,parimgN,testNum):
    f = open(inputDir + "/" +trainName, "r")
    f1 = open(outputDir + "/" + "divTest" + ".txt", "w")
    f2 = open(outputDir + "/" + "divTrain" + ".txt", "a+")
    f3 = open(outputDir + "/" + "parTrain1" + ".txt", "a+")  # 固化1
    f4 = open(outputDir + "/" + "parTrain2" + ".txt", "a+")  # 固化1
    f5 = open(outputDir + "/" + "parTrain3" + ".txt", "a+")  # 固化1
    #划分训练集与验证集
    lines = f.readlines()
    #textNum=len(lines)//10
    for i in range(len(lines)):
        #lines = f.readlines()
        if i <= testNum-1:
            f1.write(lines[i])
        elif i > testNum-1:
            f2.write(lines[i])
    f2 = open(inputDir + "/" + "divTrain.txt", "r+")#a,a+会把指针移到文件结尾，若读则读出为空，用r读
    lines = f2.readlines()
    shuffle(lines)
    partiallines=lines
    partialline=partiallines[:parimgN]
    shuffle(partialline)
    for j in range(parimgN):    #固化集
        f3.write(partialline[j])
    shuffle(partialline)
    for j in range(parimgN):    #固化集
        f4.write(partialline[j])
    shuffle(partialline)
    for j in range(parimgN):  # 固化集
        f5.write(partialline[j])

    f.close()
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
def main(args):

    inputDir = args.input_dir
    testNum = args.testNum

    outputDir = inputDir
    name="train.txt"
    divideName="train_disturb.txt"
    par_imgN=0
    disturbTrain(inputDir,outputDir,name)
    divideTrain(inputDir,outputDir,divideName,par_imgN,testNum)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_dir', default=r'E:\Model_backup\N_ninghedazhong_chongya\yolov5_6.0\20220823_test',
                        help='input train.txt path')
    parser.add_argument('--testNum', type=int, default=10,
                        help='the number of test data')
    parser.add_argument('--par_imgN', type=int, default=0,
                        help='')

    args = parser.parse_args()  
    main(args)
