"This module contains exception classes."

class InvalidInput(Exception):
    """Raised when input is invalid.
        
    Method:
        - __init__: used in initialization
    """

    def __init__(self):
        super().__init__(self)

class Quit(Exception):
    """Raised when terminal input is '%quit'.
  
    Method:
        - __init__: used in initialization
    """

    def __init__(self):
        super().__init__(self)
     

class SkipTurn(Exception):
    """Raised when terminal input is '%skip'.
   
    Method:
        - __init__: used in initialization
    """

    def __init__(self):
        super().__init__(self)


class HelpRequired(Exception):
    """Raised when terminal input is '%help'.
  
    Method:
        - __init__: used in initialization
    """

    def __init__(self):
        super().__init__(self)
