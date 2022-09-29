# -*- encoding: utf-8 -*-
#针对yolov5生成yolo训练集
import os
import argparse

class Gen_train_txt():
    def __init__(self):
        self.input_dir = r''
        self.output_dir = r''
    def run_gen_train_txt(self):
        with open(self.output_dir, 'a') as f:
            for single_path in self.input_dir:
                for root, dirs, files in os.walk(single_path):
                    for name in files:
                        if '.jpg' in name:
                            f.write(os.path.join(root, name) + '\n')
        print("生成成功")
    

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='')
    parser.add_argument('--input_dir',nargs='+', default=[r'E:\projectdata\C_chongya\classification_data\kl'],
                        help='dateset absolute path')
    parser.add_argument('--output_dir', type=str, default=r'E:\Model_backup\N_ninghedazhong_chongya\yolov5_6.0\20220823_test',
                        help='the txt file of dateset absolute path')

    args = parser.parse_args()      

    input_dir = args.input_dir
    output_dir = args.output_dir + '/train.txt'
    gen_train_txt = Gen_train_txt()
    gen_train_txt.input_dir = input_dir
    gen_train_txt.output_dir = output_dir
    gen_train_txt.run_gen_train_txt()




