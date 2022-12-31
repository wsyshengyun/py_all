# coding:utf8
from abc import abstractmethod


class Spec:
    def and_spec(self, candidate):
        raise NotImplementedError()

    def or_spec(self, candidate):
        raise NotImplementedError()

    def not_spec(self, candidate):
        raise NotImplementedError()

    @abstractmethod
    def is_satisfied_by(self, candidate):
        pass


class CompositeSpec(Spec):
    def and_spec(self, candidate):
        return AndSpec(self, candidate)

    def not_spec(self, candidate):
        return NotSpec(self, candidate)

    def or_spec(self, candidate):
        return OrSpec(self, candidate)


class AndSpec(CompositeSpec):
    def __init__(self, one, other):
        self.one: Spec = one
        self.other: Spec = other

    def is_satisfied_by(self, candidate):
        return bool(
            self.one.is_satisfied_by(candidate)
            and self.other.is_satisfied_by(candidate)
        )


class OrSpec(CompositeSpec):
    def __init__(self, one, other):
        self.one: Spec = one
        self.other: Spec = other

    def is_satisfied_by(self, candidate):
        return bool(
            self.one.is_satisfied_by(candidate)
            or self.other.is_satisfied_by(candidate)
        )


class NotSpec(CompositeSpec):
    def __init__(self, wrapped):
        self.wrapped: Spec = wrapped

    def is_satisfied_by(self, candidate):
        return bool(not
                    self.wrapped.is_satisfied_by(candidate)
                    )


class User:
    def __init__(self, super_user=False):
        """ """
        self.super_user = super_user


class UserSpec(CompositeSpec):
    def is_satisfied_by(self, candidate):
        return isinstance(candidate, User)


class SuperUserSpec(CompositeSpec):
    def is_satisfied_by(self, candidate):
        return getattr(candidate, "super_user", False)


if __name__ == '__main__':
    andrey = User()
    ivan = User(super_user=True)
    vasilly = 'not User instance'
    root_spec = UserSpec().and_spec(SuperUserSpec())
    print(root_spec)
    print(root_spec.is_satisfied_by(andrey))  # False
    print(root_spec.is_satisfied_by(ivan))  # True
    print(root_spec.is_satisfied_by(vasilly))  # False
