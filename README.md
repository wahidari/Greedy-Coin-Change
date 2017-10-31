# Penukaran Koin Dengan Algoritma Greedy

[![](https://gitlab.com/gitlab-org/gitlab-ee/badges/master/build.svg)](https://wahidari.gitlab.io)
[![](https://semaphoreci.com/api/v1/projects/2f1a5809-418b-4cc2-a1f4-819607579fe7/400484/shields_badge.svg)](https://wahidari.gitlab.io)
[![](https://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat&maxAge=86400)](https://wahidari.gitlab.io)
[![](https://img.shields.io/badge/Find%20Me-%40wahidari-009688.svg?style=social)](https://wahidari.gitlab.io)

## Language

- [![](https://img.shields.io/badge/python-3.6-blue.svg)] (https://wahidari.gitlab.io) 

## Tools

- [![Other](https://img.shields.io/badge/spyder-3-red.svg)](https://gitlab.com/wahidari)

## Test coverage

- [![](https://gitlab.com/gitlab-org/gitaly/badges/master/coverage.svg)](https://wahidari.gitlab.io) python

## Documentation

- Penukaran Koin 
    
    
    Diberikan uang senilai A. Tukar A dengan koin-koin uang yang ada.  
    Berapa jumlah minimum koin yang diperlukan untuk penukaran tersebut?

    - **Contoh :**  
    
        - tersedia banyak koin 1, 5, 10, 25   
        - Uang  senilai 32 dapat ditukar dengan banyak cara berikut:   
        - 32 = 1 + 1 + … + 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (32 koin)   
        - 32 = 5 + 5 + 5 + 5 + 10 + 1 + 1 &nbsp;&nbsp; (7 koin)   
        - 32 = 10 + 10 + 10 + 1 + 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (5 koin)   
        - ... dst             
        - **Minimum: 32 = 25 + 5 + 1 + 1 &nbsp;&nbsp; (4 koin)**   

<!--- Graph Sederhana dari Titik A ke I-->

<!--    ![](./ss/b.png)-->
    
<!--    Dari gambar di atas, kita dapat melihat bagaimana sebuah peta jalur perjalanan dapat direpresentasikan dengan -->
<!--    menggunakan graph, spesifiknya Directed Graph (graph berarah). Maka dari itu, untuk menyelesaikan permasalahan -->
<!--    jarak terpendek ini kita akan menggunakan struktur data graph untuk merepresentasikan peta. -->
<!--    Berikut adalah graph yang akan digunakan:-->

<!--- Graph Berarah dari Titik A ke I-->

<!--    ![](./ss/c.png)-->
    
<!--- Graph Berarah Beserta Jarak Masing-Masing Titik dari Titik A ke I-->

<!--    ![](./ss/d.png)-->
    
<!--    Untuk mencari jarak terpendek dari A ke B, sebuah algoritma greedy akan menjalankan langkah-langkah seperti berikut:-->
    
    
<!--    a. Kunjungi satu titik pada graph, dan ambil seluruh titik yang dapat dikunjungi dari titik sekarang.-->
    
    
<!--    b. Cari local maximum ke titik selanjutnya.-->
    
    
<!--    c. Tandai graph sekarang sebagai graph yang telah dikunjungi, dan pindah ke local maximum yang telah ditentukan.-->
    
    
<!--    d. Kembali ke langkah 1 sampai titik tujuan didapatkan.-->
    
<!--- ScreenShot 5-->

<!--    ![](./ss/e.png)-->
    
<!--    Dengan menggunakan algoritma greedy pada graph di atas, hasil akhir yang akan didapatkan sebagai jarak terpendek adalah A-C-D-G-I. -->
<!--    Hasi jarak terpendek yang didapatkan ini tidak tepat dengan jarak terpendek yang sebenarnya (A-B-H-I). -->
<!--    Algoritma greedy memang tidak selamanya memberikan solusi yang optimal, dikarenakan pencarian local maximum pada setiap langkahnya, -->
<!--    tanpa memperhatikan solusi secara keseluruhan.-->
<!--- ScreenShot 6-->

<!--    ![](./ss/f.png)-->

<!--- ScreenShot 7-->

<!--    ![](./ss/g.png)-->
    

## License
> This program is Free Software: 
You can use, study, share and improve it at your will. 
Specifically you can redistribute and/or modify it under the terms of the [GNU General Public License](https://www.gnu.org/licenses/gpl.html) 
as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
