from src.maotek import Hello
from src import maotek

print(maotek.__version__)
h = Hello('mao')
print(h.greet())
print("new feat")