# customize string representation of objects


class myColor():
    def __init__(self):
        self.red = 50
        self.green = 75
        self.blue = 100

    # use getattr to dynamically return a value
    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        elif attr == 'hexcolor':
            return "#{0:02x}{1:02x}{2:02x}".format(
                self.red, self.green, self.blue
            )
        else:
            raise AttributeError

    # use setattr to dynamically return a value
    def __setattr__(self, attr, val):
        if attr == 'rgbcolor':
            self.red = val[0]
            self.green = val[1]
            self.blue = val[2]
        else:
            super().__setattr__(attr, val)

    def __dir__(self):
        return ("red", "green", "blue", "rgbcolor", "hexcolor")


def main():
    cls1 = myColor()

    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    cls1.rgbcolor = (125, 200, 86)

    print(cls1.rgbcolor)
    print(cls1.hexcolor)

    print(cls1.red)

    print(dir(cls1))

if __name__ == "__main__":
    main()
