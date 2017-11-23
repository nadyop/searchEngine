"""
author rochanaph
September 21 2017
"""
import math
def euclidean(vector1, vector2):
    """
    terbaik~
    Mengurangkan konstanta
    fungsi untuk menghitung jarak antara 2 vektor dengan rumus euclidean ddistance
    Jarak Euclidean antara dua titik adalah panjang jalur yang menghubungkannya.
    Teorema Pythagoras memberikan jarak antara dua titik ini.
    :param vector1: vektor 1
    :param vector2: vektor
    :return:
    """
    dist = [(a - b)**2 for a, b in zip(vector1, vector2)]
    dist = math.sqrt(sum(dist))
    return dist

def cosine(vector1, vector2):
    """
    Memperhatikan derajat antara dua vektor
    Metrik kemiripan kosinus menemukan produk titik normal dari dua atribut.
    Dengan menentukan kesamaan kosinus, kita akan secara efektif menemukan kosinus sudut antara kedua benda tersebut.
    :param vector1:
    :param vector2:
    :return:
    """

    dot  = sum([a*b for a,b in zip(vector1, vector2)])
    mag1 = math.sqrt(sum([a**2 for a in vector1]))
    mag2 = math.sqrt(sum([a**2 for a in vector2]))
    return dot/(mag1*mag2)



p = [1,1,1,1,2,0,0]
q = [0,0,1,1,1,1,1]

# print euclidean(p,q)
# print cosine(p,q)

def manhattan_distance(vector1,vector2):
    """

    Jarak Manhattan adalah metrik dimana jarak antara dua titik, jumlah perbedaan mutlak koordinat Cartesian
    Misal, ada 2 (A,B) jika ingin menemukan jarak Manhattan di antara keduanya,
    harus meringkas, sumbu x dan sumbu y yang nantinya akan menemukan bagaimana kedua titik A dan B ini adalah variasi dalam sumbu X dan sumbu Y.
    """
    return sum(abs(a-b) for a,b in zip(vector1,vector2))

def jaccard_similarity(vector1,vector2):
    """
    Membagi jumlah irisan dari 2 dokumen dengan penggabungan data dari 2 file
    Irisan kata diperoleh dari kata yang sama antara dua dokumen. Sedangkan jumlah baris merupakan jumlah term yang ada pada kedua dokumen tersebut
    """
    intersection_cardinality = len(set.intersection(*[set(vector1),set(vector2)]))
    union_cardinality = len(set.union(*[set(vector1),set(vector2)]))
    return intersection_cardinality/float(union_cardinality)

    # Input: 2 objects
    # Output: Pearson Correlation Score
def pearson_correlation(object1, object2):
    """
    Digunakan untuk mengukur kekuatan dan arah hubungan linier dari dua veriabel.
    2 variabel dikatakan berkorelasi apabila perubahan salah satu variabel disertai dengan perubahan variabel lainnya,
    (arah yang sama ataupun arah yang sebaliknya).
    """
    values = range(len(object1))

    # memanggil ulang semua atribut untuk kedua objek
    sum_object1 = sum([float(object1[i]) for i in values])
    sum_object2 = sum([float(object2[i]) for i in values])

    # Sum the squares
    square_sum1 = sum([pow(object1[i], 2) for i in values])
    square_sum2 = sum([pow(object2[i], 2) for i in values])

    # Add up the products
    product = sum([object1[i] * object2[i] for i in values])

    # Calculate Pearson Correlation score
    numerator = product - (sum_object1 * sum_object2 / len(object1))
    denominator = ((square_sum1 - pow(sum_object1, 2) / len(object1)) * (square_sum2 -
                                                                         pow(sum_object2, 2) / len(object1))) ** 0.5

    # Can"t have division by 0
    if denominator == 0:
        return 0
    # di abs agar tidak minus, karena kalo minus tidak dpt muncul piechart nya
    result = abs(numerator / denominator)
    return result
