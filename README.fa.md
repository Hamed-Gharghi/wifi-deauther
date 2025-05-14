# HMD Wifi Killer 🔥

<div align="center">

[English](README.md) | [فارسی](README.fa.md)

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Linux-red.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen.svg)

</div>

## 📝 توضیحات

HMD Wifi Killer یک ابزار قدرتمند برای حملات deauthentication وای‌فای است که برای اهداف آموزشی و تست طراحی شده است. این ابزار با رابط کاربری آسان، امکان انجام حملات deauthentication را با استفاده از هر دو روش mdk4 و aircrack-ng فراهم می‌کند.

## ⚠️ هشدار

این ابزار صرفاً برای اهداف آموزشی ارائه شده است. استفاده از این ابزار علیه شبکه‌هایی که مجوز ندارید، غیرقانونی است. نویسنده مسئول سوء استفاده یا خسارات ناشی از این برنامه نیست.

## 🚀 قابلیت‌ها

- 🔍 اسکن تعاملی شبکه‌ها
- 🎯 روش‌های حمله متنوع (mdk4 و aircrack-ng)
- 🖥️ تشخیص خودکار رابط شبکه
- 📊 نمایش اطلاعات دقیق شبکه
- 🎨 رابط ترمینال رنگی و زیبا
- 🔄 نصب خودکار ابزارها
- 🛡️ بررسی دسترسی root
- 🎮 منوی تعاملی کاربرپسند

## 📋 نیازمندی‌ها

- Python 3.x
- سیستم عامل لینوکس
- دسترسی root
- کارت شبکه بی‌سیم با پشتیبانی از حالت مانیتور

### ابزارهای مورد نیاز
- مجموعه aircrack-ng
- mdk4
- scapy
- termcolor

## 🛠️ نصب

1. کلون کردن مخزن:
```bash
git clone https://github.com/Hamed-Gharghi/wifi-deauther.git
cd wifi-deauther
```

2. قابل اجرا کردن اسکریپت:
```bash
chmod +x wifi_deauther.py
```

3. اجرای اسکریپت با دسترسی root:
```bash
sudo python3 wifi_deauther.py
```

## 💻 نحوه استفاده

1. اجرای اسکریپت با sudo:
```bash
sudo python3 wifi_deauther.py
```

2. انتخاب رابط شبکه بی‌سیم از لیست

3. انتخاب روش حمله:
   - mdk4 (تهاجمی‌تر)
   - aircrack-ng (پایدارتر)

4. انتخاب شبکه هدف یا حمله به همه شبکه‌ها

5. فشردن Ctrl+C برای توقف حمله

## 🎯 روش‌های حمله

### روش mdk4
- حمله تهاجمی‌تر
- امکان هدف قرار دادن کلاینت‌های خاص
- نرخ بسته بالاتر

### روش aircrack-ng
- حمله پایدارتر
- سازگاری بهتر
- مصرف منابع کمتر

## 🔧 آرگومان‌های خط فرمان

```bash
-i, --interface    مشخص کردن رابط شبکه بی‌سیم
-t, --target      آدرس MAC شبکه وای‌فای هدف
-g, --gateway     آدرس MAC گیت‌وی (اختیاری)
-n, --count       تعداد بسته‌های deauthentication (پیش‌فرض: 1000)
```

## 📝 مجوز

این پروژه تحت مجوز MIT منتشر شده است - برای جزئیات به فایل [LICENSE](LICENSE) مراجعه کنید.

## 👨‍💻 نویسنده

- **حامد غرقی**
- GitHub: [@Hamed-Gharghi](https://github.com/Hamed-Gharghi)

## ⭐ پشتیبانی

اگر این ابزار برای شما مفید بود، لطفاً به آن در GitHub ستاره دهید!

## 📞 تماس

برای هرگونه سوال یا پیشنهاد، لطفاً یک issue در GitHub ایجاد کنید.

---

<div align="center">
ساخته شده با ❤️ توسط حامد غرقی
</div> 