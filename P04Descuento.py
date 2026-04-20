#Icker Alba
es_cliente_frecuente = input("¿Eres cliente frecuente? (si/no): ").strip().lower() == "si"
monto_compra = float(input("Ingresa el monto de tu compra: $"))
tiene_cupon = input("¿Tienes cupón de descuento? (si/no): ").strip().lower() == "si"
 
descuento = 0
 
# AND: cliente frecuente Y compra mayor a $500 → 20% descuento
if es_cliente_frecuente and monto_compra > 500:
    descuento = 0.20
    print("Descuento del 20%: cliente frecuente con compra mayor a $500.")
 
# OR: cliente frecuente O tiene cupón → 10% descuento (si no aplica el anterior)
elif es_cliente_frecuente or tiene_cupon:
    descuento = 0.10
    print("Descuento del 10%: cliente frecuente o cupón válido.")
 
# NOT: no es cliente frecuente y no tiene cupón
elif not es_cliente_frecuente and not tiene_cupon:
    print("Sin descuento: no eres cliente frecuente y no tienes cupón.")
 
monto_descuento = monto_compra * descuento
monto_final = monto_compra - monto_descuento
 
print(f"\nMonto original:  ${monto_compra:.2f}")
print(f"Descuento:       ${monto_descuento:.2f}")
print(f"Total a pagar:   ${monto_final:.2f}")
