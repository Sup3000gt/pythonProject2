class Solution(object):
    def calculate(self, s):
        res, num, sign = 0, 0, 1    # result 用于储存结果变量 , num用于储存数字变量, sign用来储存符号变量
        stack = []                  # 创建一个空栈
        for c in s:
            if c.isdigit():         # 首先检查元素是否为数字, 如果是就把元素保存到num里面
                num = 10 * num + int(c)
            elif c == "+" or c == "-":  # 如果遇到的符号是 + 或者 - 就把 num变量 储存到res变量里面
                res += sign * num       # 然后重置 num 和 sign的变量
                num = 0
                sign = 1 if c == "+" else -1    #如果是加号 sign为1 如果是减号 sign为 -1
            elif c == "(":              # 如果遇到左括号,就把res结果变量和符号都加入栈中,以准备处理括号内的表达式
                stack.append(res)
                stack.append(sign)
                res = 0                 # 然后重置 res变量 和 sign变量 因为 括号里面的res 和sign 都是local的
                sign = 1
            elif c == ")":              # 如果遇到右括号,则将当前数字 num 加入到结果res中
                res += sign * num       # 重置 num 变量为0
                num = 0                 # 这时候我们的栈中有之前append进去过的sign和res
                res *= stack.pop()      # 第一次pop弹出sign 用这个sign 乘以括号里面的结果, 设置为新结果
                res += stack.pop()      # 然后 再弹出括号外面保存的 总结果，然后把新结果加入到总结果中
        res += sign * num   # 然后再把这个数字储存到 res结果变量里面
        return res                      # 最后返回总计算结果

