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

The two binary providers preserve all 57,569 domain suffix matchers and
2,825 IPv4/IPv6 CIDRs from the [shared Windows preset](https://github.com/aghajani82/v2rayN/blob/master/v2rayN/ServiceLib/Sample/custom_routing_iran_lite.gz).
The compact MRS format is supported by Mihomo. To reproduce the providers:

```sh
python3 iran-lite/convert.py /path/to/custom_routing_iran_lite.gz /path/to/mihomo
```

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
