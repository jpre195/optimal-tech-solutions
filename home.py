# from fasthtml.common import *

# app, rt = fast_app()

# @rt('/')
# def get(): return Div(P('Hello World'), hx_get = '/change')

# serve()

from fasthtml import FastHTML

site = FastHTML(output_dir = 'site')

# site.add_page("index.html", """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>FastHTML Website</title>
#     <link rel="stylesheet" href="css/styles.css">
# </head>
# <body>
#     <h1>Welcome to My FastHTML Website</h1>
#     <img src="assets/logo.png" alt="Logo">
# </body>
# </html>
# """)

print(dir(site))

site.generate(use_common = True)
