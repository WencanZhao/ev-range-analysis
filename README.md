# EV Range in Cold Weather ❄️🔋

This project analyzes how low temperatures affect EV driving range, based on sample data.

## Data
- `ev_data_sample.csv` contains features like:
  - Ambient temperature
  - Speed
  - Battery age
  - Cabin heating
  - Route elevation gain
  - Baseline vs Measured range

## Method
- Calculate percentage range loss
- Visualize loss vs. temperature
- Observe the impact of heating

## Example Result
When you run the script, you’ll get a figure like this:

![Range Loss](results/range_loss.png)

## Requirements
```bash
pip install -r requirements.txt
