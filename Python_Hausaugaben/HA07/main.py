import subplot as sub
import csv


# input: data name

while True: 
    
    try:  
        datei_name = input('CSV Dateiname:')
        x_list, y_list = [], []
        
        with open(datei_name, 'r', encoding='utf-8') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
               x_list.append(float(row[0]))
               y_list.append(float(row[1]))  

            break
    except FileNotFoundError:
        print("Datei wurde nicht gefunden. Bitte erneut einen Dateinamen eingeben.")
   
          

# input: function_value factor
while True:
    try:
        factor = float(input('Skalierungsfaktor: '))
    except ValueError:
        print('Der Skalierungsfaktor muss vom Typ Float sein.')
    else:
        break

# input: start_percent for x_interval
while True:
    try:
        start = float(input('Start Prozent: ')) / 100  # Achtung: start in [%]
        if start < 0 or start > 1:
            print('Es werden Floats zwischen 0 und 100 erwartet.')
            continue
    except ValueError:
        print('Es werden Floats als Eingabe erwartet.')
    else:
        break

# input: end_percent for x_interval
while True:
    try:
        end = float(input('End Prozent: ')) / 100  # !Achtung!: 'end' in [%]
        if end < 0 or end > 1:
            print('Es werden Floats zwischen 0 und 100 erwartet.')
            continue
        elif end <= start:
            print('Ausschnitt des Definitionsbereiches darf nicht kleiner gleich NULL sein.')
            continue
    except ValueError:
        print('Es werden Floats als Eingabe erwartet.')
    else:
        break

# data import

# make the function graph
sub.create_subplot(x_list, y_list, factor, start, end)
