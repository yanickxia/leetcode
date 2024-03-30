# 暴力解法：这题有个简单解，如果执行完指令之后，和我们出发点的方向一样，那就回不来的。
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        if not instructions:
            return False
        pos = {}
        x, y, direct = 0, 0, "RIGHT"
        run_step = 100 * 100
        while run_step > 0:
            ins = instructions[0]

            pos_str = str(x) + "," + str(y)
            if pos_str not in pos:
                pos[pos_str] = set()

            if instructions in pos[pos_str]:
                return True

            pos[pos_str].add(instructions)

            if ins == "G":
                if direct == "RIGHT":
                    y += 1
                if direct == "LEFT":
                    y -= 1
                if direct == "UP":
                    x -= 1
                if direct == "DOWN":
                    x += 1
            elif ins == 'L':
                if direct == "RIGHT":
                    direct = "UP"
                elif direct == "LEFT":
                    direct = "DOWN"
                elif direct == "UP":
                    direct = "LEFT"
                elif direct == "DOWN":
                    direct = "RIGHT"
            else:
                if direct == "RIGHT":
                    direct = "DOWN"
                elif direct == "LEFT":
                    direct = "UP"
                elif direct == "UP":
                    direct = "RIGHT"
                elif direct == "DOWN":
                    direct = "LEFT"
            instructions = instructions[1:] + instructions[0]
            run_step -= 1

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.isRobotBounded(
        "LLGRGRRGGRGGRLGRGGRRLLRGGLRLLRGGLRLGLLRRGGRGLGRGGRLLLGGGRGRLGLLLRRLGGRRLGLGGRGLRLRRRLLGRGLRGLRRGLGRG"))
    print(s.isRobotBounded("GGLLGG"))
    print(s.isRobotBounded("GLGLGGLGL") == False)
    print(s.isRobotBounded("GG") == False)
    print(s.isRobotBounded("GL") == True)
