import abc


class IPacking(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def pack(self):
        pass


class Wrapper(IPacking):
    def pack(self):
        return "Wrapper"


class Bottle(IPacking):
    def pack(self):
        return "Bottle"


if __name__=='__main__':
    wrapper = Wrapper()
    print(wrapper.pack())



