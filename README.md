# 📊 Business Data Analyzer

A Streamlit-based web application for analyzing and visualizing business data, particularly focused on financial metrics and demographic information.

## ✨ Features

- 📁 **Data Loading**: Upload and process CSV files with error handling
- 🧹 **Data Cleaning**: Convert selected columns to numeric format
- 📈 **Statistical Analysis**: Generate basic statistics and correlation matrices
- 🎨 **Interactive Visualizations**:
  - Distribution histograms for numeric data
  - Scatter plots comparing different metrics
  - Correlation heatmaps for numeric columns
- 🔍 **Data Exploration**: 
  - View and sort top entries
  - Customizable column selection
  - Interactive data filtering

## 🛠️ Prerequisites

```bash
pip install streamlit pandas matplotlib seaborn plotly numpy
```

## ⚡ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/business-data-analyzer.git
cd business-data-analyzer
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## 🚀 Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the provided local URL (typically `http://localhost:8501`)

3. Upload a CSV file containing your business data

4. Use the interactive interface to:
   - 🧹 Clean your data
   - 📊 Generate visualizations
   - 📈 Explore statistics
   - 🔄 Sort and filter results

## 📋 Input Data Format

The application expects a CSV file with the following recommended columns:
- `Name`: Individual/Entity name
- `NetWorth`: Numeric value representing net worth
- `Age`: Numeric value for age
- `Country`: Country of origin/operation

However, the app is flexible and can work with any CSV file containing numeric and categorical data.

## 🔥 Features in Detail

### 📁 Data Loading
- Supports CSV file format
- Includes error handling and validation
- Displays success/error messages

### 🧹 Data Cleaning
- Interactive column selection for numeric conversion
- Handles missing values and invalid entries
- Preserves original data while cleaning

### 📊 Visualization Types
1. **Distribution Analysis**
   - 📈 Histogram of net worth distribution
   - 📊 Frequency analysis of numeric variables

2. **Relationship Analysis**
   - 📉 Scatter plots of age vs. net worth
   - 🔍 Interactive hover data for detailed information

3. **Correlation Analysis**
   - 🌡️ Heatmap of numeric variable correlations
   - 📝 Annotated correlation coefficients

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💎 Acknowledgments

- Built with [Streamlit](https://streamlit.io/)
- Visualization powered by [Plotly](https://plotly.com/) and [Seaborn](https://seaborn.pydata.org/)
- Data handling with [Pandas](https://pandas.pydata.org/)
