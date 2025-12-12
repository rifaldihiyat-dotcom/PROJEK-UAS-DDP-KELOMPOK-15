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
    st.image(
        "https://res.cloudinary.com/dk0z4ums3/image/upload/v1635830348/attached_image/gaya-hidup-sehat-bisa-anda-mulai-sekarang-0-alodokter.jpg",
        caption="Ilustrasi Hidup Sehat"
    )
    
    st.header("Permasalahan Kita Saat Ini")
    st.write("""
    Banyak mahasiswa atau pekerja kantoran yang sering merasa lelah, berat badan naik tak terkontrol, 
    atau justru terlalu kurus. Hal ini sering disebabkan oleh:
    
    1. **Ketidaktahuan** akan status tubuh sendiri.  
    2. **Pola makan** yang tidak sesuai kebutuhan energi.  
    3. **Kurangnya referensi** gaya hidup sehat praktis.  
    4. **Minimnya informasi** tentang pentingnya tidur yang cukup.
    
    Aplikasi ini hadir untuk membantu memantau kesehatanmu sehari-hari.
    """)
    st.divider()

    st.subheader("Fitur-fitur utama:")
    col1, col2 = st.columns(2)

    with col1:
        st.info("**1. Cek Status BMI**\nMengetahui kategori berat badanmu.")
        st.info("**2. Hitung Kalori**\nMenghitung kebutuhan energimu.")

    with col2:
        st.info("**3. Cek Air Minum**\nMenghitung target minum harian.")
        st.info("**4. Cek Waktu Tidur**\nMengatur siklus tidur agar bangun segar.")

    st.success("Tugas Projek UAS DDP KEL 15 - SEMOGA BERMANFAAT 😊")

#-- halaman cek BMI ---
def show_halaman_bmi():
    st.title("⚖ Cek Status BMI (Body Mass Index)")
    st.write("BMI adalah indikator sederhana untuk mengetahui apakah berat badanmu ideal.")
    
    col1, col2 = st.columns(2)
    with col1:
        berat = st.number_input("Masukkan Berat Badan (kg)", min_value=10.0, value=50.0)
    with col2:
        tinggi = st.number_input("Masukkan Tinggi Badan (cm)", min_value=50.0, value=160.0)

    if st.button("Hitung BMI"):
        # Rumus BMI: Berat / (Tinggi/100)^2
        tinggi_m = tinggi / 100
        bmi = berat / (tinggi_m ** 2)
        
        st.divider()
        st.metric(label="Skor BMI Kamu", value=f"{bmi:.2f}")
        
        # Logika Kategori (Conditional If-Elif)
        if bmi < 18.5:
            st.warning("Kategori: *Kekurangan Berat Badan (Underweight)*")
            st.write("Tips: Perbanyak asupan kalori dan protein sehat.")
        elif 18.5 <= bmi < 24.9:
            st.success("Kategori: *Normal (Ideal)*")
            st.write("Tips: Pertahankan pola makan dan olahraga teratur!")
        elif 25 <= bmi < 29.9:
            st.warning("Kategori: *Kelebihan Berat Badan (Overweight)*")
            st.write("Tips: Kurangi gula dan lemak, serta rutin berolahraga.")
        else:
            st.error("Kategori: *Obesitas*")
            st.write("Tips: Segera konsultasikan dengan ahli gizi atau dokter.")
   

