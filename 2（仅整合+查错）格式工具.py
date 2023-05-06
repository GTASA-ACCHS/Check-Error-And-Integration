import os
import codecs
import webbrowser

try:
    import chardet
except ImportError:
    print("chardet模块没有安装，你可以使用pip install chardet或者conda install chardet命令进行安装。")

# 将源文件转换成UTF-8格式
def convert_file_encoding_to_utf8(src_path):
    # 检测源文件编码
    with open(src_path, 'rb') as f:
        rawdata = f.read()
    encoding = chardet.detect(rawdata)['encoding']
    
    # 如果编码不是UTF-8，进行转换
    if encoding and encoding.lower() != 'utf-8':
        with codecs.open(src_path, 'r', encoding=encoding) as f:
            text = f.read()
        with codecs.open(src_path, 'w', encoding='utf-8') as f:
            f.write(text)

# 复制源文件到目标文件中
def copy_lines(src_path, dst_file):
    with codecs.open(src_path, 'r', encoding='utf-8') as f:
        for line in f:
            # 将原始文本中的每一行添加到目标文件中，并去掉末尾的换行符
            dst_file.write(line.strip() + '\n')

# 检查gtavc文本文件中的错误，并将错误信息输出到crash dump文件
def check_gtavc_file(file_path, crash_dump_file):
    # 用一个集合来存储重复的文本行和上一行
    dup_lines = set()
    last_line = None
    with codecs.open(file_path, 'r', encoding='utf-8') as f:
        for i, line in enumerate(f):
            # 跳过空行和注释
            if not line.strip():
                continue
            if line.startswith('//'):
                continue
            # 以下修改
            if ';' in line:
                continue
            if line.strip().startswith('//'):
                continue
            # 修改结束
            # 检查等号前面的空格
            if '=' in line:
                equal_idx = line.index('=')
                if line[equal_idx-1] == ' ':
                    # 如果等号前有空格，输出错误信息
                    crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (=号出现了空格啊！！！！！！)\n')
            
            # 检查同一行上的多个等号
            if line.count('=') > 1:
                crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (有两个=号啊！！！！！！，如果前缀是FEI_BTD或FEI_BTU的话就没啥事了)\n')
            
            # 检查制表符缩进
            if '\t' in line:
                crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (有Tab的缩进符啊！！！！！！)\n')
            
            # 检查等号前面是否有内容
            if not line.split('=')[0].strip():
                crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (符号=前面缺少内容啊！！！！！！)\n')
            
            # 添加判断，如果行中没有[或]或=三个之一，就将本行输出至CrashDump.txt
            if '[' not in line and ']' not in line and '=' not in line:
                crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (行中没有[或]或=三个之一)\n')

            # 检查符号=前的内容是否与之前的某行完全匹配
            if last_line is not None and last_line.strip().startswith(line.split('=')[0].strip()):
                crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (符号=前的内容与之前某一行完全匹配啊！！！！！！)\n')
            last_line = line
            
            # 检查重复行（完全相同）
            if line == last_line:
                dup_lines.add(last_line)
                dup_lines.add(line)
            # 检查重复行（符号=前的内容相同）
            elif last_line is not None and last_line.split('=')[0] == line.split('=')[0]:
                dup_lines.add(last_line)
                dup_lines.add(line)
            last_line = line

# 主函数
def main():
    # 定义源文件、目标文件和crash dump文件的名称
    gtavc_file = 'gtavc.txt'
    crash_dump_file = 'CrashDump.txt'
    # 获取当前文件夹中所有的文本文件
    file_list = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt') and f != gtavc_file and f != crash_dump_file and f != 'CHARACTERS.txt']
    # 将所有文本文件的编码格式转换为utf-8
    for file_path in file_list:
        convert_file_encoding_to_utf8(file_path)
    
    # 将所有文本文件的内容复制到gtavc文本文件中
    with open(gtavc_file, 'w', encoding='utf-8') as dst_file:
        for file_path in file_list:
            copy_lines(file_path, dst_file)

    # 检查所有文本文件中的错误并输出到crash dump文件中
    with open(crash_dump_file, 'w', encoding='utf-8') as dump_file:
        for file_path in file_list:
            check_gtavc_file(file_path, dump_file)
            
        # 在CrashDump.txt文件的末尾添加结束语
        dump_file.write('\n此工具Lzh10_慕黑倾情制作，感谢您使用英文文本整合工具。\nGithub: https://github.com/lzh102938\n哔哩哔哩: https://space.bilibili.com/1657432204\n个人Blog: https://lzh10.netlify.app\n个人小游戏: https://lzhgames.netlify.app\nQQ: 235810290\n邮箱: lzh1029384756@outlook.com※235810290@qq.com\n回首向来萧瑟处，归去，也无风雨也无晴。')
    
    # 打开生成的CrashDump.txt文件
    webbrowser.open(crash_dump_file)

if __name__ == '__main__':
    main()
