class LoopInfo(object):

    def __init__(self, index, current, previous, next_item, is_last):
        self.current = current
        self.previous = previous
        self.next = next_item
        self.index = index
        self.is_first = self.index == 0
        self.is_last = is_last


def loop_helper(iterable, previous_default=None):
    iterator = iter(iterable)
    index = 0
    previous = previous_default
    is_last = False
    try:
        current = iterator.next()
        while True:
            try:
                next_item = iterator.next()
                yield (current, LoopInfo(index, current, previous, next_item, is_last))
                previous = current
                current = next_item
                index = index + 1
            except StopIteration:
                is_last = True
                next_item = None
                yield (current, LoopInfo(index, current, previous, next_item, is_last))
                break
    except StopIteration:
        pass
