def slova(slovar)
    new_slovar={value:key for key,value in slovar.items()}
    return dict(sorted(new_slovar.items())

slovar={"cat":"кошка","dog":"собака","home":"дом","mouse":"мышь","to do":"делать","to make":"изготавливать"}
new_slovar=slova(slovar)
print(new_slovar)
