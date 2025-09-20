# Dokumentasi MQTT

## 1. Cara Kerja
MQTT menggunakan model **publish-subscribe** dengan perantara **broker**:
- **Publisher**: mengirimkan pesan ke sebuah *topik*.
- **Broker**: menerima pesan dari publisher lalu menyalurkannya.
- **Subscriber**: menerima pesan yang masuk pada topik yang disubscribe.

Contoh alurnya:
1. Publisher mengirim pesan `"Suhu: 28°C"` ke topik `sister/temp`.
2. Broker menerima pesan tersebut.
3. Semua subscriber yang subscribe topik `sister/temp` akan menerima pesan yang sama.

---

## 2. Contoh Program
Terdapat dua program:
- **pub.py** → bertindak sebagai publisher. Mengirim pesan suhu (`"Suhu: 28°C"`).
- **sub.py** → bertindak sebagai subscriber. Menerima pesan dari topik `sister/temp` dan menampilkannya di terminal.

Keduanya terhubung ke broker MQTT bernama `mqtt-broker`.

---

## 3. Contoh Output di Terminal

![Output Publisher](dokumentasi/mqtt/pub.png)
### Publisher (`pub.py`)
```bash
Menghubungkan ke mqtt-broker...
Berhasil terhubung ke broker MQTT mqtt-broker
Published: Suhu: 28°C
Published: Suhu: 28°C
Published: Suhu: 28°C
```

![Output Subscriber](dokumentasi/mqtt/sub.png)
### Subscriber (`sub.py`)

```bash
Menghubungkan ke mqtt-broker...
Berhasil terhubung ke broker MQTT mqtt-broker
Berlangganan topik: sister/temp
Menunggu pesan... (Tekan Ctrl+C untuk keluar)
Received message: Suhu: 28°C (Topic: sister/temp)
Received message: Suhu: 28°C (Topic: sister/temp)
Received message: Suhu: 28°C (Topic: sister/temp)
```

## 4. Analisis Wireshark

![Wireshark](dokumentasi/mqtt/wireshark.png)

1. Ringkasan
Di dalamnya terlihat ada:
- Proses TCP handshake
- MQTT connect dari publisher ke broker
- MQTT connack dari broker ke publisher
- beberapa MQTT publish berisi data suhu ke topik sister/temp

2. Alur Komunikasi
a. TCP Handshake
- 172.18.0.5 mengirim TCP SYN ke 172.18.0.4:1883
- 172.18.0.4 membalas dengan SYN, ACK
- 172.18.0.5 mengirim ACK → koneksi TCP berhasil dibuka.

b. MQTT Session Establishment
- Publisher (172.18.0.5) mengirim MQTT Connect Command ke broker
- Broker (172.18.0.4) merespons dengan MQTT Connect Ack → sesi MQTT siap digunakan.