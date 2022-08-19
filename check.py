def check_win(area):
    if area[0] + area[1] + area[2] == 3: return 1
    if area[3] + area[4] + area[5] == 3: return 1
    if area[6] + area[7] + area[8] == 3: return 1

    if area[0] + area[3] + area[6] == 3: return 1
    if area[1] + area[4] + area[7] == 3: return 1
    if area[2] + area[5] + area[8] == 3: return 1

    if area[0] + area[4] + area[8] == 3: return 1
    if area[2] + area[4] + area[6] == 3: return 1


    if area[0] + area[1] + area[2] == -3: return -1
    if area[3] + area[4] + area[5] == -3: return -1
    if area[6] + area[7] + area[8] == -3: return -1

    if area[0] + area[3] + area[6] == -3: return -1
    if area[1] + area[4] + area[7] == -3: return -1
    if area[2] + area[5] + area[8] == -3: return -1

    if area[0] + area[4] + area[8] == -3: return -1
    if area[2] + area[4] + area[6] == -3: return -1

    if not 0 in area: return 0

    return None