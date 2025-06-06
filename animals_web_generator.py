# import requests
#
#
# API_URL = "https://api.api-ninjas.com/v1/animals?name="
# API_KEY = "szSWwT9TDE/6KodUxjfdog==AOjQXTPTjXgqgfVS"
#
#
# def fetch_data_from_api(animal_name):
#     """
#     Fetches animal data from the API based on user-provided animal name.
#     """
#     headers = {"X-Api-Key": API_KEY}
#     url = f"{API_URL}{animal_name}"
#     #print(f"Fetching from: {url}")
#
#     response = requests.get(url, headers=headers)
#
#     # print(f"Status Code: {response.status_code}")  # DEBUG
#     # print(f"Response Text: {response.text}")
#
#     if response.status_code == 200:
#         return response.json()
#     else:
#         raise Exception(f"API request failed with status code {response.status_code}: {response.text}")


import data_fetcher


def load_template(file_path):
    """Loads HTML template content from a file."""
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def serialize_animal(animal):
    """
    Convert a single animal object into a formatted HTML <li> block.
    """
    output = '<li class="cards__item">\n'

    #if "name" in animal:
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

    # return "".join(serialize_animal(animal) for animal in data)


def build_html_page(output_string, template_string, output_file):
    """
    Replace the placeholder in the template with the output string
    and write to a new HTML file.
    """
    html_content = template_string.replace("__REPLACE_ANIMALS_INFO__", output_string)
    with open(output_file, "w", encoding="utf-8") as file:
        file.write(html_content)


def main():
    animal_name = input("Enter a name of an animal: ").strip()
    data = data_fetcher.fetch_data(animal_name)
    template = load_template("animals_template.html")

    if not data:
        html_msg = f'''
        <h2 style="color: red; text-align: center; padding-top: 2em;">
            The animal "{animal_name}" does not exist.
        </h2>
        '''
        build_html_page(html_msg, template, "animals.html")
    else:
        animals_info_str = generate_animals_info_string(data)
        build_html_page(animals_info_str, template, "animals.html")

    print("Website was successfully generated to the file animals.html.")


if __name__ == "__main__":
    main()

