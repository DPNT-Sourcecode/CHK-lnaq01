

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name: str) -> str:
    # Need feedback from "User" Server, before I can continue with implementation
    # I'm going to run "deploy" intentionally, to get a penalty and feedback
    # All we know at this point is we need to return a string containing a message
    # ___ I have now run "deploy" and seen that I need to return "Hello, World!"
    # R2 now complete for this challenge
    return "Hello, "+friend_name+"!"
