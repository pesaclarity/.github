# Pesa Clarity

Your money, made clear, without giving your data away.

Pesa Clarity is a free, ad-free app for Android and iPhone that turns M-Pesa and bank messages into a clear daily plan: what you can spend today, what is due, where money leaks, and when you will be debt-free. All analysis runs on the phone. The server only signs you in, holds backups it cannot read, and combines anonymous model updates.

Everything is open source, so anyone can check that money data never leaves the phone.

## Download

Test builds for Android are on [the app's Releases](https://github.com/pesaclarity/pesaclarity-app/releases), refreshed from every change to `dev`:

- [Android](https://github.com/pesaclarity/pesaclarity-app/releases/download/test-build/pesaclarity-play.apk) (`pesaclarity-play.apk`), with Google sign-in.
- [F-Droid build](https://github.com/pesaclarity/pesaclarity-app/releases/download/test-build/pesaclarity-foss.apk) (`pesaclarity-foss.apk`), with no Google services.

Open the file on your phone and allow installs when asked. If it helps you, [star the app](https://github.com/pesaclarity/pesaclarity-app) so others find it. Website: [pesaclarity.github.io](https://pesaclarity.github.io).

## What it does

- **A daily plan.** Safe to spend today, bills due, money leaks, goals and a debt-free date.
- **Personal and business.** Keep separate spaces for you, a business, a household, a chama, rentals or a farm. Data never crosses between them; you can rename, clear, move transactions between, or delete any space, with 30 days to change your mind if you want it.
- **Your currencies.** A base currency of your choice, with foreign amounts shown both ways.
- **Export and print.** Your data as CSV in two taps; a business can print receipts on a Bluetooth printer.
- **Encrypted backups.** On the phone, to Google Drive, or to our vault, which cannot read them.

## Free, paid for by gifts

Every feature is free and stays free. If Pesa Clarity helps you, you can give on the [Sponsor page](https://pesaclarity.github.io/sponsor/) or from Support in the F-Droid build. Giving never unlocks anything.

## Principles

1. **Free forever, no ads.**
2. **Your data stays yours, on your phone.**
3. **Plain answers, not spreadsheets.**
4. **Export in two taps.**
5. **Honest money maths.**

## Repositories

| Repo | What | Licence |
| --- | --- | --- |
| [pesaclarity-app](https://github.com/pesaclarity/pesaclarity-app) | The Flutter app for Android and iPhone | AGPL-3.0 |
| [ujumbe-parsers](https://github.com/pesaclarity/ujumbe-parsers) | SMS parser packs and engine (ujumbe) | Apache-2.0 |
| [pesaclarity-backend](https://github.com/pesaclarity/pesaclarity-backend) | Sign-in, encrypted backup vault, federated learning (ngome) | AGPL-3.0 |
| [pesaclarity-ml](https://github.com/pesaclarity/pesaclarity-ml) | On-device categoriser, message reader and privacy audits (akili) | AGPL-3.0 |
| [pesaclarity-web](https://github.com/pesaclarity/pesaclarity-web) | Website (dirisha) | AGPL-3.0, text CC BY 4.0 |
| [docs](https://github.com/pesaclarity/docs) | Spec, brand, decisions | CC BY 4.0 |

## Get involved

- **Star [pesaclarity-app](https://github.com/pesaclarity/pesaclarity-app).** It is the quickest way to help: stars show people the project is alive and help them find it.
- **Add your bank, Sacco or wallet.** A small YAML pack with synthetic sample messages in [ujumbe-parsers](https://github.com/pesaclarity/ujumbe-parsers); no Flutter needed.
- **Build with us.** Flutter, Python, machine learning, design, copy and Swahili are all welcome. Start with [good first issues](https://github.com/search?q=org%3Apesaclarity+label%3A%22good+first+issue%22+is%3Aopen&type=issues), [help wanted](https://github.com/search?q=org%3Apesaclarity+label%3A%22help+wanted%22+is%3Aopen&type=issues) and the [contributing guide](https://github.com/pesaclarity/.github/blob/main/CONTRIBUTING.md).

Status: pre-alpha. Test builds are on Releases; not yet on the Play Store or F-Droid.
