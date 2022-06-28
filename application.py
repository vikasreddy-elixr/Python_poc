import os
import sys
import click


@click.command(name="search")
@click.option('--path', required=True)
@click.option('--word', required=True)
def word_search(path, word):
    """takes the file path and the word from the user and search for existence of the word inside the file from the
    path """
    validation(path, word)

    if path.endswith(".txt") | path.endswith(".json"):
        try:
            with open(os.path.join(os.path.dirname(__file__), path), 'r') as input_file:
                lower_case_file = input_file.read()
                content = lower_case_file.lower()
                lower_case_word = word.lower()
            x = content.__contains__(lower_case_word)
            count = content.count(lower_case_word)
            if x:
                if count > 1:
                    sys.exit("Word Found, Repeated " + str(count) + " times")
                sys.exit("Word Found, Repeated " + str(count) + " time")
            else:
                click.echo("Word Not found")
        except FileNotFoundError:
            click.echo("The file does not exist in the given path")
    else:
        click.echo("Unsupported File Format")


def validation(path, word):
    """ validates the path and word provided by the user """
    if len(path.format(path)) == 0:
        click.echo("please enter valid path")
        sys.exit(-1)
    if len(word) == 0:
        click.echo("please enter the searchWord")
        sys.exit(-1)


if __name__ == '__main__':
    if len(sys.argv) == 5:
        word_search()
    else:
        sys.exit("Either path or the word is missing.")
