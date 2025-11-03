import psutil
from plyer import notification

cpu_threshold = 50
mem_threshold = 50

cpu_alert_active = False
mem_alert_active = False

print("Monitoring initiated.")

try:
    while True:
        cpu_percent = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory()
        memory_percent = memory.percent

        # CPU alert logic
        if cpu_percent > cpu_threshold and not cpu_alert_active:
            notification.notify(
                title="⚠️ CPU Warning",
                message=f"CPU usage above {cpu_threshold}%, current: {cpu_percent}%",
                timeout=5,
            )

            cpu_alert_active = True
        elif cpu_percent <= cpu_threshold:
            cpu_alert_active = False

        # Memory alert logic
        if memory_percent > mem_threshold and not mem_alert_active:
            notification.notify(
                title="⚠️ Memory Warning",
                message=f"Memory usage above {mem_threshold}%, current: {memory_percent}%",
                timeout=5,
            )

            mem_alert_active = True
        elif memory_percent <= mem_threshold:
            mem_alert_active = False
except KeyboardInterrupt:
    print("Monitoring stopped by user.")
