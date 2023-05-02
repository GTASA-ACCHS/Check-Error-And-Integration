# 导入os模块
import os

# 复制源文件到目标文件中
def copy_lines(src_path, dst_file):
    with open(src_path, 'r') as f:
        for line in f:
            # 将原始文本中的每一行添加到目标文件中，并去掉末尾的换行符
            dst_file.write(line.strip() + '\n')

# 检查gtavc文本文件中的错误，并将错误信息输出到crash dump文件
def check_gtavc_file(file_path, crash_dump_file):
    # 用一个集合来存储重复的文本行和上一行
    dup_lines = set()
    last_line = None
    with open(file_path, 'r') as f:
        for i, line in enumerate(f):
            # 跳过空行和注释
            if not line.strip() or line.startswith('//'):
                continue
            
            # 检查等号前面的空格
            if '=' in line:
                equal_idx = line.index('=')
                if line[equal_idx-1] == ' ':
                    # 如果等号前有空格，输出错误信息
                    crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (=号出现了空格啊！！！！！！)\n')
            
            # 检查重复行
            if last_line is not None and last_line.split('=')[0] == line.split('=')[0]:
                dup_lines.add(last_line)
                dup_lines.add(line)
            last_line = line
            
            # 检查同一行上的多个等号
            if line.count('=') > 1:
                crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (有两个=号啊！！！！！！，如果前缀是FEI_BTD或FEI_BTU的话就没啥事了)\n')
            
            # 检查制表符缩进
            if '\t' in line:
                crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (有Tab的缩进符啊！！！！！！)\n')
            
            # 检查等号前面是否有内容
            if not line.split('=')[0].strip():
                crash_dump_file.write(f'{file_path}:{i+1}: {line.strip()} (符号=前面缺少内容啊！！！！！！)\n')
    
    # 输出重复行
    for dup_line in sorted(list(dup_lines)):
        crash_dump_file.write(f'{file_path}:n/a: {dup_line.strip()} (有几个相同前缀了啊！！！！！！)\n')

# 主函数
def main():
    # 定义源文件、目标文件和crash dump文件的名称
    gtavc_file = 'gtavc.txt'
    crash_dump_file = 'CrashDump.txt'
    # 获取当前文件夹中所有的文本文件
    file_list = [f for f in os.listdir('.') if os.path.isfile(f) and f.endswith('.txt')]
    # 将所有文本文件的内容复制到gtavc文本文件中
    with open(gtavc_file, 'w') as dst_file:
        for file_path in file_list:
            # 忽略gtavc.txt和CrashDump.txt文件
            if file_path == gtavc_file or file_path == crash_dump_file:
                continue
            copy_lines(file_path, dst_file)

    # 检查所有文本文件中的错误并输出到crash dump文件中
    with open(crash_dump_file, 'w') as dump_file:
        for file_path in file_list:
            # 忽略gtavc.txt和CrashDump.txt文件
            if file_path == gtavc_file or file_path == crash_dump_file:
                continue
            check_gtavc_file(file_path, dump_file)
            
        # 在CrashDump.txt文件的末尾添加结束语
        dump_file.write('\n此工具Lzh10_慕黑倾情制作，感谢您使用英文文本整合工具。\nGithub: https://github.com/lzh102938\n哔哩哔哩: https://space.bilibili.com/1657432204\n个人Blog: https://lzh10.netlify.app\n个人小游戏: https://lzhgames.netlify.app\nQQ: 235810290\n邮箱: lzh1029384756@outlook.com※235810290@qq.com\n回首向来萧瑟处，归去，也无风雨也无晴。')

if __name__ == '__main__':
    main()
