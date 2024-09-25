import random

class Boomber:
    def __init__(self):
        self.boom_rate = 0

    def step(self):
        self.boom_rate += 1
        
        random_number = random.randint(1, 100)
        if random_number <= self.boom_rate:
            return True
        return False

# 创建初始的 boombers 列表
initial_boombers = [Boomber() for _ in range(1_000_000)]

# 使用 initial_boombers 的副本进行迭代
current_boombers = initial_boombers[:]

for i in range(100):
    # 计算这一轮未爆炸的 boombers
    unexploded_boombers = [boomber for boomber in current_boombers if not boomber.step()]
    
    # 计算爆炸的数量
    exploded_count = len(current_boombers) - len(unexploded_boombers)
    print(f'第{i+1}秒爆炸数: {exploded_count}')
    
    # 更新当前的 boombers 列表为未爆炸的 boombers
    current_boombers = unexploded_boombers