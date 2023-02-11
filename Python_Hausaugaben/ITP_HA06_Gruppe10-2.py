"""
6. Hausaufgabe: Batch Klausurbenotung

@author: Gruppe 10
"""

"""
@brief      Function calculates the garde. 
            Indicates whether the exam has been passed or not
@param[in]  g: grade tabel in type 'int'
@param[in]  s: exam score in type 'int'

@return:    exam_result_data [garde, passed] type float, bool 
"""
def calculate_exam_result(g, s):  # calculation of the exam_result
    exam_result_data = []
    if g == 1:
        if s < 50:
            exam_result_data = [5.0, False]
        elif 50 <= s < 54:
            exam_result_data = [4.0, True]
        elif 54 <= s < 58:
            exam_result_data = [3.7, True]
        elif 58 <= s < 62:
            exam_result_data = [3.3, True]
        elif 62 <= s < 66:
            exam_result_data = [3.0, True]
        elif 66 <= s < 70:
            exam_result_data = [2.7, True]
        elif 70 <= s < 74:
            exam_result_data = [2.3, True]
        elif 74 <= s < 78:
            exam_result_data = [2.0, True]
        elif 78 <= s < 82:
            exam_result_data = [1.7, True]
        elif 82 <= s < 86:
            exam_result_data = [1.3, True]
        else:
            exam_result_data = [1.0, True]
    elif g == 2:
        if s < 50:
            exam_result_data = [5.0, False]
        elif 50 <= s < 55:
            exam_result_data = [4.0, True]
        elif 55 <= s < 60:
            exam_result_data = [3.7, True]
        elif 60 <= s < 65:
            exam_result_data = [3.3, True]
        elif 65 <= s < 70:
            exam_result_data = [3.0, True]
        elif 70 <= s < 75:
            exam_result_data = [2.7, True]
        elif 75 <= s < 80:
            exam_result_data = [2.3, True]
        elif 80 <= s < 85:
            exam_result_data = [2.0, True]
        elif 85 <= s < 90:
            exam_result_data = [1.7, True]
        elif 90 <= s < 95:
            exam_result_data = [1.3, True]
        else:
            exam_result_data = [1.0, True]
    elif g == 3:
        if s < 40:
            exam_result_data = [5.0, False]
        elif 40 <= s < 45:
            exam_result_data = [4.0, True]
        elif 45 <= s < 50:
            exam_result_data = [3.7, True]
        elif 50 <= s < 55:
            exam_result_data = [3.3, True]
        elif 55 <= s < 60:
            exam_result_data = [3.0, True]
        elif 60 <= s < 65:
            exam_result_data = [2.7, True]
        elif 65 <= s < 70:
            exam_result_data = [2.3, True]
        elif 70 <= s < 75:
            exam_result_data = [2.0, True]
        elif 75 <= s < 80:
            exam_result_data = [1.7, True]
        elif 80 <= s < 85:
            exam_result_data = [1.3, True]
        else:
            exam_result_data = [1.0, True]
    return exam_result_data


# --------------- Input --------------- #
# input01: Notenschlüssel (type: int)
# input02: Matrikelnummer (type: int)
# input03: Klausurpunkte (type: float)
# input04: looping_trigger for break out (type: str)

"""
exam_data[matrikelnummer][exam_grade][passed]
matrikelnummer type int
exam_grade type float
passed type string ('ja', 'nein')
"""
exam_data = {}  # datenbank for the exam_information

input01 = int(input('Notenschluessel: '))  # int
if input01 not in [1, 2, 3]:
    raise ValueError('Fehler: Ungültiger Notenschluessel.')

while True:
    input02 = int(input('Matrikelnummer: '))  # int
    if input02 <= 0:
        raise ValueError('Fehler: Ungültige Matrikelnummer.')

    input03 = float(input('Punkte: '))  # float
    if (input03 < 0) or (input03 > 100):
        raise ValueError('Fehler: Ungültige Punkte.')

    exam_data[input02] = [input03]  # store the parameters 'Matrikelnr.' and 'Punkte' in the datenbank

    input04 = input('Weitere Eingabe: "ja" oder "nein"')
    if (input04 not in ['ja', 'nein']) or (input04 == 'nein'):
        break

# add parameters 'Note' and 'Bestanden' to the databank 'exam_data'
for matrikelnummer in exam_data.keys():
    exam_result = calculate_exam_result(input01, exam_data[matrikelnummer][0]) 
    exam_data[matrikelnummer].append(exam_result[0])   #store exam grade in databank
    
    if exam_result[1]:  # check if exam passed and store result string in databank
        exam_data[matrikelnummer].append('ja')
    else:
        exam_data[matrikelnummer].append('nein')

exam_data = sorted(exam_data.items())  # sort the databank by the 'Matrikelnummer'


# --------------- Output --------------- #
# layout & print_out
print('Mtr.\tPunkte\tNote\tBeatanden')

for element in exam_data:
    print(f'{element[0]}\t{element[1][0]}\t{element[1][1]}\t{element[1][2]}')
