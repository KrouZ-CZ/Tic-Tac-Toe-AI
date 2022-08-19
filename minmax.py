from check import check_win

class AI:
    def get(area: list) -> int:
        if not 0 in area: return None
        c = AI.check_one_win(area)
        if c != None:
            return c
        a = AI.start_rec(area, -1)
        for i in a:
            if a[i] == 10:
                return i
        for i in a:
            return i

    def check_one_win(area: list) -> int:
        for i in AI.get_zero(area):
            area[i] = -1
            a = check_win(area)
            if a == -1:
                return i
            else:
                area[i] = 0

    def start_rec(area: list, w: int) -> dict:
        mass = {}
        for i in AI.get_zero(area):
            area[i] = w
            a = check_win(area)
            if a == None:
                we = AI.start_rec(area, w*-1)
                if w*-1 == -1:
                    for it in we:
                        mass[i] = -10
                        if we[it] == 10:
                            mass[i] = 10
                            break
                elif w*-1 == 1:
                    for it in we:
                        mass[i] = 10
                        if we[it] == -10:
                            mass[i] = -10
                            break
                else:
                    mass[i] = 0
            elif a == 1:
                mass[i] = -10
            elif a == -1:
                mass[i] = 10
            elif a == 0:
                mass[i] = 0
            area[i] = 0
        return mass

    def get_zero(area: list) -> list:
        t = []
        for i, item in enumerate(area):
            if item == 0:
                t.append(i)
        return t