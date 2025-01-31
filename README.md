
# YouTube Audio Downloader

Ce projet est un script Python interactif permettant de télécharger l'audio de vidéos YouTube ou de playlists entières en MP3. Les fichiers téléchargés sont enregistrés dans le dossier `ytb_magic_dwld`.

## Prérequis

Avant d'utiliser ce script, assurez-vous d'avoir installé :

- Python (>=3.7)
- [Poetry](https://python-poetry.org/) pour la gestion des dépendances

### Installation de Poetry

Si Poetry n'est pas installé, utilisez la commande suivante :

```sh
curl -sSL https://install.python-poetry.org | python3 -
```

Ajoutez ensuite Poetry au PATH si nécessaire :

```sh
export PATH="$HOME/.local/bin:$PATH"
```

## Installation du projet

Clonez ce dépôt et installez les dépendances avec Poetry :

```sh
git clone <URL_DU_REPO>
cd youtube_audio_downloader
poetry install
```

## Utilisation

Exécutez le script via Poetry :

```sh
poetry run python youtube_audio_downloader/main.py
```

Une fois lancé, le script vous demandera si vous souhaitez télécharger une **playlist** ou une **vidéo unique**. Saisissez le lien et le téléchargement commencera automatiquement.
