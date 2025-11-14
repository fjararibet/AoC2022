import sys


class File():
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Dir():
    def __init__(self, name, files, children, parent):
        self.name = name
        self.files = files
        self.children = children
        self.parent = parent

    def find_child(self, child_name):
        if child_name == "..":
            return self.parent
        for c in self.children:
            if c.name == child_name:
                return c

    def get_size(self):
        size = 0
        for f in self.files:
            size += f.size
        for c in self.children:
            size += c.get_size()
        return size

    def __str__(self):
        s = f"dir {self.name}\n"
        for f in self.files:
            s += f"  {f.size} {f.name}\n"
        for c in self.children:
            s += f"  {c}"
        return s


input = open(sys.argv[1]).read().rstrip()
root = Dir("/", [], [], None)
curr = root
for line in input.split("\n")[1:]:
    if line[0] == '$':
        cli = line.split()
        command = cli[1]
        if command == "cd":
            cd_to = line[2]
            curr = curr.find_child(cd_to)
            print(cd_to)
    elif line.startswith("dir"):
        name = line.split()[1]
        curr.children.append(Dir(name, [], [], curr))
    else:
        file_line = line.split()
        size = int(file_line[0])
        name = file_line[1]
        curr.files.append(File(name=name, size=size))
print(root)


def answer(dir, ans):
    if not dir.children:
        return ans
