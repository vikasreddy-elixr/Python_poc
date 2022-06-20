import os
import sys
import click


@click.command(name="search")
@click.option('--path', default='')
@click.option('--word', default='')
def word_search(path, word):
    """takes the file path and the word from the user and search for existence of the word inside the file from the
    path """
    validation(path, word)

    if path.endswith(".txt") | path.endswith(".json"):
        try:
            with open(os.path.join(os.path.dirname(__file__), path), 'r') as input_file:
                content = input_file.read()
            x = content.__contains__(word)
            count = content.count(word)
            if x:
                sys.exit("searchWord Found " + str(count) + " times")
            else:
                click.echo("searchWord Not found")
        except FileNotFoundError:
            click.echo("The file does not exist in the given path")
    else:
        click.echo("Please Enter the Valid Path")


def validation(path, word):
    """ validates the path and word provided by the user """
    if len(path.format(path)) == 0:
        click.echo("please enter valid path")
        sys.exit(-1)
    if len(word) == 0:
        print("please enter the searchWord")
        sys.exit(-1)


if __name__ == '__main__':
    word_search()
