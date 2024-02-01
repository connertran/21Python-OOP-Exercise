"""Python serial number generator."""


class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        """Declaring the start variable"""
        self.start = start-1 #when generate the number will added by one
        self.reset_value = start-1
    def __repr__(self):
        """Show representation."""
        return f"<SerialGenerator start={self.start} next={self.start+1}>"
    def reset(self):
        """resetting to the original value"""
        self.start = self.reset_value
    def generate(self):
        """Every serial number is unique, by adding one"""
        self.start +=1
        return self.start
    
