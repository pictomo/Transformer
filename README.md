***Not related to [Transformer in the NLP or AI field](https://arxiv.org/abs/1706.03762).***

# Transformer
Transformer is a script, which rewrites the self into another form like the Transformers(of the story).
A code that itself goes back and forth between two (or more) states each time it is executed.

Go to [transformer dir](./transformer/) and try to execute [main.py](./transformer/main.py).
You will see that the script file itself is rewritten every time you run it.

[mini-transformer](./mini-transformer/) is a more compact implementation of [transformer](./transformer/).<br>
[self-reconstructor](./self-reconstructor/) is simpler and rewrite itself as itself.<br>
[ultraman-tiga](./ultraman-tiga/) is the same as [transformer](./transformer/), but it transitions between 3 states.<br>
[counter](./counter/) remembers the number of times it has been executed.

It is inspired by [Quine (self replicating code)](https://en.wikipedia.org/wiki/Quine_(computing)).<br>
[Here is my Quine try.](https://github.com/pictomo/quine-python)

# Turing Quine
It turns out that Quine can print itself, and even print slight modifications of itself.
So I wondered if this might be Turing complete.

Go to [turing-quine dir](./turing-quine/) and try to execute [main.py](./turing-quine/main.py).
A Turing machine is defined within the code.
You will see that the state of the Turing machine changes, each time it is executed.<br>
[main.py](./turing-quine/main.py) prints the status as it runs.
By running [repeater.py](./turing-quine/repeater.py), it will automatically run [main.py](./turing-quine/main.py) repeatedly, so it will be easier to see that main.py behaves as a Turing machine.