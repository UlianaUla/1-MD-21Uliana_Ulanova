md=("Уланова","Казиев","Гор","Абдунумонов","Лашкова","Куськова","Золотов","Насулина","Ермолаев","Андрей")
cd=("Иванов","Нептунов","Юпитерович","Солнцев","Лунашева","Сатурнов","Яблоков","Орлова","Воронов","Иванов")
sc=md[:5]+cd[5:]
dl=len(sc)
sc=sorted(sc)
name="Иванов"
if name in sc:
    print("Фамилия Иванов входит в состав кортежа")
else:
    print("Фамилия Иванов не входит в кортеж")
k=sc.count('Иванов')
print("Список группы MD-",md,"Список группы-", cd, "Команда-", sc, "Сколько раз встречается фамилия Иванов")