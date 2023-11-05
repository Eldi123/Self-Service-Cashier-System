# Self-Service Cashier System

Proyek ini adalah latihan coding Python pribadi yang dirancang untuk membuat sistem kasir self-service. Tujuan utamanya adalah membantu Andi, pemilik supermarket besar di Indonesia, mengotomatiskan proses pembayaran bagi pelanggannya. Dengan sistem ini, pelanggan dapat dengan mudah memasukkan barang yang dibelinya, menentukan jumlah, harga, dan mengakses fitur tambahan, meskipun mereka tidak hadir secara fisik di supermarket.

## Table of Contents
1. [Background](#background)
2. [Usage](#usage)
3. [Features](#features)
4. [Development](#development)

## Background
Andi, salah satu pemilik supermarket besar di Indonesia, berencana menggunakan sistem kasir swalayan di supermarketnya sehingga pelanggan dapat langsung memasukkan barang yang dibeli, jumlah yang dibeli, harga barang yang dibeli, dan fitur lainnya. Sehingga pelanggan yang berada di luar kota bisa membeli barang di supermarket.

## Usage
Program ini pada dasarnya merupakan program berbasis CLI yang masih dalam tahap pengembangan dan untuk menggunakannya dalam lingkup yang lebih komersial perlu dilakukan improvisasi kode untuk program berbasis GUI. Program ini terdiri dari dua bagian, modul_cashier.py yang menyimpan semua fungsi untuk menjalankan semua fitur program dan main_cashier.py. Untuk menggunakan kode ini, Anda dapat menjalankan main_cashier.py di IDE atau Anda juga dapat menjalankannya secara manual melalui comand line atau CMD tergantung sistem operasinya.

## Features
Setelah program berjalan, kita dapat menggunakan fitur-fiturnya. Berikut ini pemaparan nya:

**1. Add items**
Fitur ini dapat menambahkan nama barang, jumlah barang, dan harga barang dengan satu fungsi yaitu add_item. Berikut ini adalah flowchart untuk menjelaskan algoritma kerja fungsi tersebut.

![add_item](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/add_item%20function.drawio.png)

Pada fitur ini, input nama item diatur dengan tipe data bebas (bisa berupa string, angka float, atau integer). Hal ini karena nama item dapat berupa kode angka atau string dan kode angka juga dapat dianggap sebagai string. Namun pada saat menginput jumlah barang dan harga barang, tipe datanya ditetapkan sebagai float karena kedua input tersebut harus berupa angka dan alasan memilih float karena ada kemungkinan angka yang dimasukkan adalah pecahan. Pada fitur ini perlu kita ingat bahwa angka (float dan iteger) bisa menjadi string tetapi string tidak bisa menjadi angka. Sebagai konfirmasi, konversi ke float pada data input juga bisa secara otomatis mengakomodasi tipe data integer sehingga walaupun melakukan input integer tetap akan terkonversi ke tipe data float.

**2. Update input items**
Fitur ini dibuat untuk mengedit item yang telah diinput. Pada fitur ini, proses update nama barang, jumlah barang dan harga barang terjadi secara terpisah karena menggunakan tiga fungsi yang berbeda.
Untuk mengupdate nama item, fungsi yang digunakan adalah update_item_name. Berikut ini adalah diagram alur fungsi update_item_name:

![update_item_name](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/update_item_name%20function.drawio.png)

Sama seperti fitur add_item pada penambahan nama, fungsi update_item_name juga dapat menerima angka sebagai string.

Untuk memperbarui jumlah item, gunakan fungsi update_item_qty. Berikut adalah diagram alur update_item_qty:

![update_item_qty](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/update_item_qty%20function.drawio.png)

Selanjutnya update harga barang dilakukan menggunakan fungsi update_item_price. Berikut diagram alurnya:

![update_item_price](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/update_item_price%20function.drawio.png)

Sama seperti fitur tambah item, fungsi update_item_qty dan update_item_price juga dibuat untuk mengakomodasi tipe data float karena ada kemungkinan data masukan berupa desimal.

Yang menjadi perhatian pada saat mengembangkan fitur “Update input item” adalah apabila terjadi kesalahan pada input “Item name that want to be updated” dan pilihan update yang ingin dilakukan, maka program akan looping kembali meminta input nama item. Namun bila terjadi masalah saat menginput "New item quantity" dan "New item price" maka program akan looping meminta input "New item quantity" dan "New item price" yang mana pada bagian ini masalah yang terjadi adalah jika kita memasukkan integer pada input tersebut.

**3. Delete items**
Fitur ini dibuat untuk dapat menghapus item satu per satu. Cara kerja fitur ini adalah dengan mencocokkan nama item yang ada di daftar. Apabila cocok, maka item tersebut akan terhapus dan akan muncul pesan “The item that wants to be deleted is not listed” sebagai tanda kesalahan input ketika item tersebut tidak tercantum dan program akan looping lagi menanyakan item yang ingin dihapus.

Fitur ini menggunakan fungsi delete_item dari modul. Berikut ini adalah flowchart dari algoritma delete_item :

![delete_item](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/delete_item%20function.drawio.png)

**4. Reset transactions**
Fitur ini dibuat untuk menghapus semua input yang telah dilakukan agar dapat melakukan input kembali dari awal. Fitur ini dijalankan menggunakan fungsi reset_transaction dari modul. Berikut diagram alurnya:

![reset_transaction](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/reset_transaction%20function.drawio.png)

**5. Check Orders**
Fitur ini dilakukan untuk mengecek apakah ada kesalahan input. Pada fitur ini proses pengecekan error hanya berdasarkan ada tidaknya input nama item. Hal ini dikarenakan akan bertabrakan dengan fungsi pada fitur tambah barang dan perbarui barang, dimana fitur tersebut secara otomatis mengatur input harga barang dan jumlah barang dalam bentuk angka. Hal ini juga diperkuat dengan penerapan fitur Tampilkan transaksi secara bersamaan ke beberapa fitur lainnya sehingga jika terjadi kesalahan input juga akan gagal menampilkan daftar transaksi.

Fitur Cek pesanan dilakukan dengan menggunakan fungsi check_order. Berikut ini adalah flowchart dari algoritma fungsi check_order:

![check_order](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/check_order%20function.drawio.png)

**6. Calculate total purchases**
Fitur ini dibuat untuk menghitung jumlah total yang harus dibayar dari seluruh input item yang dibuat. Yang menarik dari fitur ini adalah terdapat ketentuan diskon berupa:
- 5% untuk pembelian > 200.000
- 8% untuk pembelian > 300.000
- 10% untuk pembelian > 500.000

Fitur ini dijalankan menggunakan fungsi total_paid dari modul. Berikut ini adalah flowchart dari algoritma fungsi total_paid :

![total_paid](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/total_paid%20function.drawio.png)

**7. Exit**
Fitur ini dijalankan tanpa fungsi dari modul dan hanya dibuat dengan menghentikan perulangan program yang sedang berjalan yang hanya menggunakan loop control flow statement “break” pada code.

**8. Show transactions**
Fitur ini merupakan fitur yang berjalan secara bersamaan ketika menjalankan beberapa fitur seperti Tambah barang, Perbarui barang masukan, Hapus barang, Periksa Pesanan, dan Hitung total pembelian. Hal ini bertujuan agar saat menjalankan fitur tersebut Anda dapat melihat detail daftar apa yang telah dilakukan.

Fitur ini dijalankan menggunakan fungsi transaction_list. Diagram alur fitur ini adalah sebagai berikut:

![transaction_list](https://github.com/Eldi123/Self-Service-Cashier-System/blob/main/Flowchart%20Self%20Service%20Cashier%20System/transaction_list%20function.drawio.png)

## Development

Seperti yang telah dijelaskan sebelumnya bahwa program ini masih berbasis CLI sehingga untuk penggunaan komersial perlu dibangun kode untuk program GUI. Selain itu juga dapat dikembangkan fitur tambahan berupa satuan dari input sehingga dapat dilakukan input yang lebih spesifik.

Atas dasar itulah saya terbuka menerima masukan untuk mengembangkan program ini. Saya sangat mengharapkan saran-saran yang dapat mengarahkan dan mengajarkan saya bagaimana mengembangkan program ini.
