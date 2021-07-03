

# age, weight, height, Genders
male_blood_volume = lambda a,w,h: (1486 * (w**0.425 * h**0.725) * 0.007184) - 825 + 1578 * (w**0.425 * h**0.725 * 0.007184)
female_blood_volume = lambda a,w,h: 1.06 * a + (822 * (w**0.425 * h**0.725 * 0.007184)) + 1395 * (w**0.425 * h**0.725 * 0.007184)

