import requests

API_URL = "https://jobfair.nordeus.com/jf24-fullstack-challenge/test"

def fetch_grid_data():
    """
    Fetches grid data from the backend API.
    
    Returns:
        list of list of int: A 2D list representing the grid heights.
        
    Raises:
        Exception: If the request fails or data is invalid.
    """
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()
        data = response.text.strip().split("\n")
        
        grid = []
        for line in data:
            row = list(map(int, line.split()))
            if len(row) != 30:
                raise ValueError("Each row must contain exactly 30 integer values.")
            grid.append(row)
        
        if len(grid) != 30:
            raise ValueError("The grid must contain exactly 30 rows.")
        
        return grid
    except requests.RequestException as e:
        print(f"Error fetching grid data from API: {e}")
        raise
    except ValueError as ve:
        print(f"Error parsing grid data: {ve}")
        raise
