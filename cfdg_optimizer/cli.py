# Jordan Cazamias
# CFDG Optimizer
# July 2014

# cli.py: Command Line Interface functionality

import click

import main

@click.command()
@click.argument('grammar-file')
@click.argument('test-images-dir')
def main(grammar_file, test_images_dir):
    """
    Run main optimization function from command line.

    :param grammar_file: Name of augmented CFDG file to start from
    :param test_images_dir: Name of directory where test images
    for exemplar scoring can be found
    """
    click.echo("Optimizing grammar '{0}' using the "
               "images in directory '{1}'..."
               .format(grammar_file, test_images_dir))
    main.run(grammar_file, test_images_dir)
