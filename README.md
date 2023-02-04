# Pelican Custom CSS

Pelican Custom CSS makes it easy to embed custom CSS into individual Pelican articles and pages.

## How

`pip install pelican-custom-css`

Next, create a `css` directory in your `content` directory.

```
website/
├── content
│   ├── css/
│   │   ├── your_custom_style1.css
│   │   └── your_custom_style2.css
│   ├── article1.md
│   └── pages
│       └── about.md
└── pelicanconf.py
```

And then add each resource as a comma-separated file name in the `CSS` tag:

```
Title: Mejor sin Wordpress
Date: 2017-02-09 18:51
Tags: programación, Wordpress, generador de páginas estáticas, generador de sitios web estáticos, rendimiento, eficiencia, comodidad, desventajas
Category: Desarrollo web
Author: jorgesumle
Slug: mejor-sin-wordpress
CSS: your_custom_style1.css, your_custom_style2.css
```

Finally, in your base template (likely named `base.html`), you need
to add the following in your `<head>` tag:

```
{% if article %}
    {% if article.styles %}
        {% for style in article.styles %}
            {{ style|format(SITEURL) }}
        {% endfor %}
    {% endif %}
{% endif %}
```

So, the template I use for my blog now looks like the following:

```
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset=utf-8">
    <title>{% block title %} {{SITENAME}} {% endblock %}</title>
    <link rel="stylesheet" href="{{ SITEURL }}/theme/css/style.css" type="text/css">
    {% if article %}
        {% if article.styles %}
            {% for style in article.styles %}
                {{ style|format(SITEURL) }}
            {% endfor %}
        {% endif %}
    {% endif %}
  </head>
  <body>
    <div class=container>
        {% block header %}
            {% include "header.html" %}
        {% endblock %}

        <div class="content">
        {% block content %} {% endblock %}
        </div>

        {% block footer %}
            {% include "footer.html" %}
        {% endblock %}
    </div>
  </body>
</html>
```

The previous code only works for articles. For most people, that's
enough. If you want to enable custom CSS in pages too insert the
following code your `<head>` tag...

```
{% if page %}
    {% if page.styles %}
        {% for style in page.styles %}
            {{ style|format(SITEURL) }}
        {% endfor %}
    {% endif %}
{% endif %}
```

That's it! You can now generate and publish your site normally, for example using `ghp-import` if you're using Github Pages or the standard `make html` or `make publish` commands from Pelican and your CSS will be copied and referenced in the right places.