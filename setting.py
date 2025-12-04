

import ultralytics


settings = ultralytics.utils.SettingsManager()


settings.update(runs_dir="D:/MyCode/public_project/yolov8-traffic-app/runs")
settings.update(datasets_dir="D:/MyCode/public_project/yolov8-traffic-app/dataset")


print(settings["runs_dir"]) 
print(settings["datasets_dir"])
