class B(Exception):
    print("exception occurred")


b= B
try:
    raise b
except B:
    pass
