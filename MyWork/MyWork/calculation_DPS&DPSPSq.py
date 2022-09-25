def get_int(str=""):
    ret = input(str)
    if ret == "":
        return 1
    else:
        return float(ret)

while True:
    damag = get_int("damag>")
    damag_interval = get_int("damag_interval>")
    size = get_int("size>")
    duration = get_int("duration>")
    number = get_int("number>")
    explosion_radius = get_int("explosion_radius>")
    cooldown = get_int("cooldown>")

    damag = damag*number

    dps = damag/(damag_interval)

    dps = dps*duration/cooldown

    dpspsq = dps*size*explosion_radius

    print("dps:>" + str(dps))
    print("dpspsq:>" + str(dpspsq))
    input()