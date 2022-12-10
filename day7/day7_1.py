lines = open('day7/input.txt', 'r').read().split('\n')

root = []
current_dir = ['root']

class Dir:
    def __init__(self, name, parent=None):
        self.name = name
        self.files = {}
        self.dirs = {}
        self.parent = parent
    
    def mkdir(self, name):
        if name not in self.dirs:
            self.dirs[name] = Dir(name, self)
        return self.dirs[name]
    
    def append(self, filename, filesize):
        if filename not in self.files:
            self.files[filename] = filesize

root = Dir('/')
current_dir = root

for line in lines:
    match line.split(' '):
        case ['$', 'ls']:
            pass
        case ['$', 'cd', '/']:
            current_dir = root
        case ['$', 'cd', '..']:
            current_dir = current_dir.parent
            if current_dir == None:
                raise Exception('Cannot cd .. from root')
        case ['$', 'cd', dir]:
            current_dir = current_dir.mkdir(dir)
        case ['dir', dir]:
            current_dir.mkdir(dir)
        case [filesize, filename]:
            filesize = int(filesize)
            current_dir.append(filename, filesize)
        case _:
            raise Exception('Invalid command')

sizes = {}
less_than_100000 = 0
def calc_size(dir):
    global less_than_100000
    size = 0
    for filename, filesize in dir.files.items():
        size += filesize
    for dirname, subdir in dir.dirs.items():
        size += calc_size(subdir)
    sizes[dir.name] = size
    if size <= 100000:
        less_than_100000 += size
    return size

calc_size(root)
print(sizes)
print(less_than_100000)
