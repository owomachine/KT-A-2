fn2testgirdi = ["The little boy ran farther than his friends . He played the best of any player ."]
fn2testparam = ["er.", "an."]

for x in fn2testgirdi:
    y = x.split()

for ara in fn2testparam:
    aram = list(ara)
    for nokta in aram:
        if nokta == ".":
            for kelim in y:
                if kelim == ".":
                    pass
                else:
                    if ara[0:2] == kelim[-2:]:
                        print(kelim)
