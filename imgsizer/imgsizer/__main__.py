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
    click.echo("Started resizing....")
    im = Image.open(src)
    size = (width, height)
    original, ext = src.split(".")
    filename = f"{original}.{image_type}"
    im.thumbnail(size)
    im.save(filename)
    click.echo("Finished resizing...")


if __name__ == "__main__":
    main()
