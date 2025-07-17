![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-success)
![Version](https://img.shields.io/badge/version-1.0-yellow)
![Monte Carlo Modeling](https://img.shields.io/badge/Monte%20Carlo-Financial%20Simulation-darkblue)

# 🔮 IONQ Monte Carlo Simulator

A Streamlit-powered app that runs Monte Carlo simulations to model future price distributions for IONQ stock using geometric Brownian motion.

---
## 📁 Project Structure

```plaintext
Monte Carlo/
├── .venv/           # Virtual environment  
├── app.py           # Streamlit UI  
├── simulator.py     # Simulation logic (geometric Brownian motion)  
├── charts.py        # Visualization functions  
├── requirements.txt # Python dependencies  
└── README.md        # Project overview  
```

## 🚀 How to Run
Activate your virtual environment and install dependencies:
```
pip install -r requirements.txt
streamlit run app.py
```

## 🔧 Parameters
Use the Streamlit sidebar to adjust:
- Initial price
- Daily return
- Daily volatility
- Time horizon
- Number of simulation runs
## 📊 Output
The app displays:
- Simulated price distribution (histogram)
- Percent change distribution
- Median, min, max values
- Optional raw simulation data
## 💡 Future Enhancements
Not included yet, but candidates for later versions:
Trajectory plots with multiple simulated paths
Value at Risk (VaR) visualization
Preset market scenarios (bull/bear/shock)
Sensitivity analysis for return/volatility parameters
**Version 1.0** – Functional baseline completed. Ready for iterative enhancement.

Let me know if you’d like to add contributor credits, Git instructions, or a quick-start gif/screenshot section next. This version is clean, complete, and perfectly geared for future growth.

