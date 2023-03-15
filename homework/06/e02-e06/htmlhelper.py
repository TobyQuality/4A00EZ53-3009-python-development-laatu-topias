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

def generate_bmi_form(content=""):
  bmi_form=f"""<h1>BMI</h1>
    <form action="#content">
        <input type="number" placeholder="mass" id="mass" min="0" max="500" name="mass">
        <label for="mass" >kg</label>
        <input type="number" placeholder="height" id="height" step="0.01" min="0.00" max="3.0" name="height">
        <label for="height" >m</label>
        <button>Calculate</button>
    </form>
    <div id="content">{content}</div>"""
  bmi_page = generate_html_page("bmi", bmi_form)
  return bmi_page

