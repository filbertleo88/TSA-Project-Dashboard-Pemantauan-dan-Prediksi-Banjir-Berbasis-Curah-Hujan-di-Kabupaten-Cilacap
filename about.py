import streamlit as st

def app():
    st.title("Tentang Kami")

    col_1, col_2, col_3 = st.columns(3)
    with col_1:
        st.header("Visi")
        st.markdown("""
        Menjadi penyedia solusi inovatif dalam mengatasi risiko banjir dan memberikan informasi yang akurat 
        untuk pengambilan keputusan di Kabupaten Cilacap.
        """)
    with col_2:
        st.header("Misi")
        st.markdown("""
        1. Mengumpulkan dan menganalisis data kejadian banjir serta curah hujan dengan akurat.
        2. Mengembangkan model prediksi banjir yang handal berdasarkan data historis.
        3. Menyediakan dashboard interaktif untuk memantau dan meramalkan risiko banjir.
        4. Menyebarkan informasi mengenai risiko banjir kepada masyarakat secara efektif.
        """)
    with col_3:
        st.header("Tujuan")
        st.markdown("""
        1. Menyediakan sumber informasi yang terpercaya terkait risiko banjir di Kabupaten Cilacap.
        2. Meningkatkan kewaspadaan dan kesiapsiagaan masyarakat terhadap potensi risiko banjir.
        3. Mendukung upaya mitigasi dan penanggulangan risiko banjir di tingkat lokal.
        """)
    
    st.header("Dataset yang Digunakan")
    st.markdown("""
    Kami menggunakan beberapa dataset dalam projek ini. Berikut adalah beberapa di antaranya:
    1. Data Kejadian Banjir di Indonesia - [BNPB](https://dibi.bnpb.go.id/)
    2. Data Curah Hujan Kabupaten Cilacap - [World Weather Online](https://www.worldweatheronline.com/cilacap-weather-history/central-java/id.aspx)
    """)

    st.header("Model yang Digunakan")
    st.markdown("""
    #### Model Prediksi:
    Kami menggunakan dua model prediksi untuk memprediksi kejadian banjir:
    
    - Model CatBoost dengan nilai F1-Score = 0.972222
    - Model Xgboost dengan nilai F1-Score = 0.963134

    #### Model Forecast (Exponential Smoothing):
    Kami menggunakan model Exponential Smoothing untuk meramalkan curah hujan pada berbagai interval waktu:

    - Model hujan 0: RMSE = 1.1599756093958493, MAE = 0.943551827957549
    - Model hujan 300: RMSE = 1.1599756093958493, MAE = 0.943551827957549
    - Model hujan 600: RMSE = 0.4784673961456537, MAE = 0.25224162915775367
    - Model hujan 900: RMSE = 0.5375419675168472, MAE = 0.20652473580345712
    - Model hujan 1200: RMSE = 1.26999279431073, MAE = 0.6273700864505144
    - Model hujan 1500: RMSE = 2.738106863694104, MAE = 1.6517205794815994
    - Model hujan 2100: RMSE = 0.6421829957267302, MAE = 0.4293358719090209
""")

    st.header("Proses Analisis")
    st.markdown("""
        Untuk memahami lebih lanjut mengenai proses analisis, silakan kunjungi link berikut:
        - [Preprocessing Data](https://colab.research.google.com/drive/1vpr6R9BGfSyeD71eOa_rdhgqbOzRA2Nq?usp=drive_link): Proses persiapan dan pembersihan data sebelum pemodelan.
        - [Pemodelan Forecast Curah Hujan](https://colab.research.google.com/drive/1ZMNm13_I4cEj6odZU_VlbDkt2jltX-xd?usp=drive_link): Tahapan pembentukan dan validasi model forecast curah hujan.
        - [Pemodelan Prediksi Banjir](https://colab.research.google.com/drive/14_ModmFTbcgpm_h9RXRNjMwHxnLLpi73?usp=drive_link): Langkah-langkah dalam membangun model prediksi banjir.
    """)


    st.header("Teknologi / Tools yang Digunakan")
    st.markdown("""
        - **Streamlit:** Untuk pembuatan antarmuka pengguna.
        - **Pandas:** Untuk manipulasi dan analisis data.
        - **Joblib:** Untuk menyimpan dan memuat model pembelajaran mesin.
        - **Plotly Express dan Plotly Graph Objects:** Library untuk membuat visualisasi data interaktif.
    """)

    st.header("Referensi Tambahan")
    st.markdown("""
        - **GitHub Project:** [Link ke Proyek di GitHub](https://github.com/username/nama-proyek)
        - **Presentasi PowerPoint:** [Link ke Presentasi PowerPoint](https://link-presentasi-powerpoint)
    """)

    st.header("Kontak")
    st.markdown("""
        Dashboard ini merupakan projek akhir dari Program DTS TSA 2023 yang dikerjakan oleh kelompok 4 (Kelas A).
        Jika Anda memiliki pertanyaan atau umpan balik, silakan hubungi kami melalui email:
        - Alfito: [alfito@example.com](mailto:alfito@example.com)
        - Ziya: [ziya@example.com](mailto:ziya@example.com)
        - Filbert Leonardo: [filbertleo88@gmail.com](mailto:filbertleo88@gmail.com)
        - Bayu: [bayu@example.com](mailto:bayu@example.com)
        - Siti: [siti@example.com](mailto:siti@example.com)
        - Amanda: [amanda@example.com](mailto:amanda@example.com)
    """)
