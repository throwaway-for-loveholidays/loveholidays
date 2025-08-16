import uuid
import random
import string

def generate_visitor_id():
    """
    Generate a random UUID-like string.
    """
    return str(uuid.uuid4())

def generate_query_id():
    """
    Generate a random query_id in format "xxxxx-xxxx-xxxx" where x is alphanumeric
    """
    def generate_alnum_segment(length):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

    return f"{generate_alnum_segment(5)}-{generate_alnum_segment(4)}-{generate_alnum_segment(4)}"