from pathlib import Path

from src.pipeline import run_project


if __name__ == "__main__":
    result = run_project(Path(__file__).resolve().parent)
    print(f"Champion model: {result['champion']}")
    print(f"Chosen hyperparameters: {result['chosen']}")
    print(f"Empirical 90% absolute-error threshold: {result['q90']:.2f} m3")
    for row in result["metrics"]:
        print(f"{row['model']}: MAE={row['mae_m3']:.2f}, RMSE={row['rmse_m3']:.2f}, MAPE={row['mape_percent']:.2f}%")

