import requests
import pytest

class ChuckNorrisAPI:
    """Interacting with the Chuck Norris jokes API"""

    BASE_URL = 'https://api.chucknorris.io/'
    JOKES_ENDPOINT = 'jokes/'
    CATEGORIES_ENDPOINT = 'categories'
    RANDOM_JOKE = 'random'

    @classmethod
    def get_all_categories(cls) -> list[str]:
        """Fetches all available joke categories"""
        url = cls.BASE_URL + cls.JOKES_ENDPOINT + cls.CATEGORIES_ENDPOINT
        print(f"Sending request to fetch all categories: {url}")
        response = requests.get(url)
        response.raise_for_status()
        categories: list[str] = response.json()
        print(f"Retrieved {len(categories)} categories: {categories}")
        return categories

    @classmethod
    def get_random_joke_by_category(cls, category: str) -> str:
        """Fetches a random joke from the specified category."""
        url = f"{cls.BASE_URL}{cls.JOKES_ENDPOINT}{cls.RANDOM_JOKE}?category={category}"
        print(f"\nRequesting a random joke for category: {category}")
        print(f"Request URL: {url}")
        response = requests.get(url)
        response.raise_for_status()
        joke: str = response.json().get("value", "No joke found")
        print(f"Retrieved joke: {joke}")
        return joke


@pytest.fixture
def api() -> ChuckNorrisAPI:
    """Fixture to initialize the ChuckNorrisAPI instance"""
    print("\nInitializing ChuckNorrisAPI instance...")
    return ChuckNorrisAPI()


def test_all_categories(api: ChuckNorrisAPI) -> None:
    """Test: Fetching the list of joke categories"""
    print("\nChecking category retrieval...")
    categories = api.get_all_categories()

    # Validate category count
    print(f"Checking that the number of categories is 16")
    assert len(categories) == 16, "ERROR: Incorrect number of categories"
    print("Category count is correct")


@pytest.mark.parametrize("category", ChuckNorrisAPI.get_all_categories())
def test_random_joke_by_category(api: ChuckNorrisAPI, category: str) -> None:
    """Testing fetching a random joke for each category"""
    joke = api.get_random_joke_by_category(category)
    print(f"Checking if the joke for category '{category}' is a string")
    assert isinstance(joke, str), f"ERROR: Joke in category '{category}' is not a string"
    print("Joke retrieved successfully\n")


if __name__ == "__main__":
    print("Running tests with pytest...")
    pytest.main()
