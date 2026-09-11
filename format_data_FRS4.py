import numpy as np
from pathlib import Path
from astropy.time import Time
from collections import defaultdict


####################################################################################################

def list_data(data_name):
    data = []
    for datei in Path(data_name).iterdir():
        data.append(datei.name)
    return data

def read_angle(data_name):
    print('                    ' + 'Read Angle')
    data_angle = []
    with open(data_name, 'r', encoding='utf-8') as f:
        for zeile in f:
            if zeile.startswith('ELE_STA/AZI_STA/NAD_SAT/AZI_SAT'):
                data_angle.append(zeile.strip().split())
    f.close()
    return data_angle

def read_residuen(data_name, skiprows=0):
    print('                    ' + 'Read Residuen')
    data_residuen = []
    count = 0
    with open(data_name, 'r', encoding='utf-8') as f:
        for zeile in f:
            if count >= skiprows:
                data_residuen.append(zeile.strip().split())
            count += 1
    f.close()
    return data_residuen

def compute_distances(pos_gnss, pos_genesis, data_res): # Hilfe KI
    print('                    ' + 'Compute Distances')


    ## GNSS Positionen einlesen

    data_gnss = defaultdict(dict)

    with open(pos_gnss, 'r', encoding='utf-8') as f:
        current_time = None
        for zeile in f:
            if zeile.startswith('*'):
                zeidat = zeile.split()
                t = Time(f'{zeidat[1]}-{zeidat[2]}-{zeidat[3]} {zeidat[4]}:{zeidat[5]}:{float(zeidat[6])}', scale='utc')
                current_time = round(t.unix, 1)
                continue
            
            if current_time is None:
                continue

            if not (zeile.startswith('PG') or zeile.startswith('PR') or zeile.startswith('PE')):
                continue

            zeidat = zeile.split()
            if len(zeidat) < 4: continue ## safety check
            data_gnss[current_time][zeidat[0]] = np.array([float(zeidat[1]), float(zeidat[2]), float(zeidat[3])])
    

    ## GENESIS Positionen einlesen

    data_gene = {}

    with open(pos_genesis, 'r', encoding='utf-8') as f:
        current_time = None
        for zeile in f:
            zeile = zeile.strip()
            if zeile.startswith('*'):
                zeidat = zeile.split()
                t = Time(f'{zeidat[1]}-{zeidat[2]}-{zeidat[3]} {zeidat[4]}:{zeidat[5]}:{float(zeidat[6])}', scale='utc')
                current_time = round(t.unix, 1)
                continue

            if current_time is None:
                continue

            if not zeile.startswith('PL'):
                continue

            zeidat = zeile.split()
            if len(zeidat) < 4: continue
            data_gene[current_time] = np.array([float(zeidat[1]), float(zeidat[2]), float(zeidat[3])])


    ## Distanzen berechnen

    distances = []

    for i in range(len(data_res[:, 0])):
        mjd = float(data_res[i, 2])
        sat = int(data_res[i, 4])

        if 0 < sat < 10: sat_line = f'PG0{sat}'
        elif 9 < sat < 100: sat_line = f'PG{sat}'
        elif 200 < sat < 210: sat_line = f'PE0{sat - 200}'
        elif 209 < sat < 300: sat_line = f'PE{sat - 200}'
        else: continue

        timeline = Time(mjd, format='mjd', scale='utc')
        key = round(timeline.unix, 1)
        data_posgnss = np.array([np.nan, np.nan, np.nan])
        data_posgene = np.array([np.nan, np.nan, np.nan])

        if key in data_gnss:
            data_posgnss = data_gnss[key].get(sat_line, np.array([np.nan, np.nan, np.nan]))
        
        if key in data_gene:
            data_posgene = data_gene[key]

        dist = np.linalg.norm(data_posgnss - data_posgene)
        distances.append(dist)
    
    return distances

def stack_data(ord, data1, data2):
    print('                    ' + 'Stack Data')
    data = []
    i1, i2 = 0, 0
    for i in range(len(ord)):
        if ord[i] == '1':
            data.append(data1[i1])
            i1 += 1
        else:
            data.append(data2[i2])
            i2 += 1
    return data

def append_data(data_org, data_new, data_nli, day=None):
    print('                    ' + 'Append Data')
    data = []
    header = ['Day', 'Num', 'Epoch', 'Epoch [MJD]', 'Sat', 'Value', 'Elev', 'Azi', 'ELE_STA', 'AZI_STA', 'NAD_SAT', 'AZI_SAT', 'Dist']
    if day == None: header.pop(0)
    data.append(header)
    if day != None:
        for i in range(len(data_org)):
            do = data_org[i]
            dn = data_new[i]
            data.append([day, do[0], do[1], do[2], do[4], do[6], do[7], do[8], dn[6], dn[7], dn[8], dn[9], data_nli[i]])
    else:
        for i in range(len(data_org)):
            do = data_org[i]
            dn = data_new[i]
            data.append([do[0], do[1], do[2], do[4], do[6], do[7], do[8], dn[6], dn[7], dn[8], dn[9], data_nli[i]])
    return data

def write_data(data, data_name):
    print('                    ' + 'Write Data')
    # maximale Breite je Spalte bestimmen
    breiten = [max(len(str(liste[i])) for liste in data) for i in range(len(data[0]))]

    with open('daten_FRS4/' + data_name, 'w') as f:
        for liste in data:
            zeile = ''.join(f'{str(wert):<{breiten[i] + 2}}' for i, wert in enumerate(liste)) # f'{liste[0]:<10}{liste[1]:<10}{liste[2]:<10}'
            f.write(zeile + '\n')
    f.close()


####################################################################################################

print()
print('####################################################################################################')
print('##########' + ''.center(80) + '##########')
print('##########' + 'GENESIS - Format Data'.center(80) + '##########')
print('##########' + ''.center(80) + '##########')
print('####################################################################################################')
print()


name_winkel = list_data('daten_winkel')
name_residuen = list_data('daten_residuen')
name_gnss_pos = list_data('daten_F3_23ddd_10.PRE')
name_genesis_pos = list_data('daten_RDAB49NG23ddd0.PRE')


Path('daten_FRS4').mkdir(exist_ok=True)

for i in range(len(name_residuen)):
    print('                  - ' + name_residuen[i][:8] + name_residuen[i][8:-1] + '4')

    data_residuen = read_residuen('daten_residuen/' + name_residuen[i], 22)

    data_winkel_n = read_angle('daten_winkel/' + name_winkel[i])
    data_winkel_z = read_angle('daten_winkel/' + name_winkel[len(name_winkel) // 2 + i])
    data_distance = compute_distances('daten_F3_23ddd_10.PRE/' + name_gnss_pos[i], 'daten_RDAB49NG23ddd0.PRE/' + name_genesis_pos[i], np.array(data_residuen))

    data_winkel = stack_data([data_residuen[i][0] for i in range(len(data_residuen))], data_winkel_n, data_winkel_z)

    day = int(name_residuen[i][10:13])

    data = append_data(data_residuen, data_winkel, data_distance, day=day)

    ## Entfernen der Ausreisser
    data = [data[0]] + [liste for liste in data[1:] if abs(float(liste[5])) <= 0.1]

    write_data(data, name_residuen[i][:-1] + '4')


print()
print('####################################################################################################')
print()

