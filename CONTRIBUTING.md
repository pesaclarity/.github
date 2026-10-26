# Contributing to Pesa Clarity

Thanks for helping. This guide applies to every repository in the organisation; a repo's own `CONTRIBUTING.md` adds setup and checks specific to it.

## Before you start

- Read the [product spec](https://github.com/pesaclarity/docs/blob/main/spec/PRODUCT-SPEC.md). Changes that go against its principles (no ads, data stays on the phone, honest money maths) will not be merged.
- For anything bigger than a small fix, open an issue first so we can agree on the approach.
- Be kind. Everyone here follows the [code of conduct](CODE_OF_CONDUCT.md).

## Never commit

- Real SMS messages, statements, phone numbers, names or account numbers. Test data must be synthetic or fully anonymised. Pull requests containing real personal data are closed and the history is purged.
- Secrets of any kind: API keys, signing keys, `.env` files, keystores.

## Pull requests

1. Fork the repo and branch from `main`.
2. Keep each pull request to one change. Small is easier to review.
3. Add or update tests. CI must pass.
4. Write commit messages in the imperative ("Add KCB paybill rule"), with a short body when the reason isn't obvious.
5. Fill in the pull request template. If the change alters the spec, open a matching pull request in [docs](https://github.com/pesaclarity/docs).

`main` is protected: changes land through reviewed pull requests with passing CI, and force-pushes are off.

## Code style

- Follow the formatter and linter configured in each repo; CI enforces them.
- Prefer clear names over comments. Comment only to explain why, not what.
- Public APIs get short doc comments.

## Licensing of contributions

Each repo states its licence in `LICENSE`:

- `pesaclarity-app`, `pesaclarity-backend`, `pesaclarity-ml`, `pesaclarity-web` code: AGPL-3.0
- `ujumbe-parsers`: Apache-2.0
- `docs`, `.github`, website text: CC BY 4.0

You keep the copyright in your contribution and license it under the repo's licence. The AGPL repos will also offer a commercial licence on request, which funds keeping the app free; for that, contributions to those repos will need a contributor licence agreement. Until the agreement is published, maintainers will ask before merging outside code into the AGPL repos.

The Pesa Clarity name and logo are trademarks and are not licensed for forks.

## Security issues

Do not open public issues for vulnerabilities. See [SECURITY.md](SECURITY.md).
