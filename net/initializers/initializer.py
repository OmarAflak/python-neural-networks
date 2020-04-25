class Initializer:
    def __init__(self):
        self.layer_sizes = None
        self.index = None

    def set_layer_sizes(self, layer_sizes):
        self.layer_sizes = layer_sizes

    def set_layer_index(self, index):
        self.index = index

    def get_io(self):
        return self.layer_sizes[self.index]

    def get(self, *shape):
        pass