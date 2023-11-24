def read_file(filename=""):
    """
    Reads a text file and prints its content to stdout.

    Parameters:
    - filename (str): The name of the text file to be read. Defaults to an empty string.

    Returns:
    - None
    """
    if not filename:
        print("Error: Please provide a filename.")
        return

    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print(content)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")
