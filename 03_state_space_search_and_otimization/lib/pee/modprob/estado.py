
class Estado:

    def __eq__(self, obj):
        return hash(self) == hash(obj)

    def __hash__(self):
        raise NotImplementedError()
    