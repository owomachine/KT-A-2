fn3testgirdi = ["Python is a programming language that lets you work quickly and integrate systems more effectively"]
fn3testparam = ["a*", "e*"]

for x in fn3testgirdi:
    y = x.split()

for ara in fn3testparam:
    aram = list(ara)
    for yıldız in aram:
        if yıldız == "*":
            for kelim in y:
                kel = list(kelim)
                if kel[0] == aram[0]:
                    pass
                if kel[-1] == aram[0]:
                    pass
                else:
                    if aram[0] in kel:
                        print(kelim)
