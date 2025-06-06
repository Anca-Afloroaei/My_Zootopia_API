import requests

API_URL = "https://api.api-ninjas.com/v1/animals?name="
API_KEY = "szSWwT9TDE/6KodUxjfdog==AOjQXTPTjXgqgfVS"


def fetch_data(animal_name):
    """
    Fetches animals data for the given animal name from the API.
    Returns: a list of animal dictionaries or an empty list if not found.
    """
    url = f"{API_URL}{animal_name}"
    headers = {"X-Api-Key": API_KEY}

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()
            return data if isinstance(data, list) else []
        else:
            print(f"API request failed with status code {response.status_code}: {response.text}")
            return []
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return []
