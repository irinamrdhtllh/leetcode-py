def predictPartyVictory(senate: str) -> str:
    r_queue = []
    d_queue = []

    for i, s in enumerate(senate):
        if s == "R":
            r_queue.append(i)
        else:
            d_queue.append(i)

    while r_queue and d_queue:
        r_i = r_queue.pop(0)
        d_i = d_queue.pop(0)

        if r_i < d_i:
            r_queue.append(r_i + len(senate))
        else:
            d_queue.append(d_i + len(senate))

    if r_queue:
        return "Radiant"
    else:
        return "Dire"
