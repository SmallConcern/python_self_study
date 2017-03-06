
def get_knight_phone_graph():
    return {1:[6,8],
            2:[7,9],
            3:[4,8],
            4:[0,3,9],
            5:[],
            6:[0,1,7],
            7:[2,6],
            8:[1,3],
            9:[2,4],
            0:[4,6]}

def get_phone_numbers(graph, start, moves, memo):
    if (start, moves) in memo:
        return memo[(start, moves)]
    if moves == 0:
        return 1
    numbers = 0
    for knight_move in graph[start]:
        numbers += get_phone_numbers(graph, knight_move, moves - 1, memo)
    memo[(start, moves)] = numbers
    return numbers