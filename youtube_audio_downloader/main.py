import yt_dlp
import os

def download_youtube_audio(url, is_playlist=False):
    # Créer le dossier de téléchargement s'il n'existe pas
    download_folder = "ytb_magic_dwld"
    os.makedirs(download_folder, exist_ok=True)
    
    # Options pour yt-dlp
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s'),
        'noplaylist': not is_playlist,  # Permet de télécharger une playlist complète si demandé
    }

    # Télécharger l'audio
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

if __name__ == "__main__":
    while True:
        choice = input("Voulez-vous télécharger une playlist (P) ou une seule vidéo (V) ? (Q pour quitter) : ").strip().lower()
        if choice == 'q':
            print("Au revoir!")
            break
        elif choice == 'p':
            url = input("Entrez le lien de la playlist : ").strip()
            download_youtube_audio(url, is_playlist=True)
        elif choice == 'v':
            url = input("Entrez le lien de la vidéo : ").strip()
            download_youtube_audio(url, is_playlist=False)
        else:
            print("Choix invalide, veuillez recommencer.")
