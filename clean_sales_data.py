import pandas as pd
from pathlib import Path

# 実行環境に合わせてパスを安全に取得（Jupyter等への対策）
try:
    base = Path(__file__).parent
except NameError:
    base = Path.cwd()

input_file = base / "data" / "sales1.csv"
output_folder = base / "output"

# ★【修正ポイント】outputフォルダがなければ自動で作成する
output_folder.mkdir(parents=True, exist_ok=True)

# 読み込みの安全対策
try:
    df = pd.read_csv(input_file)
except FileNotFoundError:
    print(f"エラー: ファイルが見つかりません → {input_file}")
    print("data フォルダの中に sales1.csv があるか確認してください。")
    exit()

print(f"元の行数: {len(df)}")
cleaned = df.drop_duplicates()
print(f"重複削除後: {len(cleaned)}")

# 保存の安全対策
try:
    output_path = output_folder / "重複削除結果.xlsx"
    cleaned.to_excel(output_path, index=False)
    print(f"完了: {output_path}")
except Exception as e:
    print(f"エラーが発生しました: {e}")