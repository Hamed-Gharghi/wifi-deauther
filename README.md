# WiFi Deauther

یک ابزار برای انجام حملات deauthentication بر روی شبکه‌های وای‌فای.

**هشدار:** استفاده از این ابزار برای حمله به شبکه‌هایی که مجوز ندارید، غیرقانونی و غیراخلاقی است. این ابزار فقط برای اهداف آموزشی و تست امنیت شبکه ارائه می‌شود.

## نصب

1. ابتدا repository را clone کنید:

   ```bash
   git clone https://github.com/YOUR_USERNAME/wifi-deauther.git
   cd wifi-deauther
   ```

2. سپس وابستگی‌ها را نصب کنید:

   ```bash
   pip3 install -r requirements.txt
   ```

## استفاده

1. برنامه را با دسترسی root اجرا کنید:

   ```bash
   sudo python3 wifi_deauther.py -i <interface> -t <target_bssid> -g <gateway_bssid> -n <packet_count>
   ```

   *   `-i` یا `--interface`: نام کارت شبکه بی‌سیم خود را مشخص کنید.
   *   `-t` یا `--target`: آدرس MAC شبکه وای‌فای مورد نظر را مشخص کنید.
   *   `-g` یا `--gateway`: آدرس MAC روتر را مشخص کنید (اختیاری).
   *   `-n` یا `--count`: تعداد بسته‌های deauthentication که می‌خواهید ارسال کنید را مشخص کنید (اختیاری).

## مجوز

این پروژه تحت مجوز MIT منتشر شده است.

## مشارکت

برای مشارکت در این پروژه، می‌توانید از طریق pull request اقدام کنید. 