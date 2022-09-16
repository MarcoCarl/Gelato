
from cgi import print_directory


gelato=input('Quanti gusti vuoi? \n')
gelato=int(gelato)
costo=int()
for i in range(gelato):
    gusto=input('Che gusto vuoi tra vanilla, cioccolato e crema \n')
    if gusto=='vanilla':
        costo+=4
    elif gusto=='cioccolato' :
        costo+=5
    elif gusto=='crema':
        costo+=2
print('il tuo costo è di'+' '+str(costo)+'$$')
print('Grazie alla prossima')