# codeprint

Print a 6–8 digit code in the middle of an 80mm ticket on `10.99.10.81:9100`.

The ticket is a 576×640 raster (80mm at 203 dpi, the same `GS v 0` path thermprint uses). The digits are drawn in the center of that image. A leading paper feed is not used, because this printer discards one and the code stays at the top.

```sh
curl -fsSL -o ~/.local/bin/codeprint \
  https://raw.githubusercontent.com/mikeybob/codeprint-public/main/codeprint \
  && chmod +x ~/.local/bin/codeprint \
  && codeprint 12345678
```

| Env | Default | |
| --- | --- | --- |
| `PRINTER_IP` | `10.99.10.81` | |
| `PRINTER_PORT` | `9100` | |
| `CODEPRINT_DUMP` | unset | Write the bytes to this file instead of printing |
