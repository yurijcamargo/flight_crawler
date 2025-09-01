# Flight Crawler

Flight Crawler is an asynchronous Python application for scraping flight information from Google Flights. It extracts details such as departure/arrival times, airline, duration, stops, price, CO2 emissions, and more, saving the results to a CSV file.




## Features

- Scrapes flight data from Google Flights
- Asynchronous scraping using Playwright
- Saves results to CSV with pandas
- Proxy support via environment variables
- Easily configurable and extensible

## Requirements

- Python 3.8+
- [Playwright](https://playwright.dev/python/)
- pandas
- python-dotenv

Install dependencies with:

```sh
pip install -r requirements.txt
````

## Usage

### 1. Set up your environment

(Optional) Create and activate a virtual environment:

```sh
python -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows PowerShell
.\.venv\Scripts\Activate.ps1
```

### 2. Configure proxy (optional)

Edit the `.env` file to set proxy settings if needed.

### 3. Run the scraper

Execute the CLI script:

```sh
python src/presentation/cli/main.py
```

The results will be saved to `google_flights.csv`.

## Project Structure

```
src/
  application/
    factories/
    use_cases/
  domain/
    entities/
    repositories/
    services/
  infrastructure/
    config/
    repositories/
    scrapers/
    url_builders/
  presentation/
    cli/
```

## Customization

* To change the departure, destination, or date, edit the parameters in `main.py`.
* To add new scrapers or output formats, extend the factory and repository classes.

## License

MIT License