#-- halaman hitung kalori ---
def show_halaman_kalori():
    st.title("🍎 Hitung Kebutuhan Kalori Harian")
    st.write("Menggunakan rumus Harris-Benedict.")

    gender = st.radio("Jenis Kelamin:", ("Laki-laki", "Perempuan"))
    usia = st.number_input("Usia (tahun)", 10, 100, 20)
    berat = st.number_input("Berat Badan (kg)", 10.0, 200.0, 60.0)
    tinggi = st.number_input("Tinggi Badan (cm)", 100.0, 250.0, 170.0)

    aktivitas = st.selectbox("Tingkat Aktivitas", (
        "Sangat Jarang (Tidak olahraga)",
        "Jarang (Olahraga 1-3 hari/minggu)",
        "Normal (Olahraga 3-5 hari/minggu)",
        "Sering (Olahraga 6-7 hari/minggu)",
        "Ekstrem (Fisik berat/atlet)"
    ))

    if st.button("Hitung Kalori"):
        if gender == "Laki-laki":
            bmr = 66.5 + (13.75 * berat) + (5.003 * tinggi) - (6.75 * usia)
        else:
            bmr = 655.1 + (9.563 * berat) + (1.850 * tinggi) - (4.676 * usia)

        faktor = {
            "Sangat Jarang (Tidak olahraga)": 1.2,
            "Jarang (Olahraga 1-3 hari/minggu)": 1.375,
            "Normal (Olahraga 3-5 hari/minggu)": 1.55,
            "Sering (Olahraga 6-7 hari/minggu)": 1.725,
            "Ekstrem (Fisik berat/atlet)": 1.9
        }

        kalori = bmr * faktor[aktivitas]

        st.success(f"Kebutuhan Kalori Harian: **{int(kalori)} kkal**")
        st.info("""
        💡 Tips:
        - Makan makanan seimbang  
        - Minum cukup air  
        - Olahraga rutin  
        - Kurangi gula & lemak berlebih  
        """)

#-- halaman cek air minum ---
def show_halaman_air():
    st.title("💧 Cek Kebutuhan Air Minum")
    st.write("Tubuh manusia membutuhkan air sekitar 30-40ml per kg berat badan.")
    
    berat = st.number_input("Masukkan Berat Badanmu (kg)", 10.0, 200.0, 50.0)
    
    if st.button("Hitung Kebutuhan Air"):
        # Rumus sederhana: Berat * 30ml
        air_ml = berat * 30
        air_liter = air_ml / 1000
        
        gelas = air_ml / 250 # Asumsi 1 gelas = 250ml
        
        st.divider()
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Volume Air", f"{air_liter:.1f} Liter")
        with col2:
            st.metric("Jumlah Gelas", f"{int(gelas)} Gelas")
            
        st.info(f"Disarankan minum minimal *{int(gelas)} gelas* (ukuran 250ml) sehari agar tidak dehidrasi.")
#-- halaman cek waktu tidur ---
def show_halaman_tidur():
    st.title("💤 Cek Waktu Tidur (Sleep Cycle)")
    st.markdown("**Masalah:** Sering bangun pusing? Bisa jadi kamu bangun di tengah siklus tidur!")
    st.write("Tidur manusia terdiri dari siklus 90 menit. Bangun di akhir siklus membuat tubuh lebih segar.")
    st.divider()

    waktu_tidur = st.time_input("Jam berapa kamu akan tidur?", datetime.time(22, 0))

    if st.button("Cek Waktu Bangun Terbaik"):
        st.info(f"Jika kamu tidur jam **{waktu_tidur}**, waktu bangun terbaik adalah:")

        sekarang = datetime.datetime.now()
        start_tidur = sekarang.replace(
            hour=waktu_tidur.hour,
            minute=waktu_tidur.minute,
            second=0
        )

        if start_tidur < sekarang:
            start_tidur += datetime.timedelta(days=1)

        cols = st.columns(3)
        siklus_list = [4, 5, 6]

        for i, siklus in enumerate(siklus_list):
            durasi = siklus * 90
            waktu_bangun = start_tidur + datetime.timedelta(minutes=durasi)
            jam_str = waktu_bangun.strftime("%H:%M")

            with cols[i]:
                st.info(f"Opsi {i+1} — {siklus} Siklus")
                st.subheader(f"⏰ {jam_str}")
                st.caption(f"Durasi tidur: {durasi//60} jam")

#--- sidebar navigasi ---
def main():
    st.sidebar.title("SIDE BAR PENUNJUK KESEHATAN")
    pilihan = st.sidebar.radio(
        "Pilih Menu:",
        ("🏠 Beranda", "1. ⚖️ Cek Status BMI", "2. 🍎 Hitung Kalori",
         "3. 💧 Cek Air Minum", "4. 💤 Cek Waktu Tidur")
    )

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

if __name__ == "__main__":
    main()
        