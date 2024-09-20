import random


def roll(total=3, unluckies=1):
    """
    total: 总共的号码数量，默认为3
    unluckies: 不幸运的号码数量，默认为1
    """
    if total < 3 :
        raise ValueError("总数量必须至少为3")
    if total - unluckies < 2:
        raise ValueError("总数量和不幸运数量之差必须大于2")
    # 创建一个包含1到total数字的列表，随机选择一个获胜号码
    numbers = list(range(1, total + 1))
    winning_number = random.choice(numbers)
    
    # 用户随机选择一个号码
    user_number = random.choice(numbers)
    numbers.remove(user_number)

    # 从剩下的号码中随机选择不幸运的未中奖号码，并移除它
    for _ in range(unluckies):
        unlucky_number = random.choice([num for num in numbers if num != winning_number])
        numbers.remove(unlucky_number)

    # 判断坚持原选择是否胜利
    insist_win = (winning_number == user_number)
    
    # 判断改变选择后是否胜利
    user_number = random.choice(numbers)
    change_win = (winning_number == user_number)
    print(f'随机选择: {winning_number}, 用户选择: {user_number}, 保持原选择是否胜利: {insist_win}, 改变选择后是否胜利: {change_win}')
    return {'insist': insist_win, 'change': change_win}

# 测试函数
if __name__ == "__main__":
    results = {'insist': 0, 'change': 0}
    trials = 100_000
    for _ in range(trials):
        print(f'【次数: {_+1:}/{trials:}】 ', end='')
        result = roll(total=10, unluckies=8)
        if result['insist']:
            results['insist'] += 1
        if result['change']:
            results['change'] += 1

    print(f"坚持原选择胜利次数: {results['insist']} ({results['insist']/trials*100:.2f}%)")
    print(f"改变选择后胜利次数: {results['change']} ({results['change']/trials*100:.2f}%)")