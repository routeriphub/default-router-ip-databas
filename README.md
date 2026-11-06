# 🌐 Universal Default Router IP & Hardware Database

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Models Indexed](https://img.shields.io/badge/Models-250%2B-green.svg)](https://routeriphub.com/routers/)
[![Formats](https://img.shields.io/badge/Formats-JSON%20%7C%20CSV-orange.svg)](#-data-formats)
[![Live Directory](https://img.shields.io/badge/Web-routeriphub.com-purple.svg)](https://routeriphub.com/)

An open-source, machine-readable database of default gateway IP addresses, admin credentials, Wi-Fi naming schemes, and diagnostic specifications for over **250+ enterprise and consumer wireless routers**.

Curated and maintained by [RouterIPHub.com](https://routeriphub.com/).

---

## ⚡ Quick Access by Gateway Subnet

| Gateway IP | Primary Manufacturers | Direct Interactive Hub |
| :--- | :--- | :--- |
| `192.168.1.1` | Netgear, ASUS, Linksys, Cisco, Verizon Fios, Ubiquiti | [192.168.1.1 Setup Guide](https://routeriphub.com/ip/192-168-1-1/) |
| `192.168.0.1` | TP-Link, D-Link, Netgear, Tenda | [192.168.0.1 Setup Guide](https://routeriphub.com/ip/192-168-0-1/) |
| `192.168.2.1` | Belkin, Bell Canada Home Hub, SMC, Edimax | [192.168.2.1 Setup Guide](https://routeriphub.com/ip/192-168-2-1/) |
| `10.0.0.1` | Xfinity / Comcast xFi, Apple AirPort | [10.0.0.1 Setup Guide](https://routeriphub.com/ip/10-0-0-1/) |
| `192.168.1.254` | AT&T Fiber BGW, BT Smart Hub, Bbox | [192.168.1.254 Guide](https://routeriphub.com/isp/att-bgw320/) |
| `192.168.88.1` | MikroTik RouterBOARD / RouterOS | [MikroTik Directory](https://routeriphub.com/brands/mikrotik/) |
| `192.168.8.1` | Huawei, GL.iNet Travel Routers | [192.168.8.1 Guide](https://routeriphub.com/ip/192-168-8-1/) |

---

## 💻 Developer Quickstart (cURL & jq)

Filter the raw JSON dataset directly from your command line:

```bash
# Query all Netgear models and their default passwords
curl -s https://raw.githubusercontent.com/routeriphub/default-router-ip-databas/main/data/routers.json \
  | jq '.[] | select(.brand=="Netgear") | {model: .model, ip: .default_ip, pass: .default_password}'
```

```bash
# Find which hardware runs on 192.168.2.1
curl -s https://raw.githubusercontent.com/routeriphub/default-router-ip-databas/main/data/routers.json \
  | jq '.[] | select(.default_ip=="192.168.2.1") | {brand: .brand, model: .model, pass: .default_password}'
```

---

## 🐍 Python Search Example

Run the included lookup script:

```bash
python examples/lookup.py Netgear
python examples/lookup.py 192.168.2.1
python examples/lookup.py "Archer AX55"
```

---

## 📊 Data Formats

- **JSON:** [`data/routers.json`](data/routers.json) (250+ structured models with Wi-Fi standard, credentials, and web profiles).
- **CSV:** [`data/routers.csv`](data/routers.csv) (Flat spreadsheet format for Pandas/Excel data analysis).
- **Gateway Mapping:** [`data/gateways.json`](data/gateways.json) (Subnet to manufacturer mapping matrix).

---

## 🌐 Interactive Network Tools (Live on Web)

In addition to this raw dataset, [RouterIPHub](https://routeriphub.com/) provides free client-side diagnostic utilities:
* **[IPv4 CIDR Subnet Calculator](https://routeriphub.com/tools/subnet-calculator/)** — Real-time usable host range, broadcast address, and CIDR prefix calculator.
* **[Wi-Fi QR Code Generator](https://routeriphub.com/tools/wifi-qr-code/)** — Generate encrypted WPA2/WPA3 guest network QR signs.
* **[Local Gateway IP Detector](https://routeriphub.com/find-router-ip.html)** — Auto-detect active router gateway IP.

---

## 🤝 Contributing

Contributions are welcomed! Have a new hardware model or updated firmware credentials?
1. Check [CONTRIBUTING.md](CONTRIBUTING.md).
2. Submit a Pull Request.

---

## 📄 License

This dataset is open-source and released under the [MIT License](LICENSE).
