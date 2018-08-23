from collections import deque


class Tree(object):
    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        if self.root is not None:
            return self.root.value
        else:
            return None

    def print_tree(self):
        """

        :return:
        """
        root = self.root
        level_list = []     # to store each level
        my_deque = deque()  # create a deque to store the node
        value_list = []     # store the value of node
        if root is None:
            return "The tree is empty!"
        else:
            my_deque.append(root)
            current_level = 1
            next_level = 0
            while current_level != 0:
                node = my_deque.popleft()
                if node is not None:
                    value_list.append(node.value)

                    for child in [node.left, node.right]:
                        if child is not None:
                            my_deque.append(child)
                        else:
                            my_deque.append(None)
                else:
                    my_deque.append(None)
                    my_deque.append(None)
                    value_list.append('|')

                current_level -= 1
                next_level += 2

                if current_level == 0:
                    level_list.append(value_list)
                    value_list = []
                    current_level = next_level
                    next_level = 0
                    if all(item is None for item in my_deque):
                        break

        height = len(level_list)
        new_list = []
        count = 2 ** (height - 1) - 1
        space_list = ["|" for i in range(count)]

        new_list.append(space_list + level_list[0] + space_list)
        for i in range(1, height):
            temp_list = []
            for j in level_list[i][:-1]:
                temp_list.append(j)
                temp_list = temp_list + ["|" for k in range(count)]
            temp_list.append(level_list[i][-1])
            count = int(count / 2)
            new_list.append(temp_list)
        final_list = []
        for i in new_list:
            if len(i) != 2 ** height - 1:
                num = int((2 ** height - 1 - len(i)) / 2)
                space_list = ["|" for k in range(num)]
                i = space_list + i + space_list
            final_list.append(i)
        return final_list


class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right
