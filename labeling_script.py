from pathlib import Path
import shutil
import click

from audio_augmentation import Audio

@click.command()
@click.argument('audio_path')
def label_ww(audio_path):
    audio_path = Path(audio_path)
    assert audio_path.exists(), 'Please provide a valid path to the folder ' \
                          'containing the audios'
    positives_path = audio_path / 'positives'
    positives_path.mkdir(exist_ok=True)
    negatives_path = audio_path/ 'negatives'
    negatives_path.mkdir(exist_ok=True)
    for audio_file in audio_path.glob('*.wav'):
        print('\n--------------------------')
        print('listening to audio {}'.format(audio_file.name))
        audio = Audio.from_file(audio_file)
        audio.play()
        while click.confirm('Do you want to play it again?'):
            audio.play()
        if click.confirm('\nIs the file a true negative?'):
            shutil.move(audio_file, negatives_path/audio_file.name)
        else:
            shutil.move(audio_file, positives_path/audio_file.name)
        if not click.confirm('Audio file moved. Do you want to continue'):
            exit()

if __name__ == '__main__':
    label_ww()