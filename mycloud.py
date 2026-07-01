# Mycloud
import requests
import json
class Song:
    def __init__(self, title: str, artist: str):
        self.title = title
        self.artist = artist
    def info(self, number: int):
        print(f"{number}. 🎵 {self.title}  —  🎤 {self.artist}")
library = [
    Song("teenpopken+Yung Trappa-VERSUS BATTLE vs feduk", "Teenpoken x Yung Trappa"),
    Song("tuborosho + dxnkwer + xsonsss - клубняк2010 P R I M E", "xsonsss X dxnkwer x tuborosho "),
    Song("yung trappa + xsonsss - dope & dr*gs", "xsonsss x Yung Trappa"),
    Song("xsonsss + timmitheboy + кузнецкий сквад - рич форевер 2 & stereo love", "xsonsss x Кузнецкий Сквад"),
    Song("Laughin To The Bank", "Chief Keef"),
    Song("yung trappa + xsonsss - dope prime hardstyle mix", "xsonsss x Yung Trappa"),
    Song("SupaPlaya x Голосование remix (prod.reflexseeya)", "rflxs x Yung Trappa"),
    Song("I Don't Like (Ft. Lil Reese)", "Chief Keef x Lil Reese"),
    Song("Love Sosa", "Chief Keef"),
    Song("Ирак", "Boulevard Depo x avoloj4"),
    Song("Нету меня x I Don't Like mashup", "Yung Trappa x Chief Keef"),
    Song("yung trappa + xsonsss - нету меня & ты так красива", "Yung Trappa x xsonsss"),
    Song("FREDO SANTANA - ON THAT Ft CHIEF KEEF", "Fredo Santana x Chief Keef"),
    Song("SIL-A x Yung Trappa - Молодые Боссы", "SIL-A x Yung Trappa"),
    Song("MORGENSHTERN, Lil Pump - WATAFAK", "Morgenshtern x Lil Pump"),
    Song("SIL-A + Yung Trappa + PRADABLADER- Давай кинем барыгу", "SIL-A x Yung Trappa x PRADABLADER"),
    Song("D Rose", "Lil Pump"),
    Song("yung trappa + xsonsss - dope & kazantip 2007", "Yung Trappa x xsonsss"),
    Song("ESSKEETIT", "Lil Pump"),
    Song("Я РОНЯЮ ЗАПАД", "FACE"),
    Song("Yung Trappa + PRADABLADER - ФЕЙКАМ ЗАВАЛИТЬ...!!!", "Yung Trappa x PRADABLADER")
]
playlists = {}
try:
    with open("library.json", "r") as file:
        data = json.load(file)
    library = []
    for item in data:
        library.append(Song(item["title"], item["artist"]))
except:
    pass
while True: 
    print("1. Показать все песни")
    print("2. Добавить песню")
    print("3. Найти песню")
    print("4. Создать плейлист")
    print("5. Добавить песню в плейлист")
    print("6. Показать плейлист")
    print("7. Показать текст песни")
    print("8. Сохранить")
    print("9. Выход")
    choice = input("Выберите пункт: ")
    if choice == "1":
        print("🎧═══════ МОЙ ПЛЕЙЛИСТ ═══════🎧")
        number = 1
        for song in library:
            song.info(number)
            number = number + 1
    elif choice == "2":
        new_title = input("Введите название новой песни: ")
        new_artist = input("Введите имя нового исполнителя: ")
        library.append(Song(new_title, new_artist))
        print("Песня добавлена! 🎶")        
    elif choice == "3":
        query = input("Что ищем? ")
        found = False
        number = 1
        for song in library:
            if query in song.title or query in song.artist:
                song.info(number)
                number = number + 1
                found = True
        if found == False:
            print("Ничего не найдено ")
    elif choice == "4":
        playlist_name = input("Введите название нового плейлиста: ")
        playlists[playlist_name] = []
        print("Плейлист создан!")
    elif choice == "5":
        pl_name = input("В какой плейлист добавляем песню? ")
        if pl_name in playlists:
            number = 1
            for song in library:  
                song.info(number)
                number = number + 1
            song_number = int(input("Введите номер песни, которую хотите добавить в плейлист: "))
            chosen_song = library[song_number - 1]
            playlists[pl_name].append(chosen_song)
        else:
            print("К сожалению, такого плейлиста нет - проверьте правильность написания, или создайте плейлист с таким названием")
    elif choice == "6":
        pl_name = input("Какой плейлист показать? ")
        if pl_name in playlists:
            number = 1 
            for song in playlists[pl_name]:
                song.info(number)
                number = number + 1
        else:
            print("К сожалению, такого плейлиста нет - проверьте правильность написания, или создайте плейлист с таким названием")
    elif choice == "7":
        number = 1
        for song in library:  
            song.info(number)
            number = number + 1
        song_number = int(input("Введите номер песни, текст которой хотите узнать: "))
        chosen_song = library[song_number - 1]
        url = f"https://api.lyrics.ovh/v1/{chosen_song.artist}/{chosen_song.title}"
        try:
            otvet = requests.get(url, timeout=10)
            data = otvet.json()
            if "lyrics" in data:
                print(data["lyrics"])
            else:
                print("Текста данной песни нет")
        except:
            print("Текст не найден или сервис недоступен")
    elif choice == "8":
        data = []
        for song in library:
            data.append({"title": song.title, "artist": song.artist})
        with open("library.json", "w") as file:
            json.dump(data, file)
        print("Сохранено!")
    elif choice == "9":
        break