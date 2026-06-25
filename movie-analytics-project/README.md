# 🎬 Movie Industry Analytics Project

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Pandas](https://img.shields.io/badge/Pandas-Latest-green.svg)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Latest-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 📊 Project Overview

This data analytics project explores movie industry trends from 2010-2023, analyzing box office performance, genre popularity, studio success rates, and return on investment (ROI) patterns. The project demonstrates end-to-end data analysis using Python, pandas, matplotlib, and seaborn.

## 🎯 Key Objectives

1. **Genre Analysis**: Which genres generate the highest revenue and ROI?
2. **Temporal Trends**: How has the movie industry evolved over the years?
3. **Studio Performance**: Which studios are most successful?
4. **Profitability Factors**: What drives a movie's financial success?
5. **Budget Correlation**: Does higher budget guarantee box office success?

## 📁 Project Structure

```
movie-analytics-project/
│
├── data/
│   ├── movies_dataset.csv          # Main dataset (500 movies)
│   └── analysis_summary.csv        # Summary statistics
│
├── notebooks/
│   └── movie_analysis.ipynb        # Main analysis notebook
│
├── visualizations/
│   ├── genre_analysis.png          # Genre performance charts
│   ├── yearly_trends.png           # Temporal trend analysis
│   ├── studio_performance.png      # Studio comparison
│   ├── correlation_matrix.png      # Feature correlation heatmap
│   └── budget_analysis.png         # Budget vs revenue scatter plots
│
├── scripts/
│   └── (optional Python scripts)
│
├── requirements.txt                # Python dependencies
└── README.md                       # Project documentation
```

## 🔧 Technologies Used

- **Python 3.8+**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computing
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Jupyter Notebook**: Interactive analysis environment

## 📦 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/movie-analytics-project.git
cd movie-analytics-project
```

### 2. Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the analysis
```bash
jupyter notebook notebooks/movie_analysis.ipynb
```

## 📈 Dataset Description

The dataset contains **500 movies** with the following attributes:

| Column | Description |
|--------|-------------|
| `title` | Movie title |
| `genre` | Movie genre (Action, Comedy, Drama, etc.) |
| `year` | Release year (2010-2023) |
| `runtime_minutes` | Movie duration in minutes |
| `budget_millions` | Production budget in millions USD |
| `box_office_millions` | Box office revenue in millions USD |
| `rating` | MPAA rating (G, PG, PG-13, R, NC-17) |
| `imdb_score` | IMDB rating (4.0-9.0) |
| `studio` | Production studio |
| `director_experience_years` | Director's years of experience |
| `num_theaters` | Number of theaters in release |
| `profit_millions` | Profit (box office - budget) |
| `roi_percentage` | Return on investment percentage |

## 🔍 Key Insights

### Genre Performance
- **Highest Revenue Genres**: Action and Sci-Fi dominate box office
- **Best ROI**: Horror and Documentary films offer excellent returns on smaller budgets
- **Most Produced**: Drama is the most frequently produced genre

### Budget Analysis
- Strong positive correlation between budget and box office revenue
- However, ROI decreases with higher budgets
- Sweet spot exists for mid-budget films ($50-100M)

### Studio Analysis
- Major studios (Disney, Universal, Warner Bros) lead in total revenue
- Independent studios show competitive ROI with focused strategies

### Temporal Trends
- Steady growth in average budgets over time
- Box office volatility increases post-2020
- IMDB scores remain relatively stable

## 📊 Sample Visualizations

The project includes comprehensive visualizations:
- **Genre Analysis**: Bar charts and box plots
- **Yearly Trends**: Time series analysis
- **Correlation Matrix**: Feature relationship heatmap
- **Budget vs Revenue**: Scatter plots with IMDB score overlay

## 🚀 Future Enhancements

- [ ] Add machine learning models to predict box office success
- [ ] Incorporate additional data sources (Rotten Tomatoes, Metacritic)
- [ ] Interactive dashboard using Plotly/Dash or Streamlit
- [ ] Sentiment analysis on movie reviews
- [ ] International box office breakdown
- [ ] Actor/Director influence analysis

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.


## 🙏 Acknowledgments

- Dataset created for educational and portfolio purposes
- Inspired by real-world movie industry analytics
- Thanks to the open-source community for amazing tools

---

⭐ **Star this repository if you find it helpful!**
