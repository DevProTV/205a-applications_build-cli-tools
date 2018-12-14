from PIL import Image
import click


@click.command()
@click.argument("src", type=click.Path(exists=True))
@click.option("--width", default=600, type=int, help="width of the image")
@click.option("--height", default=400, type=int, help="height of the image")
@click.option("--image-type", default="png", type=str, help="format of the saved image")
def main(src, width, height, image_type):
    """
        CLI to resize images.
    """
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

def resize(src, width, height, image_type):
    pass

def thumbnail(src, width, height, image_type):
    pass

def iconify(src):
    pass

if __name__ == "__main__":
    main()
