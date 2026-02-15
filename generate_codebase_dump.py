
import os

files_to_dump = [
    # Root
    r"get_chat_id.py",
    r"index.html",
    r"start_backend.bat",
    r"start_frontend.bat",
    r"verify_logic.py",
    r"verify_telegram.py",
    
    # Backend
    r"urban-sanitation-platform\backend\app\main.py",
    r"urban-sanitation-platform\backend\app\database.py",
    r"urban-sanitation-platform\backend\app\models.py",
    r"urban-sanitation-platform\backend\app\schemas.py",
    r"urban-sanitation-platform\backend\app\crud.py",
    r"urban-sanitation-platform\backend\app\logic.py",
    r"urban-sanitation-platform\backend\app\routers\analytics.py",
    r"urban-sanitation-platform\backend\app\routers\config.py",
    r"urban-sanitation-platform\backend\app\routers\incidents.py",
    r"urban-sanitation-platform\backend\app\routers\tasks.py",
    r"urban-sanitation-platform\backend\get_chat_ids.py",
    r"urban-sanitation-platform\backend\check_time.py",
    r"urban-sanitation-platform\backend\requirements.txt",
    
    # Frontend
    r"urban-sanitation-platform\frontend\package.json",
    r"urban-sanitation-platform\frontend\postcss.config.js",
    r"urban-sanitation-platform\frontend\eslint.config.js",
    r"urban-sanitation-platform\frontend\index.html",
    r"urban-sanitation-platform\frontend\src\main.jsx",
    r"urban-sanitation-platform\frontend\src\App.jsx",
    r"urban-sanitation-platform\frontend\src\App.css",
    r"urban-sanitation-platform\frontend\src\index.css",
    r"urban-sanitation-platform\frontend\src\api\client.js",
    r"urban-sanitation-platform\frontend\src\components\AnalyticsCharts.jsx",
    r"urban-sanitation-platform\frontend\src\components\ConfigPanel.jsx",
    r"urban-sanitation-platform\frontend\src\components\Dashboard.jsx",
    r"urban-sanitation-platform\frontend\src\components\ReportIncidentForm.jsx",
    r"urban-sanitation-platform\frontend\src\components\TaskBoard.jsx",
    r"urban-sanitation-platform\frontend\src\components\ZoneCard.jsx"
]

output_file = "project_codebase.txt"

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("PROJECT CODEBASE DUMP\n")
    outfile.write("=====================\n\n")
    
    for filepath in files_to_dump:
        abs_path = os.path.abspath(filepath)
        
        outfile.write(f"=== START FILE: {filepath} ===\n")
        
        if os.path.exists(abs_path):
            try:
                with open(abs_path, "r", encoding="utf-8") as infile:
                    content = infile.read()
                    outfile.write(content)
            except Exception as e:
                outfile.write(f"Error reading file: {e}\n")
        else:
             outfile.write(f"File not found: {abs_path}\n")
             
        outfile.write(f"\n=== END FILE: {filepath} ===\n\n")

print(f"Dump complete to {os.path.abspath(output_file)}")
