
# from __future__ ... 必须放在顶行, 不然报错;
from __future__ import annotations
from typing import  Protocol
from typing import Any, TypeVar

T = TypeVar("T", covariant=True)


class Operation(Protocol[T]):
    def __call__(self, *args, **kwargs) -> T:
        pass


def sumint(*, x:Any, y:Any) -> str:
    return f"{x} + {y} = {x+y}"


def greet(*, name:Any = "World") -> str:
    return f"Hello {name}"


def apply_operation(operation: Operation[str], **kwargs:Any) -> str:
    return operation(**kwargs)


if __name__ == '__main__':
    print(apply_operation(sumint, x=2, y=2))
    print(apply_operation(greet, name='Stack'))
