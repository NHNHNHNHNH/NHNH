#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：卢锐
日期：2021/6/3
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果


    pass #编写执行代码,代码完成后将pass删除


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果

    pass #编写执行代码,代码完成后将pass删除


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    pass #根据以上提示编写执行代码，代码完成后删除掉pass


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
rpsls(choice_name)
import random

# 电脑人随机出拳
computer = random.randint(0, 4)

user = int(input('请输入你的选择：0.石头，1.史波克，2.纸，3.蜥蜴，4.剪刀'))

if computer == 0:
    computer = '石头'
elif computer == 1:
    computer = '史波克'
elif computer == 2:
    computer = '纸'
elif computer == 3:
    computer = '蜥蜴'
elif computer == 4:
    computer = '剪刀'
else:
    print('Error: No Correct Name')

if user == 0:
    user = '石头'
elif user == 1:
    user = '史波克'
elif user == 2:
    user = '纸'
elif user == 3:
    user = '蜥蜴'
else:
    user = '剪刀'
print('电脑人出的是:%s,用户出的是:%s' % (computer, user))
if user == computer:
    print('平局')
elif((user == 3 or 4 and computer == 0)
   or (user == 0 or 4 and computer == 1)
   or (user == 1 or 0 and computer == 2)
   or (user == 1 or 2 and computer == 3)
   or (user == 3 or 2 and computer == 4)):
   print('机器赢了')
if ((user == 0 and computer == 3 or 4)
   or (user == 1 and computer == 0 or 4)
   or (user == 2 and computer == 1 or 0)
   or (user == 3 and computer == 1 or 2)
   or (user == 4 and computer == 3 or 2)):
   print('你赢了')
