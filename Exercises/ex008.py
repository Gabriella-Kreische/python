n = float(input('Type a number in meter: '))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000
print('{} meters(m) is equal to:\n{} Kilometer(km),\n{} Hectometer(hm),\n{} Dekameter(dam),\n{} Decimeter(dm)\n{} Centimeter(cm)\n{} Millimeter(mm)!'.format(n, km, hm, dam, dm, cm, mm))
