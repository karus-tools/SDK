import reconsleuth

client = reconsleuth.Client()

minecraft_profile = client.minecraft_lookup(username="rosathorn")
print(minecraft_profile)

print("------------------------------------------------------------")

roblox_profile = client.roblox_lookup(username="Mexican_adrian16")
print(roblox_profile)

print("------------------------------------------------------------")

twitch_profile = client.twitch_lookup(username="linaiz")
print(twitch_profile)
