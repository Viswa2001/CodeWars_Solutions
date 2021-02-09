def warn_the_sheep(queue):
    length_queue=len(queue)
    enemy = 'wolf'
    wolf_index = queue.index(enemy)
    if wolf_index == (len(queue)-1):
        return "Pls go away and stop eating my sheep"
    else:
        return f'Oi! Sheep number {len(queue)-(wolf_index+1)}! You are about to be eaten by a wolf!'