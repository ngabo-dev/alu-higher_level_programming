def raise_exception_msg(message=""):
    try:
        raise NameError(message)
    except NameError:
        print(message)
