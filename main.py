from gtts import gTTS
from playsound import playsound
import os

class PresentationSpeak(object):
    def __init__(self,name):
        self.name = name

    def speak(self,audioString):
        print(audioString)
        tts = gTTS(text=audioString,lang='id',slow=False,lang_check=True)
        tts.save('audio.mp3')
        playsound('audio.mp3')
        os.remove('audio.mp3')

def main():
    presentationspeak = PresentationSpeak('eric')
    text = [
        'Selamat Pagi teman-teman',
        'Perkenalkan nama saya eric',
        'Mohon maaf pada kali ini saya membuat program yang membuat saya setidaknya bisa berbicara didalam presentasi kali ini',
        'Seperti yang saya sudah saya jelaskan di group WhatsApp, bahwa mic saya AMPAS!!',
        'Saya membuat program ini semalaman jadi tolong dimaklumi',
        'Kalau teman-teman penasaran ingin buat program ini silahkan datang ke github saya',
        'Oke balik ke topik presentasi',
        'Pada kali ini saya akan mempresentasikan project Internet of Thing kelompok kami',
        'Pertama-tama perkenalkan nama saya adalah Ida Bagus Dwi Putra Purnawa alias eric cornetto',
        'Dan ada teman-teman saya yaitu Adrian, Deva M-Word, dan Ricardo Wisnu h3h3h3h3',
        'Tema project yang kami ambil adalah Home Automation',
        'Home Automation adalah sebuah system automisasi rumah yang digunakan untuk mempermudah penggunanya dalam melakukan berbagai kegiatan dirumah',
        'Eitsss tunggu dulu, kami membuat bukan Home Automation biasa, kami menggunakan Intellegent Personal Assistant atau yang sering disebut Virtual assistant',
        'Intellegent Personal Assistant disini berperan sebagai media perantara pengguna dengan mesin',
        'Intellegent Personal Assistant atau yang nama lainnya virtual assistant merupakan system kecerdasan buatan yang membantu pengguna dalam menyelesaikan berbagai tugas yang bersifat repeatable',
        'Mungkin teman-teman pernah dengar tentang Alexa,Google Assistant, dan Siri',
        'Mereka adalah contoh produk Virtual Assistant yang sering digunakan dan bisa diterapkan dalam system Home Automation',
        'Nah pada kali ini kami membuat versi kami sendiri, tetapi fitur Home Automation sangatlah luas, jadi pada kali ini kami cuman menerapkan beberapa fitur Home Automation dikarenakan keterbatasan budget',
        'Beberapa Fitur yang kami mungkin kami terapkan yaitu seperti menghidupkan lampu dengan Virtual Assistant,monitoring temperatur,memainkan musik,dan lain-lain',
        'Fitur yang kami buat nanti bergantung terhadap ketersediaan budget, mungkin kami menerapkan beberapa fitur saja atau bisa saja lebih',
        'Selanjutnya kami tentu saja menggunakan Raspberry Pi karena tidak mungkin menggunakan arduino untuk menjalankan Machine Learning di dalamnya, karena memiliki kekuatan komputasi yang lebih rendah dari Raspberry Pi',
        'Buat teman-teman yang ingin membuat system Deep Learning saya sarankan menggunakan Jetson Nano',
        'Selanjutnya yaitu alat-alat yang dibutuhkan, alat-alat didalam list tersebut masih bersifat sementara tergantung kebutuhan fitur yang ada',
        'Selanjutnya yaitu proses pengerjaan project kami',
        'Pertama membuat model Virtual Assistantnya , untuk membuat model tersebut saya yang bertanggung jawab dikarenakan di dalam kelompok kami hanya saya yang mempunyai pengetahuan dibidang Kecerdasan buatan',
        'Kedua membuat skema wire diagram, tugas ini dikerjakan oleh teman-teman kelompok saya',
        'Ketiga memasang alat sesuai wire diagram',
        'Keempat menjalankan program Virtual Assistant yang saya buat di dalam raspberry pi',
        'Kelima melakukan Trial and Error di dalam program',
        'Terakhir melakukan penyesuaian antara program dengan alat',
        'Selanjutnya adalah maanfaat dari Home Automation',
        'Pertama mempermudah pekerjaan yang bersifat repeatable atau berulang-ulang seperti menonton televisi,memutar musik,membuka pintu,menyalakan lampu dan lain-lain',
        'Yang Kedua ,dengan berkurangnya pekerjaan berulang-ulang yang dilakukan membuat kita lebih fokus terhadap pekerjaan yang produktif',
        'Ketiga, tentu saja kita punya tenaga lebih dalam melakukan perkerjaan yang lebih produktif',
        'Yang terakhir, jika teman-teman menganut paham boboknisme, project ini sangatlah berguna sekali',
        'Sekian presentasi saya, saya ucapkan terima kasih'



    ]

    for i in text:
        presentationspeak.speak(i)


if __name__ == '__main__':
    main()