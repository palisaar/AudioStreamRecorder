import click
import AudioRecorder

'''
Autor: Lennart Palisaar
20211638
'''


@click.command()
@click.argument('url')
@click.option('--name', default='test')
@click.option('--length', default=3)
@click.option('--block_size', default=40)
def on_enter(url, name, length, block_size):
    print('recording imminent')
    AudioRecorder.record_audio(name, url, length, block_size)


if __name__ == '__main__':
    on_enter()