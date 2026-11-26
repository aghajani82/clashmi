# Iran Lite for Clash Mi on iOS

Install [the official Clash Mi app](https://apps.apple.com/us/app/clash-mi/id6744321968).
Iran Lite is delivered through the Mihomo subscription.

## Sanaei subscription

In **Panel Settings → Clash / Mihomo**, enable routing and use the following
URL as **Global routing rules**, if your subscription uses a group named
`PROXY` and you want the same standalone routing policy as the other Iran
Lite clients.

```text
https://raw.githubusercontent.com/aghajani82/clashmi/main/iran-lite/routing-overlay.yaml
```

Save and apply the settings, then import or update your usual `/mihomo/`
subscription in Clash Mi. Use Rule mode. If you already maintain other routing
rules, merge the two provider entries and direct rules into your existing
YAML and retain its proxy group and catch-all. The example does not contain
any server or subscription credential.
Keep the same subscription and overlay URLs. Clash Mi's Mihomo core refreshes
the providers every 86,400 seconds while running. Use the provider update
control, if available, to fetch the new provider files immediately.

The two binary providers preserve all 57,572 domain suffix matchers and
2,825 IPv4/IPv6 CIDRs from the [shared Windows preset](https://github.com/aghajani82/v2rayN/blob/master/v2rayN/ServiceLib/Sample/custom_routing_iran_lite.gz).
The compact MRS format is supported by Mihomo. To reproduce the providers:

```sh
python3 iran-lite/convert.py /path/to/custom_routing_iran_lite.gz /path/to/mihomo
```

## به‌روزرسانی قوانین در v2rayN و v2rayNG

با هستهٔ Xray می‌توان قوانین Iran Lite را از فایل‌های دادهٔ جداگانه خواند. این روش
یک بار تنظیم می‌شود و برای به‌روزرسانی‌های بعدی نیازی به نصب دوباره، حذف برنامه
یا واردکردن دوبارهٔ لینک ساب ندارد.

| نام فایل | آدرس ثابت |
| --- | --- |
| `iran-lite-domains.dat` | [دانلود دامنه‌ها](https://raw.githubusercontent.com/aghajani82/clashmi/main/iran-lite/iran-lite-domains.dat) |
| `iran-lite-ips.dat` | [دانلود محدوده‌های IP](https://raw.githubusercontent.com/aghajani82/clashmi/main/iran-lite/iran-lite-ips.dat) |
| `xray-routing.json` | [پروفایل Iran Lite](https://raw.githubusercontent.com/aghajani82/clashmi/main/iran-lite/xray-routing.json) |

- **ویندوز (v2rayN)** — دو فایل DAT را در پوشهٔ `bin` برنامه بگذار.
  در تنظیمات Routing، مجموعهٔ `Aghajani Edition - Iran Lite` را باز کن. آدرس JSON را در
  **URL (optional)** بگذار و **Import Rules From Subscription URL** را بزن.
  برای جایگزینی قوانین موجود، در پرسش افزودن به انتهای فهرست **No** را بزن.
  ذخیره کن و مطمئن شو مجموعهٔ Iran Lite فعال و **Domain strategy** روی
  `IPOnDemand` است. برای به‌روزرسانی‌های بعدی فقط دو فایل DAT را جایگزین
  و اتصال را یک بار قطع و وصل کن.
- **اندروید (v2rayNG)** — در **Geo files** یا **Assets**، دو منبع با نام
  دقیق فایل‌های DAT و آدرس‌های جدول اضافه کن و دکمهٔ دانلود را بزن.
  بعد از دانلود موفق، آدرس فایل JSON را کپی کن و در **Routing Settings → Import
  Rulesets from Clipboard** وارد کن. **Domain strategy** را روی `IPOnDemand`
  بگذار. برای به‌روزرسانی‌های بعدی فقط دکمهٔ دانلود Geo files را بزن و اتصال
  را یک بار قطع و وصل کن.

JSON قوانین فعلی روتینگ را جایگزین می‌کند. اگر قانون شخصی داری، پیش از
واردکردن JSON از قواعد خودت خروجی بگیر. نسخهٔ Preview 3 یا جدیدتر استثناهای
ChatGPT را هنگام استفاده از Iran Lite اعمال می‌کند.

The source lists are [Chocolate4U/Iran-v2ray-rules](https://github.com/Chocolate4U/Iran-v2ray-rules)
(GPLv3) and [bootmortis/iran-hosted-domains](https://github.com/bootmortis/iran-hosted-domains) (MIT).

## Custom iOS binary

The public Clash Mi checkout refers to local Flutter packages
`../libclash-vpn-service` and `../board-service`, and to
`bind/apple/Libclash.xcframework`. The public fork needs those build inputs
before it can produce a custom iOS app. Distribution of a custom build also
requires Apple signing and provisioning for the app and its VPN extension.
A shareable TestFlight link can be created only after a signed build is
uploaded to App Store Connect and approved for external testing.

## bootmortis MIT notice

Copyright (c) 2022 bootmortis

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
