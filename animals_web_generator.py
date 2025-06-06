import json


def load_data(file_path):
    """Loads data from the JSON file."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_template(file_path):
    """Loads HTML template content from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def serialize_animal(animal):
    """
    Convert a single animal object into a formatted HTML <li> block.
    """
    output = '<li class="cards__item">\n'

    if "name" in animal:
        output += f'  <div class="card__title">{animal["name"]}</div>\n'

    output += '  <p class="card__text">\n'

    if "characteristics" in animal:
        characteristics = animal["characteristics"]
        if "diet" in characteristics:
            output += f'    <strong>Diet:</strong> {characteristics["diet"]}<br/>\n'
        if "type" in characteristics:
            output += f'    <strong>Type:</strong> {characteristics["type"]}<br/>\n'

    if "locations" in animal and animal["locations"]:
        output += f'    <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'

    return output


def generate_animals_info_string(data):
    """
    Generate an HTML-formatted string containing all animals' information.
    """
    output = ""
    for animal in data:
        output += serialize_animal(animal)
    return output


def build_html_page(output_string, template_string, output_file):
    """
    Replace the placeholder in the template with the output string
    and write to a new HTML file.
    """
    html_content = template_string.replace("__REPLACE_ANIMALS_INFO__", output_string)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)


def main():
    animals_data = load_data("animals_data.json")
    template = load_template("animals_template.html")
    animals_info_str = generate_animals_info_string(animals_data)
    build_html_page(animals_info_str, template, "animals.html")


if __name__ == "__main__":
    main()

