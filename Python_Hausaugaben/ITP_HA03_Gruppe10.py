# -*- coding: utf-8 -*-
"""
3. Hausaufgabe: Automatisierte Klausurbenotung

@author: Gruppe 10
"""


def exam_result(g, s):  # calculation of the exam_result 
    """
    parameter "g": grade_number
    parameter "s": exam_score
    """
    if g == 1:
        if s < 50:
            return 'Note: 5.0'
        elif 50 <= s < 54:
            return 'Note: 4.0'
        elif 54 <= s < 58:
            return 'Note: 3.7'
        elif 58 <= s < 62:
            return 'Note: 3.3'
        elif 62 <= s < 66:
            return 'Note: 3.0'
        elif 66 <= s < 70:
            return 'Note: 2.7'
        elif 70 <= s < 74:
            return 'Note: 2.3'
        elif 74 <= s < 78:
            return 'Note: 2.0'
        elif 78 <= s < 82:
            return 'Note: 1.7'
        elif 82 <= s < 86:
            return 'Note: 1.3'
        return 'Note: 1.0'
    elif g == 2:
        if s < 50:
            return 'Note: 5.0'
        elif 50 <= s < 55:
            return 'Note: 4.0'
        elif 55 <= s < 60:
            return 'Note: 3.7'
        elif 60 <= s < 65:
            return 'Note: 3.3'
        elif 65 <= s < 70:
            return 'Note: 3.0'
        elif 70 <= s < 75:
            return 'Note: 2.7'
        elif 75 <= s < 80:
            return 'Note: 2.3'
        elif 80 <= s < 85:
            return 'Note: 2.0'
        elif 85 <= s < 90:
            return 'Note: 1.7'
        elif 90 <= s < 95:
            return 'Note: 1.3'
        return 'Note: 1.0'
    elif g == 3:
        if s < 40:
            return 'Note: 5.0'
        elif 40 <= s < 45:
            return 'Note: 4.0'
        elif 45 <= s < 50:
            return 'Note: 3.7'
        elif 50 <= s < 55:
            return 'Note: 3.3'
        elif 55 <= s < 60:
            return 'Note: 3.0'
        elif 60 <= s < 65:
            return 'Note: 2.7'
        elif 65 <= s < 70:
            return 'Note: 2.3'
        elif 70 <= s < 75:
            return 'Note: 2.0'
        elif 75 <= s < 80:
            return 'Note: 1.7'
        elif 80 <= s < 85:
            return 'Note: 1.3'
        return 'Note: 1.0'
    

grade_nr = int(input('Bitte geben Sie einen passenden Notenschluessel ein.'))

if grade_nr not in [1, 2, 3]:
    raise Exception('Fehler: Unbekannter Notenschluessel!')

score = float(input('Bitte geben Sie Ihre erreichten Punkte ein.'))     

print(exam_result(grade_nr, score))
