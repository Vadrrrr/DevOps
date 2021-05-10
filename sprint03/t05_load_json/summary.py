import collections
import json


def summary(filename, summarize_by):
    with open(filename, 'r') as f:
        res = json.load(f)

    counter = collections.Counter()

    for i in res:
        try:
            counter.update({i[summarize_by]})
        except KeyError:
            counter.update({None})
        except TypeError:
            counter.update({'unhashable'})

    result = dict(sorted(counter.items(), key=lambda x: x[1], reverse=True))

    return result

