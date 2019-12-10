import dejavu

if __name__ == '__main__':
    config = {"database": {
        "host":"127.0.0.1",
        "user":"local",
        "database":"dejavu"
    }}
    djv = dejavu.Dejavu(config)
    djv.fingerprint_file("mp3/planet_money_ad.mp3", group_id=0)
