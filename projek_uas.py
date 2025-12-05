import streamlit as st
import datetime

#--- konfigurasi halaman ---
st.set_page_config(
    page_title="Aplikasi hidup sehat",
    layout="wide",
    initial_sidebar_state="expanded"
)

#--- halaman utama ---
def show_beranda():
    st.title("Selamat Datang di Health Companion 👋")
    st.image("https://res.cloudinary.com/dk0z4ums3/image/upload/v1635830348/attached_image/gaya-hidup-sehat-bisa-anda-mulai-sekarang-0-alodokter.jpg", caption="Ilustrasi Hidup Sehat")
    
    st.header("Permasalahan Kita Saat Ini")
    st.write("""
    Banyak mahasiswa atau pekerja kantoran yang sering merasa lelah, berat badan naik tak terkontrol, 
    atau justru terlalu kurus. hal ini disebabkan karna tidak adanya atau kurang perhatian terhadap 
    kesehatan tubuh dan biasanya hal itu dikeranakan hal berikut:
    1.  **Ketidaktahuan** akan status tubuh sendiri.
    2.  **Pola makan** yang tidak sesuai kebutuhan energi.
    3.  **Kurangnya referensi** gaya hidup praktis.
    4.  **Minimnya informasi** tentang pentingnya tidur yang cukup.
    
    Aplikasi ini hadir untuk membantu mengatasi permasalahan tersebut dengan menyediakan fitur-fitur
    yang mudah digunakan untuk memantau kesehatanmu sehari-hari.
    """)
    st.divider()

    st.subheader("Fitur-fitur utama yang kami tawarkan:")
    col1, col2 = st.columns(2)

    with col1:
        st.info("**1. Cek Status BMI**\nMengetahui kategori berat badanmu.")
        st.info("**2. Hitung Kalori**\nMenghitung kebutuhan energimu.")
    with col2:
        st.info("**3. Cek Air Minum**\nMenghitung target minum harian.")
        st.info("**4. Cek Waktu Tidur**\nMengatur siklus tidur agar bangun segar.")

    st.success("Tugas Projek UAS DDP KEL 15 - SEMOGA BERMANFAAT 😊")

    #-- halaman cek bmi ---



    #-- halaman hitung kalori ---



    #-- halaman cek air minum ---



    #-- halaman cek waktu tidur ---
    def show_halaman_tidur():
       st.title("💤 Cek Waktu Tidur (Sleep Cycle)")
       st.markdown("**Masalah:** Sering bangun tidur tapi badan pegal dan kepala pusing (Sleep Inertia).")
       st.write("Manusia tidur dalam siklus 90 menit. Kita harus bangun di akhir siklus agar segar.")
       st.divider()
    
    waktu_tidur = st.time_input("Jam berapa kamu berencana tidur?", datetime.time(22, 00))
    
    if st.button("Cek Waktu Bangun Terbaik"):
        st.write(f"Jika kamu tidur jam **{waktu_tidur}**, sebaiknya kamu bangun pada jam:")
        
        # Konversi datetime
        sekarang = datetime.datetime.now()
        start_tidur = sekarang.replace(hour=waktu_tidur.hour, minute=waktu_tidur.minute, second=0)
        
        if start_tidur < sekarang:
            start_tidur += datetime.timedelta(days=1)
        
        cols = st.columns(3) 
        
        daftar_siklus = [4, 5, 6] # Siklus tidur dalam hitungan 90 menit
        
        for i, siklus in enumerate(daftar_siklus):
            durasi_menit = siklus * 90
            waktu_bangun = start_tidur + datetime.timedelta(minutes=durasi_menit)
            
            jam_str = waktu_bangun.strftime("%H:%M")
            
            # hasil
            with cols[i]:
                st.info(f"Opsi {i+1} ({siklus} Siklus)")
                st.subheader(f"⏰ {jam_str}")
                st.caption(f"Tidur selama {durasi_menit/60} Jam")

#--- sidebar navigasi ---
def main():
    
    st.sidebar.title("SIDE BAR PENUNJUK KESEHATAN")
    st.sidebar.write("Navigasi Aplikasi:")
    
    pilihan = st.sidebar.radio(
        "Pilih Menu:",
        ("🏠 Beranda", "1. ⚖️ Cek Status BMI", "2. 🍎 Hitung Kalori", "3. 💧 Cek Air Minum", "4. 💤 Cek Waktu Tidur")
    )
    
    #  Pindah Halaman
    if pilihan == "🏠 Beranda":
        show_beranda()
    elif pilihan == "1. ⚖️ Cek Status BMI":
        show_halaman_bmi()
    elif pilihan == "2. 🍎 Hitung Kalori":
        show_halaman_kalori()
    elif pilihan == "3. 💧 Cek Air Minum":
        show_halaman_air()
    elif pilihan == "4. 💤 Cek Waktu Tidur":
       show_halaman_tidur()