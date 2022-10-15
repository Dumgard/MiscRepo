from collections import defaultdict


def _id_to_group_encode_v1(_id: int):
    return sum(map(int, list(str(_id))))


def _id_to_group_encode_v2(_id: int):
    res = 0
    while _id > 0:
        res += _id % 10
        _id = _id // 10
    return res


def group_distribution_v2(n_customers: int,
                          n_first_id: int = 0,
                          ) -> list[float]:
    """
        This function calculates distribution of people among the groups
    in case numeration starts from n_first_id and goes to (n_customers + n_first_id - 1)

    :param n_customers:     Total number of people that should be distributed
    :param n_first_id:      Starting point of numeration, 0 by default
                                (it provides solution for both tasks then/)
    :return:                List, where List[I] is a fraction that group I makes
                                up of the total number of customers
    """

    ans = [0] * (len(str(n_customers)) * 9 + 1)

    for i in map(_id_to_group_encode_v2, range(n_first_id, n_customers + n_first_id)):
        ans[i] += 1

    while ans[-1] == 0:
        ans.pop()

    return ans


def group_distribution_v1(n_customers: int,
                          n_first_id: int = 0,
                          ) -> list[float]:
    """
        This function calculates distribution of people among the groups
    in case numeration starts from n_first_id and goes to (n_customers + n_first_id - 1)

    :param n_customers:     Total number of people that should be distributed
    :param n_first_id:      Starting point of numeration, 0 by default
                                (it provides solution for both tasks then/)
    :return:                List, where List[I] is a fraction that group I makes
                                up of the total number of customers
    """

    d = defaultdict(int)

    for i in range(n_first_id, n_customers + n_first_id):
        d[_id_to_group_encode_v2(i)] += 1

    ans = [0] * (max(d.keys()) + 1)

    for k, v in d.items():
        ans[k] = v / n_customers

    return ans


if __name__ == '__main__':
    from timeit import timeit

    N_trials = 10 ** 2
    print(timeit('group_distribution_v1(100000)',
                 setup='from __main__ import group_distribution_v1', number=N_trials))
    print(timeit('group_distribution_v2(100000)',
                 setup='from __main__ import group_distribution_v2', number=N_trials))
    # print(group_distribution_v1(100000))
    # print(group_distribution_v1(100000, 1000))
