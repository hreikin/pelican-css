#!/usr/bin/env python3
# pelican-css: embed custom CSS easily
# Copyright (C) 2017 Jorge Maldonado Ventura

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
Embed CSS files for Pelican
===========================

This plugin allows you to easily embed CSS files in the header of individual
articles or pages. The CSS files are embedded using the HTML <link> tag
inside the <head> tag.
"""

import os
import shutil

from pelican import signals


def format_css(gen, metastring, formatter):
    """
    Create a list of URL-formatted style tags
    Parameters
    ----------
    gen: generator
        Pelican Generator
    metastring: string
        metadata['scripts'] or metadata['styles']
    formatter: string
        String format for output.
    Output
    ------
    List of formatted strings
    """
    metalist = metastring.replace(' ', '').split(',')
    site_url = '%s'
    return [formatter.format(site_url, x) for x in metalist]


def copy_resources(src, dest, file_list):
    """
    Copy files from content folder to output folder
    Parameters
    ----------
    src: string
        Content folder path
    dest: string,
        Output folder path
    file_list: list
        List of files to be transferred
    Output
    ------
    Copies files from content to output
    """
    if not os.path.exists(dest):
        os.makedirs(dest)
    for file_ in file_list:
        file_src = os.path.join(src, file_)
        shutil.copy2(file_src, dest)


def add_tags(gen, metadata):
    """
    It will add the CSS to the article
    """
    if 'css' in metadata.keys():
        style = '<link rel="stylesheet" href="{0}/css/{1}" type="text/css">'
        metadata['styles'] = format_css(gen, metadata['css'], style)


def move_resources(gen):
    """
    Move CSS files from css folder to output folder
    """
    css_files = gen.get_files('css', extensions='css')

    css_dest = os.path.join(gen.output_path, 'css')
    copy_resources(gen.path, css_dest, css_files)


def register():
    """
    Plugin registration
    """
    signals.article_generator_context.connect(add_tags)
    signals.page_generator_context.connect(add_tags)
    signals.article_generator_finalized.connect(move_resources)
