fn1testgirdi = ["You can go faster than 150", "Dikkatli yolculuk yapın"]
fn1testparam = ["fa+", "dik+"]
aranacak = list()
for x in fn1testgirdi:
    y = x.split()
    for z in y:
        aranacak.append(z)

for ara in fn1testparam:
    aram = list(ara)
    for artı in aram:
        if artı == "+":
            for kelim in aranacak:
                if ara[0:2] == kelim[0:2].lower():
                    print(kelim)
