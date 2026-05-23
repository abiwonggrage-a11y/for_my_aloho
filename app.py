import streamlit as st

# 1. Konfigurasi halaman (bikin judul di tab browser & pakai emoji lucu)
st.set_page_config(
    page_title="Hiii my aloho! 🌟",
    page_icon="💖",
    layout="centered"
)

# 2. Efek balon otomatis pas web pertama kali dibuka
st.balloons()

# 3. Bagian Header / Pembuka
st.title("💖 💖")
st.subheader("Bikin web ini khusus buat alohomorais!")
st.write("Hai! Web ini sengaja aku bikin buat pengingat kalau kita udah ngelewatin banyak hal seru bareng-bareng. *Scroll* ke bawah yaa! ✨")

st.markdown("---")

# 4. Bagian Galeri Foto
st.header("📸 our photos are my favorites")
st.write("kalian kangen ga sih?")

# Kita bikin 2 kolom biar fotonya berjejer rapi dan estetik
col1, col2 = st.columns(2)

with col1:
    # Ganti 'foto_kita1.jpg' dengan nama file foto kamu yang ada di folder yang sama
    st.image("https://drive.google.com/file/d/1S4oBwXnxCyaF479Jo24DyScWhs8cVe6G/view?usp=sharing", caption="bukber kita yang jadi favorite aku soalnya full member!", use_container_width=True)
    st.image("WhatsApp Image 2026-05-23 at 14.36.24 (2).jpeg", caption="walaupun kita gaada perpisahan tapi kita punya foto berkebaya bareng🤍", use_container_width=True)

with col2:
    st.image("https://drive.google.com/file/d/1VmwJPwN7jA5-7K7Vapa-dYZovgUlRuKP/view?usp=sharing", caption="selalu berdelapan terus ya!!!", use_container_width=True)
    st.image("https://drive.google.com/file/d/1J3cUQKq9wg-OLzLM-ADJBuc9pUTK1tpk/view?usp=sharing", caption="makasih! karena kalian, masa masa sma aku bener bener indah💕", use_container_width=True)

st.markdown("---")

# 5. Bagian Pesan Rahasia / Interaktif
st.header("💌 pesan dari cewe imut")

# Pakai fitur expander biar kesannya kayak ngebuka surat rahasia
with st.expander("Klik di sini ya dongo buat liatnya! 👇"):
    st.write("""
    Makasih ya guys udah selalu ada buat aku, udah mau dengerin cerita aku, 
    dan jadi orang yang paling ngertiin aku. gatau deh gimana jadinya kalo pas sma aku ga ketemu sama kalian, kalo aja waktu itu shinta ga so asik sama aku pas awal pembagian kelas, mungkin aku gaakan deket sama manusia tobrut nan jorang kayak dia, dan kalo aja aku gak masuk ke sangga rasunah, mungkin aku gaakan deket sama manusia cerewet kayak firda, manusia dongo kayak jeisyra, manusia kerdil kayak hasna, dan manusia islam tapi jorang kayak kaysa. mungkin kalo ga dari sana aku juga gaakan deket sama si bodoh merris, terus juga mungkin aku bakal asing lagi sama si tobrut hikmah. awalnya aku mikir kayak 'ah gaakan awet deh pertemanannya, soalnya di tiktok banyak yang bilang temen sma tuh pada toxic' tapi pas aku ketemu kalian....emang toxic sih,,,mulutnya maksudnya! apalagi si inisial jeisyra jeisyra itu! tapii gapapaaa justru itu yang serunya! sahabatan sama kalian tuh gakerasa.. baru aja kita deket pas kelas 10, eh sekarang kita udah pada lulus.....udah pada fokus sama jalan hidupnya masing masing, jadi dewasa gaenak ya? yang biasanya kita ketemu setiap hari, sekarang cuman bisa setahun 1 atau 2 kali, itu juga ga selalu full member ☹️ walaupun kayak gitu kita harus tetep sahabatan ya! sampe nikah, punya anak, punya cucu, punya cicit, sampe nenek nenek, till jannah!
    
    Semoga kita bisa sukses bareng-bareng dan nanti kita keliling dunia berdelapan! 
    *You are the best!* 🥐✨
    """)

# 6. Tombol Interaktif Tambahan
st.markdown("### tahu ga seberapa beruntungnya aku punya kalian?")
if st.button("Klik buat cari tahu! 👉👌"):
    st.success("Jawabannya: ♾️♾️♾️♾️♾️INFINITY!!!!!")
    st.snow() # Efek salju turun buat bonus kejutan
