police_car = 'パトカー'
taxi = 'タクシー'
mix_string_list = [p + t for p, t in zip(police_car, taxi)]
mix_string = ''.join(mix_string_list)
print(mix_string)