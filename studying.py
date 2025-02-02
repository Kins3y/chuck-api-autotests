import requests
import unittest

class ChuckNorrisAPI:
    """API jokes about Chuck Norris."""

    BASE_URL = 'https://api.chucknorris.io/'
    JOKES_ENDPOINT = 'jokes/'
    CATEGORIES_ENDPOINT = 'categories'
    RANDOM_JOKE = 'random'

    @classmethod
    def get_all_categories(cls):
        """List of all categories"""
        url = cls.BASE_URL + cls.JOKES_ENDPOINT + cls.CATEGORIES_ENDPOINT
        print(f"[INFO] Requesting a list of categories: {url}")
        response = requests.get(url)
        response.raise_for_status()
        categories = response.json()
        print(f"[SUCCESS] Got {len(categories)} categories: {categories}")
        return categories

    @classmethod
    def get_random_joke_by_category(cls, category):
        """Random joke from a specific category"""
        url = f"{cls.BASE_URL}{cls.JOKES_ENDPOINT}{cls.RANDOM_JOKE}?category={category}"
        print(f"\n[INFO] Requesting a random joke for category: {category}")
        print(f"[INFO] Request URL: {url}")
        response = requests.get(url)
        response.raise_for_status()
        joke = response.json().get("value")
        print(f"[SUCCESS] The joke: {joke}")
        return joke


class TestChuckNorrisJokes(unittest.TestCase):
    """API Tests for Chuck Norris jokes"""

    def setUp(self):
        """Starting initialization"""
        print("\n[SETUP] Preparing for test run...")
        self.api = ChuckNorrisAPI()

    def test_all_categories(self):
        """Assertion of category list and their jokes"""
        print("\n[TEST] Testing response of categories' list...")
        categories = self.api.get_all_categories()

        # Testing number of categories
        print(f"[ASSERT] Testing if amount of categories is 16")
        self.assertEqual(len(categories), 16, "ERROR: Wrong number of categories")
        print("[SUCCESS] Correct number of categories")

        for category in categories:
            joke = self.api.get_random_joke_by_category(category)
            print(f"[ASSERT] Checking if joke in category {category} is a string")
            self.assertIsInstance(joke, str, f"ERROR: Joke of category {category} is not a string")
            print("[SUCCESS] Joke received correctly\n")


if __name__ == "__main__":
    print("[INFO] Initializing tests...")
    unittest.main()
