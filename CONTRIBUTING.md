# Contributing to the Router IP Database

We welcome contributions from network engineers, sysadmins, and homelabbers!

## How to Add or Update a Router Model

1. **Fork** this repository.
2. Add your hardware entry to `data/routers.json` following this schema:
   ```json
   {
     "brand": "Manufacturer Name",
     "model": "Model Name and Number",
     "slug": "brand-model-slug",
     "default_ip": "192.168.1.1",
     "default_username": "admin",
     "default_password": "password",
     "wifi_standard": "Wi-Fi 6 (802.11ax)",
     "web_profile": "https://routeriphub.com/routers/brand-model-slug/"
   }
   ```
3. Append the row to `data/routers.csv`.
4. Open a **Pull Request** with the title `Add [Brand] [Model]`.

For live diagnostic tools, subnet calculators, and Wi-Fi QR tools, visit [RouterIPHub](https://routeriphub.com/).
