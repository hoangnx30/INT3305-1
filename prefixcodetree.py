class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.symbol = None

    def insert_left(self):
        if not self.left:
            self.left = Node()

    def insert_right(self):
        if not self.right:
            self.right = Node()

    # def __str__(self, level=0):
    #     ret = repr(self.symbol) + "\n"
    #     if self.left:
    #         ret += "\t" * level + "|-- " + self.left.__str__(level + 1)
    #     if self.right:
    #         ret += "\t" * level + "└── " + self.right.__str__(level + 1)
    #     return ret
    #
    # def __repr__(self):
    #     return '<tree node representation>'


class PrefixCodeTree:
    def __init__(self):
        self.root = Node()

    def insert(self, codeword, symbol):
        node = self.root
        for bit in codeword:
            if bit == 0:
                node.insert_left()
                node = node.left
            if bit == 1:
                node.insert_right()
                node = node.right
        node.symbol = symbol

    def decode(self, encode_data, length):
        res = ''
        node = self.root
        bits = ''
        for c in encode_data:
            bits += bin(c)[2:].zfill(8)
        bits = bits[:length]
        for bit in bits:
            if bit == '0':
                node = node.left
            elif bit == '1':
                node = node.right
            if node.symbol:
                res += node.symbol
                node = self.root
        return res


def main():
    codebook = {
        'x1': [0],
        'x2': [1, 0, 0],
        'x3': [1, 0, 1],
        'x4': [1, 1]
    }

    code_tree = PrefixCodeTree()

    for symbol in codebook:
        code_tree.insert(codebook[symbol], symbol)

    encode_data = b'\xd2\x9f\x20'
    length = 21
    print(code_tree.decode(encode_data, length))


main()
