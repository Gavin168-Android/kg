import json
import glob
import os

# ========== 配置区域 ==========
NEW_TITLE = "https://你的新地址.com/?c=xxx"   # ← 改成你想要的新 title
FILE_PATTERN = "a*.json"                     # 匹配 a1.json ~ a100.json
# =============================

for filepath in glob.glob(FILE_PATTERN):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 修改 title
        if "data" in data and "title" in data["data"]:
            old_title = data["data"]["title"]
            data["data"]["title"] = NEW_TITLE
            print(f"已修改: {filepath}  |  旧值: {old_title}")
        
        # 写回文件（保持缩进美观）
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            
    except Exception as e:
        print(f"处理失败 {filepath}: {e}")

print("\n全部处理完成！")
