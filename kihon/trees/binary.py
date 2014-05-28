MAX_SIZE = 1000


class BinaryTree:
    def __init__(self, *args, **kwargs):
        self.parent = kwargs.get('parent', None)
        self.left = kwargs.get('left', None)
        self.right = kwargs.get('right', None)
        self.key = kwargs.get('key', None)
        self.value = kwargs.get('value', None)

    def insert_node(self, node):
        if node.key == self.key:
            self.value = node.value
        elif node.key < self.key:
            if self.left:
                self.left.insert_node(node)
            else:
                node.parent = self
                self.left = node
        else:
            if self.right:
                self.right.insert_node(node)
            else:
                node.parent = self
                self.right = node

    def insert(self, key, value=None):
        self.insert_node(BinaryTree(key=key, value=value))

    def extend(self, data):
        for item in data:
            if isinstance(item, tuple):
                self.insert(*item)
            else:
                self.insert(item)

    def search(self, key):
        result = self.search_node(key)
        return result.value \
            if result else None

    def search_node(self, key):
        if key == self.key:
            return self
        elif key < self.key:
            return self.left.search_node(key) \
                if self.left else None
        else:
            return self.right.search_node(key) \
                if self.right else None

    def delete(self, key):
        node = self.search_node(key)

        if node:
            node.delete_node()

    def delete_node(self):

        if self.left:
            import ipdb; ipdb.set_trace()
            # Takes the max from the left child
            node = self.left.maximum

            # It could have minor child (left) itself
            aux_left_child = node.left

            # Replaces this node with the left maximum
            self._replace_node(node)

            # Re-insert maximum children if it is necessary
            if aux_left_child:
                node.left.insert_node(aux_left_child)

        elif self.right:
            # Takes the min from the right child
            node = self.right.minimum

            # It could have a major child (right) itself
            aux_right_child = node.right

            # Re-insert maximum children is it was necessary
            self._replace_node(node)

            # Re-insert minimum children if it is necessary
            if aux_right_child:
                node.right.insert_node(aux_right_child)

        else:
            # Deleting a leaf
            self._replace_node(None)

    def _replace_node(self, node):

        # Replace node children with mines
        if node:

            if node != self.left:
                node.left = self.left

            if node != self.right:
                node.right = self.right

        # Tell parent to change child
        if self.parent:
            if self.parent.left == self:
                self.parent.left = node
            else:
                self.parent.right = node


    @property
    def minimum(self):
        return self.left.minimum if self.left else self

    @property
    def maximum(self):
        return self.right.maximum if self.right else self

    def __str__(self):
        return '({key}, {value}) -> ({left}, {right})'.format(key=self.key,
                                                              value=self.value,
                                                              left=str(self.left) if self.left else '-',
                                                              right=str(self.right) if self.right else '-')


