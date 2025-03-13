# `gutenberg_ipsum2`— A better lorem ipsum

`gutenberg_ipsum2` is a simple wrapper function for [Markovify](https://github.com/jsvine/markovify) that allows you to generate semi-sensical filler text with Markov chains. Because it is a script, it's easy to use its output in other applications, such as [TextExpander](https://textexpander.com/) and [Keyboard Maestro](https://www.keyboardmaestro.com/main/).

## Installation

This uses [uv](https://docs.astral.sh/uv/) to manage virtual environments and package installation. [Install uv](https://docs.astral.sh/uv/#installation) and then run this:

    uv sync


## Basic usage

To generate five sentences from Dickens's *David Copperfield*, navigate to this directory in a terminal and run:

    uv run gutenberg_ipsum2.py corpora/copperfield.txt 5

In general, follow this syntax:

    uv run gutenberg_ipsum2.py corpus [num_sentences]


## Better usage

Instead of generating all your text in a terminal and copying/pasting it to other applications, it's best to use `gutenberg_ipsum2` with a program like TextExpander. 

For instance, we can make a new shell script snippet to put 5 sentences of *A Christmas Carol*-esque text where our cursor is. Create a new snippet with the following script:

    #!/usr/bin/env bash
    cd path/to/gutenberg-ipsum2/; uv run gutenberg_ipsum2.py corpora/christmascarol.txt 5

Then add an abbreviation for the snippet like `;ipchris`. I prefix all mine with `;ip` for "ipsum".

In any application, type `;ipchris` and get fresh new Dickens-trained text!

<img src="https://github.com/andrewheiss/gutenberg-ipsum2/raw/master/images/typing.gif" alt="Example expansion in TextExpander">


## Custom corpora

You can add whatever texts you want. Simply place them in the corpora folder (or anywhere really), and create new snippets in TextExpander to point to them. Here's a sampling of my collection:

![Example Gutenberg Ipsum snippets](https://github.com/andrewheiss/gutenberg-ipsum2/raw/master/images/text_expander.png)
