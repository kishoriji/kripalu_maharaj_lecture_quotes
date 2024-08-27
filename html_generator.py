import collections
import os


def generate_homepage(group_names, output_file):
    title = "One-liner quotes by Kripalu Maharaj"
    html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f4f4f4;
            display: flex;
            justify-content: center;
            align-items: flex-start;
            min-height: 100vh;
        }}
        .container {{
            width: 80%;
            max-width: 600px;
            text-align: center;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        h1 {{
            margin-bottom: 20px;
            font-size: 26px;
            color: #003366;
        }}
        ul {{
            list-style: none;
            padding: 10px;
        }}
        li {{
            margin-bottom: 10px;
            padding: 20px 15px;
            border: 1px solid #ccc;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
            font-size: 22px;
            text-align: center;
        }}
        li:hover {{
            background-color: #f0f0f0;
        }}
        a {{
            text-decoration: none;
            color: #402612;
            display: block;
            width: 100%;
            height: 100%;
        }}
        a:hover {{
            color: #007BFF;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <ul>
            {links}
        </ul>
    </div>
</body>
</html>
    """

    # Generate the list of links
    links_html = '\n'.join(f'<li><a href="{name}.html">{name}</a></li>' for name in group_names)

    # Create the final HTML content
    final_html = html_template.format(title=title, links=links_html)

    # Write the HTML content to the output file
    with open(os.path.join('public', output_file), 'w') as file:
        file.write(final_html)


def generate_group_page(title, item_list, output_file):
    # Define the HTML structure with placeholders for title and items
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f7f7f7;
            margin: 0;
            padding: 20px;
        }}
        .container {{
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }}
        h1 {{
            text-align: center;
            font-size: 36px;
            color: #402612;
            margin-bottom: 40px;
        }}
        .post-list {{
            list-style-type: none;
            padding: 0;
            margin: 0;
        }}
        .post-list li {{
            padding: 20px;
            margin-bottom: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }}
        .post-list li h2 {{
            font-size: 22px;
            margin: 0 0 10px;
            color: #767a68;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>{title}</h1>
        <ul class="post-list">
"""

    # Add each item in the item_list to the HTML content
    for item in item_list:
        html_content += f"""
            <li>
                <h2>{item}</h2>
            </li>
"""
    # Close the HTML tags
    html_content += """
        </ul>
    </div>
</body>
</html>
"""

    # Write the HTML content to the output file
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)


def read_group_names_with_titles():
    titles_for_groups = collections.defaultdict(list)
    basepath = 'quotes'
    for filename in os.listdir(basepath):
        if not filename.endswith('.txt'):
            continue
        name = filename.split('.')[0]
        with open(os.path.join(basepath, filename), encoding='utf-8') as f:
            for line in f:
                titles_for_groups[name].append(line.strip())
    return titles_for_groups


def main():
    titles_for_groups = read_group_names_with_titles()
    output_homepage_file = 'index.html'
    print(titles_for_groups.keys())
    generate_homepage(titles_for_groups.keys(), output_homepage_file)
    # Generate individual group pages
    for group_name, titles in titles_for_groups.items():
        output_group_page_file = f'public/{group_name}.html'
        generate_group_page(group_name, titles, output_group_page_file)


if __name__ == '__main__':
    main()
