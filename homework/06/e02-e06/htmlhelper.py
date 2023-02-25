
def generate_html_page(title ="My title", content="<p>Hello</p>"):
    """
    Function will return a valid html5 page as string.
    """
    html_page = f"""<!DOCTYPE html>
<html lang=\"en\">
  <head>
    <meta charset=\"utf-8\">
    <title>{title}</title>
  </head>
  <body>
    {content}
  </body>
</html>"""

    return html_page