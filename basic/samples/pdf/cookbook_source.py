#!/usr/bin/env python
# -*- encoding: utf-8 -*-
"""
Topic: 处理pdf2txt.py -o pc.txt /home/mango/work/perfect.pdf生成的txt文件
Desc : 最后的结果是我想要的，去除了页头和页脚的部分
"""
import re


def beauty(txt_file):
    with open(txt_file, mode='r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        for line in lines:
            if line.startswith('www.it-ebooks.info'):
                f.seek(f.tell() - 1, 1)
                if f.readline().startswith('Chapter '):
                    # 回退7位
                    f.seek(f.tell() - 7, 1)
                else:
                    f.seek(f.tell() - 5, 1)
            else:
                f.write(line)
        f.truncate()


def beauty2(pre_txt, after_txt):
    with open(pre_txt, mode='r', encoding='utf-8') as f:
        lines = f.readlines()
    result_lines = []
    for i, line in enumerate(lines):
        if line.startswith('www.it-ebooks.info'):
            if result_lines[len(result_lines) - 4].startswith('| '):
                # 删除7
                for k in range(7):
                    result_lines.pop()
            else:
                check_str = result_lines[len(result_lines) - 2].strip()
                if re.match('\d{3}', check_str):
                    # 删除3行
                    for k in range(3):
                        result_lines.pop()
        else:
            result_lines.append(line)

    # 结果写入
    with open(after_txt, mode='w', encoding='utf-8') as f:
        f.writelines(result_lines)


def generate_chapter():
    """
    解析文本文件，生成最终的待翻译文件
    """



if __name__ == '__main__':
    # beauty2('pc_pre.txt', 'pc_after')
    pass
