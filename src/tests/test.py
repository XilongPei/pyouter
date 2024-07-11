from typing import Any
from pyouter.app import App
from pyouter.router import Router
from pyouter.oh_my_zsh.install import install as omz
from pyouter.fish.install import install as fish
from pyouter.bash.install import install as bash


def hello(config, options):
    print("hello")

class Hello:
    def __init__(self) -> None:
        pass 
        
    def __call__(self, config, options) -> Any:
        self.config = config
        self.options = options
        self.inner()
    
    def inner(self):
        print("hello class")
    

def runner():
    '''
    示例:
        App.use 方法必须传入一个router，router内部可以嵌套子router，配置了后，路由从一级节点开始层层路由
    
    用例: 
        * python test.py test.hello
        * python test.py test.hello_class
    '''
    app = App()
    app.use(
        router=Router(
            test=Router(
                hello=hello,
                hello_class=Hello()
            )
        )
    )
    app.run()
    
if __name__=="__main__":
    runner()