from load import idioms
from random import choice


used_idioms = []
idioms = [idiom['word'] for idiom in idioms if len(idiom['word'])==4]
def get_clue():
    global used_idioms
    qualified_idioms = idioms
    if len(used_idioms) != 0:
        qualified_idioms = [idiom for idiom in idioms if idiom[0]==used_idioms[-1][-1] if idiom not in used_idioms]
        if len(qualified_idioms) == 0:
            print('AI无法找到答案,你赢了！')
            quit()
    clue = choice(qualified_idioms)
    solutions = [idiom for idiom in idioms if idiom[0] == clue[-1] if idiom not in used_idioms]
    while len(solutions) == 0:
        clue = choice(qualified_idioms)
        solutions = [idiom for idiom in idioms if idiom[0] == clue[-1] if idiom not in used_idioms]
    used_idioms.append(clue)
    return clue, solutions
 
clue, solutions = get_clue()
print(solutions)
answer = input(' -> '.join(used_idioms)+ ' -> ?')
while True:
    if answer in solutions:
        print('恭喜你答对了！')
        used_idioms.append(answer)
        clue, solutions = get_clue()
        print(solutions)
        answer = input(' -> '.join(used_idioms)+ ' -> ?')
        print(' -> '.join(used_idioms))
        answer = input(f'{clue}?')
    else:
        if answer not in solutions:
            print('答案不正确！')
        if answer in used_idioms:
            print('你重复了！')
        print('再试一次吧！')
        answer = input(' -> '.join(used_idioms)+ ' -> ?')