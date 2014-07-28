# Jordan Cazamias
# CFDG Optimizer
# July 2014

import click

import main

@click.command()
@click.argument('grammar-file')
@click.argument('test-images-dir')
def main(grammar_file, test_images_dir):
    click.echo("Optimizing grammar '{0}' using the "
               "images in directory '{1}'..."
               .format(grammar_file, test_images_dir))
    main.run(grammar_file, test_images_dir)
