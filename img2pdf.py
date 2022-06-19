# -*- coding: utf-8 -*-

from PIL import Image
import sys
import os

docs = """usage:
    python3 img2pdf.py [input_path] [output_path]
    input_path:
        输入图片文件夹的地址.
    output_path:
        输入保存的地址.
    """

if len(sys.argv) == 3:
    input_filename = sys.argv[1]
    output_filename = sys.argv[2]
elif len(sys.argv) == 2:
    if not os.path.exists(os.path.abspath('.')+"/pdf"):
        os.mkdir("pdf")
    input_filename = sys.argv[1]
    output_filename = os.path.abspath('.')+"/pdf"
else:
    if not os.path.exists(os.path.abspath('.')+"/pdf"):
        os.mkdir("pdf")
    output_filename = os.path.abspath('.')+"/pdf"
    input_filename = os.path.abspath('.')

#def img2pdf(input_filename,output_filename):
filedir_list = os.listdir(input_filename+'/')
file_index = 0
for filedir in filedir_list:
    if filedir.find('.') == -1 :
        pdf_name = filedir
        img_list = []
        file_list = os.listdir(input_filename+'/'+filedir)
        #寻找图片并排序
        for img in file_list:
            if img.endswith('.jpg') or img.endswith('.img') or img.endswith('.bmp'):
                img_list.append(img)
        #添加入PDF文件
        pdf_imglist = []
        for i in img_list:
            img = Image.open(input_filename+'/'+filedir+'/'+i)
            if img.mode == "RGBA":
                img = img.convert('RGB')
                pdf_imglist.append(img)
            else:
                pdf_imglist.append(img)
        #保存
        savefile = output_filename +'/'+ pdf_name + '.pdf'
        imgMerge = pdf_imglist.pop(0)
        imgMerge.save(savefile, "PDF", resolution=100.0, save_all=True, append_images=pdf_imglist)
        print("output: ",savefile)