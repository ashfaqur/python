KM_TO_MILE = 0.621371

kms = input('How many miles did you run today?\n')
kms = float(kms)
mileage = kms * KM_TO_MILE
mileage = round(mileage, 2)
print(f'Your {round(kms,1)} km run was {mileage} mi')
