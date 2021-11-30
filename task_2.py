def deg_to_dm(deg):
    d = int(deg)
    m = float((deg - d) * 60)

    while d > 360:
        d -= 360
    while d < 0:
        d += 360

    coef = (d / 180)

    if coef > 1:
        coef += -2

    return f'{abs(d)}^{round(abs(m), 5)}\'{"E" if -0.5 < coef <= 0.5 else "W"}'
