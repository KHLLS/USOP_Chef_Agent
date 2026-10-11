# USOP Chef Agent

Agent koki berbasis LangChain yang menganalisis gambar bahan makanan dan menghasilkan rekomendasi resep masakan Indonesia yang halal serta dapat dieksekusi berdasarkan bahan yang tampak di foto.

## Fitur utama

- Membuka pemilih file gambar lokal menggunakan Tkinter.
- Mengubah file gambar menjadi data URL base64 agar dapat dikirim ke model.
- Membuat pesan `HumanMessage` yang berisi gambar dan prompt.
- Menjalankan agent dengan model OpenAI-compatible melalui endpoint Kenari.
- Menggunakan alat pencarian web Tavily untuk menambah informasi relevan.
- Mencetak hasil analisis dan rekomendasi resep ke console.

## Struktur proyek

- `main.py` — bootstrap aplikasi, inisialisasi model, membuat agent, dan menjalankan invoke.
- `prompt.py` — berisi `CHEF_PROMPT` dan `SYSTEM_CHEF_PROMPT` yang menjadi instruksi utama agent.
- `tools.py` — tool pencarian web berbasis Tavily.
- `image_decoder.py` — fungsi untuk memilih gambar dan membangun payload gambar.
- `requirements.txt` — daftar dependency Python yang dibutuhkan.

## Teknologi yang dipakai

- Python
- LangChain
- LangChain OpenAI / OpenAI-compatible model
- Kenari API endpoint
- Tavily API
- Tkinter untuk file picker

## Persyaratan

- Python 3.10+
- Koneksi internet untuk akses API
- API key dari Kenari dan Tavily

## Setup

1. Buat environment virtual (opsional tapi disarankan):

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

2. Install dependensi:

   ```bash
   pip install -r requirements.txt
   ```

3. Buat file `.env` di root project dengan variabel berikut:

   ```env
   MODELS=gpt-4o-mini
   KENARI_API_KEY=your_kenari_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

   Catatan:
   - `MODELS` adalah model yang tersedia di endpoint Kenari.
   - `KENARI_API_KEY` dipakai untuk autentikasi ke endpoint `https://kenari.id/v1`.
   - `TAVILY_API_KEY` dibutuhkan oleh tool `web_search` di `tools.py`.

## Menjalankan aplikasi

```bash
python main.py
```

Setelah itu, akan muncul dialog pemilihan file gambar. Pilih foto bahan makanan yang ingin dianalisis. Program akan mengirim gambar ke agent dan menampilkan hasil analisis resep di terminal.

## Output yang dihasilkan

Agent akan mencoba memberikan:

- daftar bahan yang teridentifikasi dari foto
- asumsi bumbu dapur yang tersedia
- 2 sampai 3 rekomendasi resep masakan Indonesia
- waktu persiapan dan memasak
- langkah-langkah pembuatan
- catatan substitusi halal jika diperlukan

## Catatan implementasi

- `main.py` memakai `create_agent` dan `agent.invoke()` untuk memproses input.
- `image_decoder.py` membangun `HumanMessage` dengan gambar, tetapi teks yang dikirim saat ini adalah literal `"prompt"` sesuai implementasi yang ada.
- Prompt utama untuk analisis dan resep ada di `prompt.py`, bukan melalui argumen CLI.
