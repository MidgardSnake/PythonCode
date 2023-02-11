#variable definition 
x = -1.2

#calculation
a = 3**(4 + x)
b = 938.1 // a
c = ((-2*x) + b) % a

#print results
print("2.2.1: a =", a)
print("2.2.2: b =", b)
print("2.2.3: c =", c)

#logical operations
aussage_1 = a < b
aussage_2 = (True or False) and not(a > b) != (-3 > -1)

#print results
print("2.2.4: a kleiner als b ist", aussage_1)
print("2.2.5: (wahr oder falsch) und nicht (a groesser als b) ist ungleich" +  
      "(-3 groesser als -1) ist", aussage_2)

"""
Zusatzfrage: 
Bei einer logischen und verknuepfung werden die einzelnen 
logischen ausdruecke nacheinander geprueft. 
Sobald der erste logische Ausdruck als false ausgewertet wird, 
so wird der zweite logische ausdruck der and Verknuepfung nicht mehr
ueberprueft da etwas mit logisch false verundet immer false ergeibt.

Mit s = 3 unt t = 0:
Beim pruefen von nur s/t > 0 wird zuerst die Division durchgefuehrt. Da eine 
Division durch null nicht moeglich ist wird ein wird der Fehler ausgegeben.

Beim pruefen von t != 0 and s/t > 0 zuerst wird t != 0 zu false ausgewertet. 
s/t wird demzuflge nicht mehr berechnet da durch die and Verknuepfung 
der gesammte Ausdruck bereits false ist, unabhaenngig davon wie s/t > 0 ausgwertet
wird. Somit kommt es nicht zu einem ZeroDevivsionError.
"""

s = 3 
t = 0

#error = s/t > 0
no_error = (t != 0) and (s/t > 0)     

print("\nZusatzfrage:")
print("Bei einer logischen und verknuepfung werden die einzelnen" +  
"logischen ausdruecke nacheinander geprueft." +
"Sobald der erste logische Ausdruck als false ausgewertet wird," +
"so wird der zweite logische Ausdruck der and Verknuepfung nicht mehr" +
"ueberprueft da etwas mit logisch false verundet immer false ergeibt.")

print("Mit s = 3 unt t = 0:" +
"Beim pruefen von nur s/t > 0 wird zuerst die Division durchgefuehrt. Da eine" + 
"Division durch null nicht moeglich ist wird ein wird der Fehler ausgegeben.")

print("Beim pruefen von t != 0 and s/t > 0 zuerst wird t != 0 zu false" +
      "ausgewertet. s/t wird demzuflge nicht mehr Berechnet da durch" + 
      "die and Verknuepfung der gesammte ausdruck bereits false ist,"+
      "unabhaenngig davon wie s/t > 0 ausgwertet wird. " + 
      "Somit kommt es nicht zu einem ZeroDevivsionError.")
