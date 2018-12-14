from PIL import Image
import click
from os import path
import os
from glob import glob


ICON_SIZE = (32, 32)
ICON_DIR = 'icons'
THUMBNAIL_DIR = 'thumbnails'

@click.group()
def main():
    """
        CLI to resize images.
    """
    # click.echo(
    #     click.style("Started resizing....", fg='red')
    # )
    # im = Image.open(src)
    # size = (width, height)
    # original, ext = src.split(".")
    # filename = f"{original}.{image_type}"
    # resized_image = im.resize(size)
    # resized_image.save(filename)
    # click.echo(
    #     click.style("Finished resizing...", fg='red')
    # )

@main.command()
@click.argument("src", type=click.Path(exists=True))
@click.option("--width", default=600, type=int, help="width of the image")
@click.option("--height", default=400, type=int, help="height of the image")
@click.option("--image-type", default="png", type=str, help="format of the saved image")
def resize(src, width, height, image_type):
    click.echo(
        click.style("Started resizing....", fg='red')
    )
    im = Image.open(src)
    size = (width, height)
    original, ext = src.split(".")
    filename = f"{original}.{image_type}"
    resized_image = im.resize(size)
    resized_image.save(filename)
    click.echo(
        click.style("Finished resizing...", fg='red')
    )

@main.command()
@click.argument("dir", type=click.Path(exists=True))
@click.option('--width', type=int, help='width of the thumbail image', required=True)
@click.option('--height', type=int, help='height of the thumbnail image', required=True)
@click.option("--ext", type=str, default='png', help="extension of the images to change to thumbnails")
def thumbnail(dir, width, height, ext):
    click.echo(
        click.style("Started thumbnail generation....", fg='red')
    )
    size = (width, height)
    dest_dir = path.join(dir, THUMBNAIL_DIR)
    if not path.exists(dest_dir):
        os.makedirs(dest_dir)
    image_files = glob(path.join(dir, f'*.{ext}'))
    for image_file in image_files:
        original, typ = path.basename(image_file).split(".")
        filename =  path.join(dest_dir, f"{original}.{ext}")
        click.echo(
            click.style(f'Processing {filename}', fg='yellow')
        )
        im = Image.open(image_file)
        im.thumbnail(size)
        im.save(filename)
    click.echo(
        click.style("Finished thumbnail generation...", fg='red')
    )

@main.command()
@click.argument("dir", type=click.Path(exists=True))
@click.option("--ext", default="png", type=str, help="format of the saved image")
def iconify(dir, ext):
    click.echo(
        click.style('Started iconify...', fg='red')
    )
    dest_dir = path.join(dir, ICON_DIR)
    if not path.exists(dest_dir):
        os.makedirs(dest_dir)
    image_files = glob(path.join(dir, f'*.{ext}'))
    for image_file in image_files:
        original, typ = path.basename(image_file).split(".")
        filename =  path.join(dest_dir, f"{original}.{typ}")
        click.echo(
            click.style(f'Processing {filename}', fg='yellow')
        )
        im = Image.open(image_file)
        im.thumbnail(ICON_SIZE)
        im.save(filename)
    click.echo(
        click.style('Finished iconify...', fg='red')
    )

if __name__ == "__main__":
    main()
