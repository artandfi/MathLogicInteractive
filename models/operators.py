from operator import not_, or_, and_, eq


def impl(a, b):
    return not a or b


operator_strings = {
    not_: "¬",
    and_: "&",
    or_: "v",
    impl: "->",
    eq: "<->"
}
operator_priority = {
    not_: 1,
    and_: 2,
    or_: 3,
    impl: 4,
    eq: 5
}
arity = {
    not_: 1,
    and_: 2,
    or_: 2,
    impl: 2,
    eq: 2
}
