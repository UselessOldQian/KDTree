class KD_node:
    def __init__(self, point=None, split=None, LL=None, RR=None):
        """
        point:data point
        split:devide dimension
        LL, RR:the left child node and right child node
        """
        self.point = point
        self.split = split
        self.left = LL
        self.right = RR
        self.isvisited = 0

    def __str__(self):
        return 'point:{} split:{} left:{} right:{}'.format(self.point,
                                                           self.split,
                                                           self.left.point,
                                                           self.right.point)

    def initialize(self):
        self.isvisited = 0
        if self.left:
            self.left.initialize()
        if self.right:
            self.right.initialize()