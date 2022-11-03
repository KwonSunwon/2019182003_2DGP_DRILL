# Game World
# layer 0: background
# layer 1: player, ball
# layer 2: foreground
objects = [[], [], []]

def add_object(o, depth):
    objects[depth].append(o)

def add_objects(ol, depth):
    objects[depth] += ol
    
def remove_object(o):
    for layer in objects:
        if o in layer:
            layer.remove(o)
            del o
            return
    raise ValueError('Object not in world')

def all_objects():
    for layer in objects:
        for o in layer:
            yield o
            
def clear():
    for o in all_objects():
        del o
    for layer in objects:
        layer.clear()