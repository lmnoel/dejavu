import dejavu

if __name__ == '__main__':
    config = {"database": {
        "host":"127.0.0.1",
        "user":"local",
        "database":"dejavu"
    }}
    djv = dejavu.Dejavu(config)
    for i in range(0, 10):

        match = djv.recognize("../../podblocker/chunks_18/chunk_{}.mp3".format(i), group_id=0, known_song_id=0)
    print(match)