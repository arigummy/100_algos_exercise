
class Cach:
    def __init__(self, val=None):
        self._val = val

    def __str__(self):
        return f"Cash: {self._val}"


class LRU_Cach:

    def __init__(self, cap:int=0):

        self._cap = cap
        self._caches  = {}
        self._keys = []


    def get(self, key, default=None):

        if key in self._caches:
            self._keys.remove(key)
            self._keys.insert(0, key)
            return self._caches[key]

        else:
            return default


    def put(self, key, val):

        if self._cap == 0: return

        if key in self._caches:
            self._caches[key] = val
            self._keys.remove(key)
            self._keys.insert(0, key)

        else:
            self._caches[key] = val
            # print(f"keys len: {len(self._keys)}")
            if len(self._keys) >= self._cap:
                # self._keys.remove(key)
            # else:
                del self._caches[self._keys[-1]]
                self._keys.pop()

            self._keys.insert(0, key)


    def __len__(self):
        return self._cap

    # def __contains__(self):

    def __str__(self):
        res = "Cash:\n"
        if self._cap == 0:
            return "Cash is None"
        for key in self._keys:
            res += f"{key}: \"{self._caches[key]}\"\n"
        return res

x = LRU_Cach(3)
x.put(15, "old")
x.put(3, "new")
x.put(1, "anew")
x.put(3, "hah")
# a = [1]
# print(a[-1])

print(x)
