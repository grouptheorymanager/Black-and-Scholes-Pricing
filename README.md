# Black-Scholes Pricing

This project implements the Black-Scholes model for pricing European call and put options. It includes a Python script for calculations, a Jupyter notebook for testing and analysis, and a Streamlit web application for user-friendly option pricing.

## Features

- Calculates European call and put option prices using the Black-Scholes formula.
- Computes option Greeks (e.g., Delta, Gamma) for sensitivity analysis.
- Jupyter notebook for testing the model with example calculations and visualizations.
- Streamlit web app for interactive parameter input and result display.
- Modular Python script for programmatic use.

## Technologies Used

- Python 3.8+
- Libraries: `numpy`, `scipy`, `pandas`, `matplotlib`, `streamlit`
- Jupyter Notebook for interactive analysis
- Streamlit for the web interface

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/grouptheorymanager/Black-and-Schoels-Pricing.git
   cd Black-and-Schoels-Pricing
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Install Jupyter Notebook if not already installed:
   ```bash
   pip install jupyter
   ```

## Usage

### Option 1: Streamlit Web App

Run the Streamlit app to interact with the Black-Scholes model via a web interface:

```bash
streamlit run streamlit_app.py
```

- Open your browser to `http://localhost:8501`.
- Enter parameters (e.g., stock price, strike price, time to maturity, volatility, risk-free rate) to calculate option prices and view Greeks.

### Option 2: Jupyter Notebook

Test and analyze the model interactively:

1. Navigate to the `notebooks` folder:
   ```bash
   cd notebooks
   ```
2. Launch the notebook:
   ```bash
   jupyter notebook test_model.ipynb
   ```
3. Follow the notebook to run example calculations, input parameters, and view visualizations.

### Option 3: Python Script

Use the `bs_model.py` script for programmatic calculations:

```bash
python src/bs_model.py
```

- Edit the script to set parameters (e.g., stock price, strike price, volatility) or integrate it into other projects.

## Project Structure

- `src/bs_model.py`: Core Python script for Black-Scholes calculations.
- `notebooks/test_model.ipynb`: Jupyter notebook for testing and analyzing the model.
- `streamlit_app.py`: Streamlit web application for user-friendly option pricing.
- `requirements.txt`: Lists required Python libraries.

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make changes and commit (`git commit -m "Add feature"`).
4. Push to your fork (`git push origin feature-branch`).
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Notes

For questions or feedback, open an issue on GitHub.
